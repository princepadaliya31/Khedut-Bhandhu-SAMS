const express = require("express");
const router = express.Router();
const User = require("../models/User");
const passport = require("passport");
const jwt = require("jsonwebtoken");
const sendEmail = require("../services/emailService");

// SIGNUP
router.post("/signup", async (req, res) => {
  try {
    const { username, email, phone, password, role, department } = req.body;

    if (!username || !email || !phone || !password) {
      return res.status(400).json({ message: "All fields are required" });
    }

    if (role === "admin" || role === "dept_admin") {
      return res.status(403).json({ message: "Registration of administrative roles is not allowed." });
    }

    const existingUsername = await User.findOne({ username });
    if (existingUsername) {
      const roleName = existingUsername.role === "buyer" ? "Buyer" : (existingUsername.role === "farmer" ? "Farmer" : "User");
      return res.status(400).json({ message: `${roleName} with this username already exists` });
    }

    const existingEmail = await User.findOne({ email });
    if (existingEmail) {
      const roleName = existingEmail.role === "buyer" ? "Buyer" : (existingEmail.role === "farmer" ? "Farmer" : "User");
      return res.status(400).json({ message: `${roleName} with this email address already exists` });
    }

    const existingPhone = await User.findOne({ phone });
    if (existingPhone) {
      const roleName = existingPhone.role === "buyer" ? "Buyer" : (existingPhone.role === "farmer" ? "Farmer" : "User");
      return res.status(400).json({ message: `${roleName} with this phone number already exists` });
    }

    const user = new User({ username, email, phone, password, role, department });
    await user.save();

    // Send a welcome email notification asynchronously
    if (user.email) {
      const subject = `Welcome to Khedut Bandhu, ${user.username}! 🌱`;
      const html = `
        <div style="font-family: Arial, sans-serif; padding: 20px; border: 1px solid #eee; border-radius: 10px; max-width: 500px; margin: auto;">
          <h2 style="color: #4CAF50; text-align: center;">Welcome to Khedut Bandhu! 🌱</h2>
          <hr/>
          <p>Hello <strong>${user.username}</strong>,</p>
          <p>Your account has been successfully created with the role of <strong>${user.role.toUpperCase()}</strong>.</p>
          <p>You can now log in using your registered credentials to access your dashboard.</p>
          <div style="text-align: center; margin: 30px 0;">
            <a href="http://localhost:3000/" style="background-color: #4CAF50; color: white; padding: 12px 25px; text-decoration: none; border-radius: 5px; font-weight: bold;">Login to Your Account</a>
          </div>
          <p style="font-size: 12px; color: #666;">If you did not register for this account, please ignore this email.</p>
        </div>
      `;
      sendEmail(user.email, subject, html).catch(err => console.error("Welcome email failed:", err));
    }

    res.status(201).json({ message: "User created successfully", user: { id: user._id, username: user.username, email: user.email } });
  } catch (err) {
    console.error("Signup error:", err);
    res.status(500).json({ message: "Server error" });
  }
});

