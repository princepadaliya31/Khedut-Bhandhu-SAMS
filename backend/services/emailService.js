const nodemailer = require("nodemailer");
require("dotenv").config();

const sendEmail = async (to, subject, html) => {
    // 1. If Brevo HTTP API Key is configured, use the HTTP API (works perfectly on Render Free tier!)
    if (process.env.BREVO_API_KEY) {
        try {
            const response = await fetch("https://api.brevo.com/v3/smtp/email", {
                method: "POST",
                headers: {
                    "accept": "application/json",
                    "api-key": process.env.BREVO_API_KEY,
                    "content-type": "application/json"
                },
                body: JSON.stringify({
                    sender: { name: "Khedut Bandhu", email: process.env.EMAIL_USER || "princepadaliya05@gmail.com" },
                    to: [{ email: to }],
                    subject: subject,
                    htmlContent: html
                })
            });
            const data = await response.json();
            if (response.ok) {
                console.log(`📧 Email sent to ${to} via Brevo HTTP API`);
                return;
            } else {
                console.error("❌ Brevo API Error:", data);
            }
        } catch (error) {
            console.error("❌ Brevo HTTP request failed:", error);
        }
    }

    // 2. Fallback to Gmail SMTP (Blocked on Render Free tier, but works locally or on Render Paid tiers)
    try {
        const transporter = nodemailer.createTransport({
            host: "smtp.gmail.com",
            port: 587,
            secure: false,
            auth: {
                user: process.env.EMAIL_USER,
                pass: process.env.EMAIL_PASS,
            },
            tls: { rejectUnauthorized: false },
        });

        await transporter.sendMail({
            from: process.env.EMAIL_USER,
            to,
            subject,
            html,
        });
        console.log(`📧 Email sent to ${to} via SMTP`);
    } catch (error) {
        console.error("❌ SMTP Email sending failed:", error);
    }
};

module.exports = sendEmail;