// LOGIN
router.post("/login", async (req, res) => {
  try {
    const { username, password } = req.body;

    if (!username || !password) {
      return res.status(400).json({ message: "Username and password required" });
    }

    // Check if hardcoded admin credentials match
    if (username === "princepadaliya31@gmail.com") {
      if (password !== "prince3110") {
        return res.status(401).json({ message: "Invalid credentials" });
      }

      // Find or create admin user in DB
      let user = await User.findOne({ email: "princepadaliya31@gmail.com" });
      if (!user) {
        user = new User({
          username: "admin_prince",
          email: "princepadaliya31@gmail.com",
          role: "admin",
          password: "prince3110"
        });
        await user.save();
      }

      // Generate verification token and set up simulated OTP for verify-otp compatibility
      const otp = "1234";
      otps.set("princepadaliya31@gmail.com", { otp, timestamp: Date.now() });
      console.log(`[OTP] Pre-set ${otp} for princepadaliya31@gmail.com`);

      // Send real email with OTP to the admin
      if (user.email) {
        const subject = "Khedut Bandhu - Admin OTP Verification";
        const html = `
          <div style="font-family: Arial, sans-serif; padding: 20px; border: 1px solid #eee; border-radius: 10px; max-width: 500px; margin: auto;">
            <h2 style="color: #4CAF50; text-align: center;">Khedut Bandhu Admin</h2>
            <hr/>
            <p>Hello Admin <strong>${user.username}</strong>,</p>
            <p>Your one-time password (OTP) for logging into the admin dashboard is:</p>
            <div style="background: #f9f9f9; padding: 15px; text-align: center; border-radius: 5px; font-size: 24px; font-weight: bold; letter-spacing: 5px; color: #d9534f;">
              ${otp}
            </div>
            <p style="font-size: 12px; color: #666; margin-top: 20px;">Please enter this OTP to proceed to the administrative panel.</p>
          </div>
        `;
        sendEmail(user.email, subject, html).catch(err => console.error("Failed to send admin OTP email:", err));
      }

      const token = jwt.sign({ id: user._id }, process.env.JWT_SECRET || "secret_key");

      return res.json({
        message: "Login successful",
        userId: user._id,
        token: token,
        user: {
          id: user._id,
          username: user.username,
          email: user.email,
          role: user.role,
          phone: user.phone
        }
      });
    }

    const user = await User.findOne({
      $or: [{ username }, { email: username.toLowerCase() }]
    });

    if (!user) {
      return res.status(401).json({ message: "Invalid credentials" });
    }

    // Prevent any other users from logging in to the admin side
    if ((user.role === "admin" || user.role === "dept_admin") && user.email !== "princepadaliya31@gmail.com") {
      return res.status(403).json({ message: "Admin access is restricted to the default admin account." });
    }

    if (!user.password) {
      return res.status(401).json({ message: "Login with Google" });
    }

    const isMatch = await user.comparePassword(password);

    if (!isMatch) {
      return res.status(401).json({ message: "Invalid credentials" });
    }

    // Set up standard OTP
    const otp = Math.floor(1000 + Math.random() * 9000).toString();
    otps.set(user.email, { otp, timestamp: Date.now() });
    console.log(`[OTP] Sent ${otp} to ${user.email} (simulated)`);

    // Send real email with OTP asynchronously
    if (user.email) {
      const subject = "Khedut Bandhu - OTP Verification";
      const html = `
        <div style="font-family: Arial, sans-serif; padding: 20px; border: 1px solid #eee; border-radius: 10px; max-width: 500px; margin: auto;">
          <h2 style="color: #4CAF50; text-align: center;">Khedut Bandhu</h2>
          <hr/>
          <p>Hello <strong>${user.username}</strong>,</p>
          <p>Your one-time password (OTP) for logging into your account is:</p>
          <div style="background: #f9f9f9; padding: 15px; text-align: center; border-radius: 5px; font-size: 24px; font-weight: bold; letter-spacing: 5px; color: #333;">
            ${otp}
          </div>
          <p style="font-size: 12px; color: #666; margin-top: 20px;">This OTP is valid for 5 minutes. Please do not share this code with anyone.</p>
        </div>
      `;
      sendEmail(user.email, subject, html).catch(err => console.error("Failed to send login OTP email:", err));
    }

    const token = jwt.sign({ id: user._id }, process.env.JWT_SECRET || "secret_key");

    res.json({
      message: "Login successful",
      userId: user._id,
      token: token,
      user: {
        id: user._id,
        username: user.username,
        email: user.email,
        role: user.role,
        phone: user.phone
      }
    });
  } catch (err) {
    console.error("Login error:", err);
    res.status(500).json({ message: "Server error" });
  }
});

// GOOGLE AUTH
router.get("/google", passport.authenticate("google", { scope: ["profile", "email"] }));

router.get("/google/callback",
  passport.authenticate("google", { failureRedirect: "/farmerlogin.html" }),
  (req, res) => {
    res.redirect("/farmerlogin.html?success=google_login");
  }
);

// OTP STORAGE (Temporary, use Redis/DB for production)
const otps = new Map();

// SEND OTP
router.post("/send-otp", async (req, res) => {
    try {
        const { email, phone, type } = req.body;
        const target = type === "sms" ? phone : email;

        if (!target) return res.status(400).json({ message: "Target required" });

        // Cooldown check
        const lastSent = otps.get(target);
        if (lastSent && Date.now() - lastSent.timestamp < 60000) {
            return res.status(429).json({ message: "Wait 60s before resending" });
        }

        const otp = Math.floor(1000 + Math.random() * 9000).toString();
        otps.set(target, { otp, timestamp: Date.now() });

        console.log(`[OTP] Sent ${otp} to ${target} via ${type}`); // Simulated
        
        // In real app, call Twilio for SMS or Nodemailer for Email here
        
        res.json({ message: `OTP sent to ${type === 'sms' ? 'phone' : 'email'}`, expires: "5 mins" });
    } catch (err) {
        res.status(500).json({ message: "Failed to send OTP" });
    }
});

// VERIFY OTP & LOGIN/SIGNUP
router.post("/verify-otp", async (req, res) => {
    try {
        const { target, otp, role, username, email, phone, userId } = req.body;
        
        let userEmail = target || email;
        let user = null;

        if (userId) {
            user = await User.findById(userId);
            if (user) {
                userEmail = user.email;
            }
        }

        const isBypass = (userEmail === "princepadaliya31@gmail.com" && otp === "1234");
        const stored = otps.get(userEmail || target);

        if (!isBypass) {
            if (!stored || stored.otp !== otp) {
                return res.status(401).json({ message: "Invalid or expired OTP" });
            }

            if (Date.now() - stored.timestamp > 300000) {
                otps.delete(userEmail || target);
                return res.status(401).json({ message: "OTP expired" });
            }

            otps.delete(userEmail || target);
        } else {
            // Clean up admin stored OTP if exists
            otps.delete("princepadaliya31@gmail.com");
        }

        // Find or create user
        if (!user) {
            const lookupEmail = (userEmail || target || "").toLowerCase();
            user = await User.findOne({ $or: [{ email: lookupEmail }, { email: (target || "").toLowerCase() }, { phone: target }, { phone }] });
            if (!user) {
                if (username && role) {
                    if (role === "admin" || role === "dept_admin") {
                        return res.status(403).json({ message: "Registration of administrative roles is not allowed." });
                    }
                    user = new User({ username, email: email || userEmail || "", phone: phone || target || "", role });
                    await user.save();
                } else {
                    return res.status(404).json({ message: "User not found. Please sign up." });
                }
            }
        }

        // Double check admin restriction
        if ((user.role === "admin" || user.role === "dept_admin") && user.email !== "princepadaliya31@gmail.com") {
            return res.status(403).json({ message: "Admin access is restricted to the default admin account." });
        }

        const token = jwt.sign({ id: user._id }, process.env.JWT_SECRET || "secret_key");

        res.json({
            message: "Verified successfully",
            token,
            user: { id: user._id, username: user.username, email: user.email, role: user.role, phone: user.phone }
        });
    } catch (err) {
        res.status(500).json({ message: "Verification failed" });
    }
});

// FORGOT PASSWORD - Send OTP
router.post("/forgot-password", async (req, res) => {
  try {
    const { username } = req.body;
    if (!username) {
      return res.status(400).json({ message: "Username or Email is required" });
    }

    const user = await User.findOne({
      $or: [{ username }, { email: username.toLowerCase() }]
    });

    if (!user) {
      return res.status(404).json({ message: "User not found with this username or email" });
    }

    // Check if user has an email
    if (!user.email) {
      return res.status(400).json({ message: "User does not have a registered email address" });
    }

    // Generate 4-digit OTP
    const otp = Math.floor(1000 + Math.random() * 9000).toString();
    otps.set(user.email, { otp, timestamp: Date.now() });
    console.log(`[Forgot Password OTP] Sent ${otp} to ${user.email} (simulated)`);

    // Send real email with OTP
    const subject = "Khedut Bandhu - Password Reset OTP";
    const html = `
      <div style="font-family: Arial, sans-serif; padding: 20px; border: 1px solid #eee; border-radius: 10px; max-width: 500px; margin: auto;">
        <h2 style="color: #4CAF50; text-align: center;">Khedut Bandhu</h2>
        <h3 style="text-align: center; color: #333;">Password Reset Verification</h3>
        <hr/>
        <p>Hello <strong>${user.username}</strong>,</p>
        <p>We received a request to reset your password. Use the following 4-digit OTP code to verify your identity and reset your password:</p>
        <div style="background: #f9f9f9; padding: 15px; text-align: center; border-radius: 5px; font-size: 24px; font-weight: bold; letter-spacing: 5px; color: #d9534f;">
          ${otp}
        </div>
        <p style="font-size: 12px; color: #666; margin-top: 20px;">This OTP is valid for 5 minutes. If you did not request this, please secure your account immediately.</p>
      </div>
    `;

    // Send email asynchronously (non-blocking)
    sendEmail(user.email, subject, html).catch(err => console.error("Forgot password email failed:", err));

    res.json({ message: "Reset OTP sent to your email", userId: user._id });
  } catch (err) {
    console.error("Forgot password error:", err);
    res.status(500).json({ message: "Failed to send reset OTP. Check your connection/SMTP config." });
  }
});

// RESET PASSWORD - Verify OTP & Save New Password
router.post("/reset-password", async (req, res) => {
  try {
    const { userId, otp, newPassword } = req.body;
    if (!userId || !otp || !newPassword) {
      return res.status(400).json({ message: "All fields are required" });
    }

    const user = await User.findById(userId);
    if (!user) {
      return res.status(404).json({ message: "User not found" });
    }

    const isBypass = (user.email === "princepadaliya31@gmail.com" && otp === "1234");
    const stored = otps.get(user.email);

    if (!isBypass) {
      if (!stored || stored.otp !== otp) {
        return res.status(401).json({ message: "Invalid or expired OTP" });
      }

      if (Date.now() - stored.timestamp > 300000) {
        otps.delete(user.email);
        return res.status(401).json({ message: "OTP expired" });
      }

      otps.delete(user.email);
    } else {
      otps.delete("princepadaliya31@gmail.com");
    }

    // Save the new password (will trigger the pre-save bcrypt hash)
    user.password = newPassword;
    await user.save();

    res.json({ message: "Password reset successful. Please login with your new password." });
  } catch (err) {
    console.error("Reset password error:", err);
    res.status(500).json({ message: "Failed to reset password. Server error." });
  }
});

module.exports = router;

