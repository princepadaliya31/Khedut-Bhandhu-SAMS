html = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Khedut Bandhu – System Architecture</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&display=swap" rel="stylesheet">
<style>
*{box-sizing:border-box;margin:0;padding:0;}
body{font-family:'Inter',sans-serif;background:#fff;padding:32px;min-width:2500px;}
h1{text-align:center;font-size:30px;font-weight:900;color:#0d1b2a;margin-bottom:4px;}
.sub{text-align:center;font-size:14px;color:#666;margin-bottom:28px;}
/* TOP BAND */
.top-band{display:flex;gap:16px;align-items:stretch;margin-bottom:20px;}
.col{flex:1;display:flex;flex-direction:column;gap:10px;}
.col-header{border-radius:10px 10px 0 0;padding:12px 14px;color:#fff;font-weight:800;font-size:13px;}
.col-sub{font-size:11px;font-weight:500;opacity:.85;margin-top:2px;}
.col-body{background:#F7F9FC;border:1.5px solid #E0E7EF;border-radius:0 0 12px 12px;padding:14px;flex:1;}
/* role boxes */
.role-box{background:#fff;border-radius:8px;padding:10px 12px;margin-bottom:10px;border:1.5px solid #E8EEF5;box-shadow:0 2px 8px rgba(0,0,0,.05);}
.role-title{font-size:12px;font-weight:800;margin-bottom:6px;}
.role-box ul{list-style:none;padding:0;}
.role-box ul li{font-size:10.5px;color:#555;padding:2px 0 2px 12px;position:relative;}
.role-box ul li::before{content:"›";position:absolute;left:2px;color:#aaa;font-weight:700;}
/* backend layers */
.layer{background:#fff;border-radius:8px;padding:10px 12px;margin-bottom:8px;border-left:4px solid #1565C0;box-shadow:0 2px 6px rgba(0,0,0,.04);}
.layer-title{font-size:11.5px;font-weight:800;color:#1565C0;margin-bottom:5px;}
.layer ul{list-style:none;display:flex;flex-wrap:wrap;gap:4px;}
.layer ul li{font-size:10px;color:#444;background:#EEF3FA;padding:2px 8px;border-radius:20px;}
/* db rows */
.db-row{background:#fff;border-radius:7px;padding:8px 11px;margin-bottom:7px;border:1.5px solid #E0E7EF;font-size:10.5px;}
.db-name{font-weight:800;color:#0d47a1;margin-bottom:3px;}
.db-fields{color:#666;font-size:10px;}
/* ext services */
.ext-box{border-radius:10px;padding:12px 14px;margin-bottom:10px;}
.ext-title{font-size:12px;font-weight:800;margin-bottom:6px;}
.ext-box ul{list-style:none;}
.ext-box ul li{font-size:10.5px;padding:2px 0 2px 12px;position:relative;}
.ext-box ul li::before{content:"✦";position:absolute;left:1px;font-size:9px;}
/* infra */
.infra-box{border-radius:10px;padding:12px 14px;margin-bottom:10px;background:#fff;border:1.5px solid #E0E7EF;box-shadow:0 2px 8px rgba(0,0,0,.05);}
.infra-icon{font-size:24px;margin-bottom:6px;}
.infra-title{font-size:12px;font-weight:800;margin-bottom:5px;}
.infra-box ul{list-style:none;}
.infra-box ul li{font-size:10.5px;color:#555;padding:2px 0 2px 12px;position:relative;}
.infra-box ul li::before{content:"›";position:absolute;left:2px;color:#aaa;}
/* arrow */
.arrow-wrap{display:flex;flex-direction:column;align-items:center;justify-content:center;width:54px;flex-shrink:0;}
.arrow-line{display:flex;flex-direction:column;align-items:center;gap:4px;}
.arrow-svg{font-size:28px;color:#64748b;}
.arrow-label{font-size:9px;font-weight:700;color:#64748b;text-align:center;background:#E0E7EF;padding:3px 7px;border-radius:20px;white-space:nowrap;}
/* TECH BAR */
.tech-bar{background:#F1F5F9;border-radius:12px;padding:16px 28px;display:flex;align-items:center;gap:0;margin-bottom:20px;border:1.5px solid #E0E7EF;}
.tech-label{font-size:13px;font-weight:900;color:#0d1b2a;margin-right:28px;white-space:nowrap;}
.tech-items{display:flex;gap:14px;flex-wrap:wrap;flex:1;}
.tech-chip{display:flex;align-items:center;gap:6px;background:#fff;border-radius:20px;padding:6px 14px;font-size:11px;font-weight:700;border:1.5px solid #E0E7EF;box-shadow:0 1px 4px rgba(0,0,0,.05);}
.chip-dot{width:10px;height:10px;border-radius:50%;flex-shrink:0;}
/* BOTTOM BAND */
.bottom-band{display:grid;grid-template-columns:1fr 1fr 1fr;gap:20px;}
.bot-panel{border-radius:14px;overflow:hidden;box-shadow:0 4px 20px rgba(0,0,0,.07);}
.bot-header{padding:13px 20px;font-size:14px;font-weight:800;color:#fff;}
.bot-body{padding:18px 20px;}
/* key points */
.kp-item{display:flex;align-items:flex-start;gap:10px;padding:9px 0;border-bottom:1px solid #F0F4F8;font-size:12px;color:#333;}
.kp-item:last-child{border-bottom:none;}
.kp-icon{font-size:16px;flex-shrink:0;}
/* flow */
.flow-row{display:flex;align-items:center;justify-content:center;gap:0;flex-wrap:nowrap;}
.flow-box{border-radius:10px;padding:12px 16px;text-align:center;min-width:120px;}
.flow-icon{font-size:22px;margin-bottom:4px;}
.flow-name{font-size:11px;font-weight:800;}
.flow-arrow{font-size:24px;color:#64748b;padding:0 6px;}
/* roles */
.role-row{display:flex;align-items:flex-start;gap:12px;padding:10px 0;border-bottom:1px solid #F0F4F8;}
.role-row:last-child{border-bottom:none;}
.role-ico{font-size:22px;flex-shrink:0;}
.role-info-name{font-size:12px;font-weight:800;margin-bottom:2px;}
.role-info-desc{font-size:11px;color:#555;line-height:1.4;}
</style>
</head>
<body>
<h1>🌾 Khedut Bandhu – System Architecture (High Level)</h1>
<div class="sub">Comprehensive End-to-End Architecture &nbsp;|&nbsp; MERN Stack + AI Microservice &nbsp;|&nbsp; Agricultural Digital Platform</div>

<!-- TOP BAND -->
<div class="top-band">

<!-- COL 1: CLIENTS -->
<div class="col">
<div class="col-header" style="background:#1565C0;">
  <div>CLIENTS / FRONTEND</div>
  <div class="col-sub">React.js (Create React App) · Web Browser</div>
</div>
<div class="col-body">
  <div style="text-align:center;font-size:38px;margin-bottom:12px;">💻📱</div>
  <div class="role-box">
    <div class="role-title" style="color:#1565C0;">👨‍🌾 Farmer</div>
    <ul>
      <li>Register / Login via OTP or Google</li>
      <li>Browse &amp; buy seeds, pesticides, tools</li>
      <li>Upload crop photo for AI diagnosis</li>
      <li>View live APMC market prices</li>
      <li>Track orders &amp; subsidy applications</li>
    </ul>
  </div>
  <div class="role-box">
    <div class="role-title" style="color:#2E7D32;">🛍️ Buyer</div>
    <ul>
      <li>Google OAuth or OTP login</li>
      <li>Browse agricultural products</li>
      <li>Add to cart &amp; checkout</li>
      <li>Track delivery status</li>
    </ul>
  </div>
  <div class="role-box">
    <div class="role-title" style="color:#6A1B9A;">🛡️ Admin / Dept-Admin</div>
    <ul>
      <li>Manage products, orders, rates</li>
      <li>Approve subsidy applications</li>
      <li>Resolve farmer complaints</li>
      <li>View audit logs &amp; analytics</li>
    </ul>
  </div>
</div>
</div>

<!-- ARROW 1→2 -->
<div class="arrow-wrap">
  <div class="arrow-line">
    <span class="arrow-svg">⇄</span>
    <span class="arrow-label">HTTPS<br>REST API</span>
  </div>
</div>

<!-- COL 2: BACKEND -->
<div class="col">
<div class="col-header" style="background:#0d47a1;">
  <div>BACKEND</div>
  <div class="col-sub">Node.js + Express.js · Port 5000</div>
</div>
<div class="col-body">
  <div class="layer">
    <div class="layer-title">🌐 API Gateway / Controller Layer</div>
    <ul><li>REST Controllers</li><li>Request Validation</li><li>Exception Handling</li><li>Rate Limiting (100 req/15 min)</li><li>CORS + Helmet Security</li></ul>
  </div>
  <div class="layer" style="border-left-color:#1976D2;">
    <div class="layer-title" style="color:#1976D2;">⚙️ Service Layer</div>
    <ul><li>Auth Service (OTP/JWT)</li><li>Product Service</li><li>Order Service</li><li>Market Rate Service</li><li>AI Proxy Service</li><li>Email Service</li></ul>
  </div>
  <div class="layer" style="border-left-color:#0288D1;">
    <div class="layer-title" style="color:#0288D1;">🧩 Business Logic Layer</div>
    <ul><li>Cart &amp; Checkout Logic</li><li>Cancellation Fee Calc</li><li>Luhn Card Validation</li><li>OTP Expiry Checks</li><li>Delivery Charge Rules</li></ul>
  </div>
  <div class="layer" style="border-left-color:#C62828;">
    <div class="layer-title" style="color:#C62828;">🔐 Security Layer</div>
    <ul><li>JWT Authentication</li><li>Role-Based Authorization</li><li>bcrypt Password Hashing</li><li>Mongo Sanitize</li></ul>
  </div>
  <div class="layer" style="border-left-color:#558B2F;">
    <div class="layer-title" style="color:#558B2F;">🛠️ Utility Layer</div>
    <ul><li>Multer File Upload</li><li>Nodemailer Email</li><li>Passport Google OAuth</li><li>FormData AI Proxy</li></ul>
  </div>
</div>
</div>

<!-- ARROW 2→3 -->
<div class="arrow-wrap">
  <div class="arrow-line">
    <span class="arrow-svg">⇄</span>
    <span class="arrow-label">Mongoose<br>ODM</span>
  </div>
</div>

<!-- COL 3: DATA LAYER -->
<div class="col">
<div class="col-header" style="background:#1b5e20;">
  <div>DATA LAYER</div>
  <div class="col-sub">MongoDB Atlas / Local · Mongoose ODM</div>
</div>
<div class="col-body">
  <div style="text-align:center;font-size:32px;margin-bottom:12px;">🍃</div>
  <div class="db-row"><div class="db-name">📋 users</div><div class="db-fields">_id, username, email, phone, role, password, googleId, cart[], orders[], complaints[], subsidies[], landDetails, bankDetails, location</div></div>
  <div class="db-row"><div class="db-name">📦 products</div><div class="db-fields">_id, name, category, price, stock, imageUrl, type, usedFor[], crops[], usageSteps[], safetyInstructions[], reviews[], averageRating</div></div>
  <div class="db-row"><div class="db-name">🌾 marketrates</div><div class="db-fields">_id, cropName, rate, previousRate, state, region, marketName, date, timestamps</div></div>
  <div class="db-row"><div class="db-name">🤖 diseasecases</div><div class="db-fields">_id, userId, cropName, imageUrl, diagnosedDisease, confidence, userFeedback, metadata, isTrainingReady</div></div>
  <div class="db-row"><div class="db-name">🔑 otps</div><div class="db-fields">_id, userId, otp, expiresAt</div></div>
  <div class="db-row"><div class="db-name">🏛️ schemes</div><div class="db-fields">_id, schemeName, description, eligibility, formLink, status</div></div>
  <div class="db-row"><div class="db-name">📝 feedbacks</div><div class="db-fields">_id, userId, message, rating, createdAt</div></div>
  <div class="db-row"><div class="db-name">🔍 auditlogs</div><div class="db-fields">_id, adminId, action, targetId, details, timestamp</div></div>
</div>
</div>

<!-- ARROW 3→4 -->
<div class="arrow-wrap">
  <div class="arrow-line">
    <span class="arrow-svg">→</span>
    <span class="arrow-label">API<br>Calls</span>
  </div>
</div>

<!-- COL 4: EXTERNAL SERVICES -->
<div class="col">
<div class="col-header" style="background:#4527A0;">
  <div>EXTERNAL SERVICES</div>
  <div class="col-sub">Third-Party APIs &amp; Integrations</div>
</div>
<div class="col-body">
  <div class="ext-box" style="background:#E8F5E9;border:1.5px solid #A5D6A7;">
    <div class="ext-title" style="color:#2E7D32;">🔑 Google OAuth 2.0</div>
    <ul style="color:#2E7D32;">
      <li>Social login for Farmers &amp; Buyers</li>
      <li>Profile data (name, email, avatar)</li>
      <li>Passport.js strategy integration</li>
    </ul>
  </div>
  <div class="ext-box" style="background:#FFF8E1;border:1.5px solid #FFE082;">
    <div class="ext-title" style="color:#E65100;">📧 Gmail SMTP (Nodemailer)</div>
    <ul style="color:#E65100;">
      <li>OTP delivery emails</li>
      <li>Order confirmation &amp; invoice</li>
      <li>Refund QR code emails</li>
      <li>Aadhaar verification OTP</li>
    </ul>
  </div>
  <div class="ext-box" style="background:#E3F2FD;border:1.5px solid #90CAF9;">
    <div class="ext-title" style="color:#1565C0;">🪪 Digio Aadhaar KYC API</div>
    <ul style="color:#1565C0;">
      <li>Offline Aadhaar KYC sessions</li>
      <li>Farmer identity verification</li>
      <li>Simulation fallback mode</li>
    </ul>
  </div>
  <div class="ext-box" style="background:#F3E5F5;border:1.5px solid #CE93D8;">
    <div class="ext-title" style="color:#6A1B9A;">💳 Razorpay Payment Gateway</div>
    <ul style="color:#6A1B9A;">
      <li>Create &amp; verify payment orders</li>
      <li>Card &amp; Netbanking processing</li>
      <li>PCI-DSS compliant encryption</li>
    </ul>
  </div>
  <div class="ext-box" style="background:#E8EAF6;border:1.5px solid #9FA8DA;">
    <div class="ext-title" style="color:#283593;">📊 QR Server API</div>
    <ul style="color:#283593;">
      <li>UPI payment QR generation</li>
      <li>Refund QR code generation</li>
      <li>Dynamic amount encoding</li>
    </ul>
  </div>
</div>
</div>

<!-- ARROW 4→5 -->
<div class="arrow-wrap">
  <div class="arrow-line">
    <span class="arrow-svg">→</span>
    <span class="arrow-label">HTTP<br>Proxy</span>
  </div>
</div>

<!-- COL 5: INFRASTRUCTURE -->
<div class="col">
<div class="col-header" style="background:#37474F;">
  <div>INFRASTRUCTURE &amp; AI</div>
  <div class="col-sub">Deployment · AI Service · Monitoring</div>
</div>
<div class="col-body">
  <div class="infra-box" style="border-top:3px solid #7B1FA2;">
    <div class="infra-icon">🧠</div>
    <div class="infra-title" style="color:#7B1FA2;">Python FastAPI – AI Microservice</div>
    <ul>
      <li>Port 8005 — independent service</li>
      <li>TensorFlow/Keras CNN model</li>
      <li>PlantVillage dataset (38 classes)</li>
      <li>/predict &amp; /health endpoints</li>
      <li>Model file: best_phase1.h5</li>
    </ul>
  </div>
  <div class="infra-box" style="border-top:3px solid #1565C0;">
    <div class="infra-icon">🚀</div>
    <div class="infra-title" style="color:#1565C0;">Node.js Process Manager</div>
    <ul>
      <li>Start All via .bat launcher scripts</li>
      <li>start_all.bat orchestrates services</li>
      <li>Environment via .env config</li>
      <li>Async MongoDB reconnect on fail</li>
    </ul>
  </div>
  <div class="infra-box" style="border-top:3px solid #2E7D32;">
    <div class="infra-icon">📁</div>
    <div class="infra-title" style="color:#2E7D32;">File &amp; Static Asset Serving</div>
    <ul>
      <li>Multer: crop image uploads</li>
      <li>Stored in /upload/training_data</li>
      <li>Express static file serving</li>
      <li>Image used for AI + case record</li>
    </ul>
  </div>
  <div class="infra-box" style="border-top:3px solid #E65100;">
    <div class="infra-icon">📊</div>
    <div class="infra-title" style="color:#E65100;">Logging &amp; Monitoring</div>
    <ul>
      <li>Console request logging middleware</li>
      <li>Server log files (server_log.txt)</li>
      <li>MongoDB connection error handling</li>
      <li>AI service offline fallback</li>
    </ul>
  </div>
</div>
</div>

</div><!-- end top-band -->

<!-- TECH STACK BAR -->
<div class="tech-bar">
  <div class="tech-label">⚙️ TECHNOLOGY STACK</div>
  <div class="tech-items">
    <div class="tech-chip"><div class="chip-dot" style="background:#61DAFB;"></div>React.js</div>
    <div class="tech-chip"><div class="chip-dot" style="background:#68A063;"></div>Node.js</div>
    <div class="tech-chip"><div class="chip-dot" style="background:#000;"></div>Express.js</div>
    <div class="tech-chip"><div class="chip-dot" style="background:#4DB33D;"></div>MongoDB</div>
    <div class="tech-chip"><div class="chip-dot" style="background:#FF6F00;"></div>TensorFlow</div>
    <div class="tech-chip"><div class="chip-dot" style="background:#009688;"></div>FastAPI (Python)</div>
    <div class="tech-chip"><div class="chip-dot" style="background:#4285F4;"></div>Google OAuth 2.0</div>
    <div class="tech-chip"><div class="chip-dot" style="background:#0284C7;"></div>Razorpay</div>
    <div class="tech-chip"><div class="chip-dot" style="background:#EA4335;"></div>Gmail SMTP</div>
    <div class="tech-chip"><div class="chip-dot" style="background:#7B1FA2;"></div>Digio KYC API</div>
    <div class="tech-chip"><div class="chip-dot" style="background:#F59E0B;"></div>JWT + Passport.js</div>
    <div class="tech-chip"><div class="chip-dot" style="background:#6366F1;"></div>bcrypt + Helmet</div>
  </div>
</div>

<!-- BOTTOM BAND -->
<div class="bottom-band">

<!-- KEY POINTS -->
<div class="bot-panel">
  <div class="bot-header" style="background:#1565C0;">✅ KEY POINTS</div>
  <div class="bot-body" style="background:#F7F9FC;">
    <div class="kp-item"><span class="kp-icon">🌾</span><span>Direct farmer-to-market platform — eliminates middlemen and ensures fair crop pricing via live APMC rates</span></div>
    <div class="kp-item"><span class="kp-icon">🤖</span><span>AI-powered CNN model detects crop diseases from leaf photos with confidence score and cure recommendation</span></div>
    <div class="kp-item"><span class="kp-icon">🔐</span><span>Multi-layer security: OTP login, JWT sessions (7d), Google OAuth, Aadhaar KYC, bcrypt password hashing</span></div>
    <div class="kp-item"><span class="kp-icon">💳</span><span>Full payment ecosystem: COD, UPI QR, Credit/Debit Card (Luhn validated), Netbanking via Razorpay</span></div>
    <div class="kp-item"><span class="kp-icon">🏛️</span><span>Government scheme tracker lets farmers apply for subsidies and track approval status end-to-end</span></div>
    <div class="kp-item"><span class="kp-icon">📦</span><span>Automated refund system: cancellations trigger UPI QR code refund emails with exact refund amount encoded</span></div>
  </div>
</div>

<!-- FLOW SUMMARY -->
<div class="bot-panel">
  <div class="bot-header" style="background:#2E7D32;">🔄 SYSTEM FLOW (Behind the Scenes)</div>
  <div class="bot-body" style="background:#F1F8F2;">
    <div class="flow-row" style="margin-bottom:18px;">
      <div class="flow-box" style="background:#E3F2FD;border:2px solid #90CAF9;">
        <div class="flow-icon">⚛️</div>
        <div class="flow-name" style="color:#1565C0;">React<br>Frontend</div>
      </div>
      <div class="flow-arrow">→</div>
      <div class="flow-box" style="background:#E8F5E9;border:2px solid #A5D6A7;">
        <div class="flow-icon">🟢</div>
        <div class="flow-name" style="color:#2E7D32;">Express<br>Backend</div>
      </div>
      <div class="flow-arrow">→</div>
      <div class="flow-box" style="background:#F3E5F5;border:2px solid #CE93D8;">
        <div class="flow-icon">🍃</div>
        <div class="flow-name" style="color:#6A1B9A;">MongoDB<br>Database</div>
      </div>
    </div>
    <div class="flow-row">
      <div class="flow-box" style="background:#FFF8E1;border:2px solid #FFE082;">
        <div class="flow-icon">🧠</div>
        <div class="flow-name" style="color:#E65100;">FastAPI<br>AI Service</div>
      </div>
      <div class="flow-arrow">→</div>
      <div class="flow-box" style="background:#E8EAF6;border:2px solid #9FA8DA;">
        <div class="flow-icon">📧</div>
        <div class="flow-name" style="color:#283593;">Gmail<br>SMTP</div>
      </div>
      <div class="flow-arrow">→</div>
      <div class="flow-box" style="background:#FCE4EC;border:2px solid #F48FB1;">
        <div class="flow-icon">💳</div>
        <div class="flow-name" style="color:#880E4F;">Razorpay<br>Gateway</div>
      </div>
    </div>
  </div>
</div>

<!-- ROLES INVOLVED -->
<div class="bot-panel">
  <div class="bot-header" style="background:#4527A0;">👥 ROLES INVOLVED</div>
  <div class="bot-body" style="background:#F5F3FF;">
    <div class="role-row">
      <div class="role-ico">👨‍🌾</div>
      <div>
        <div class="role-info-name" style="color:#1565C0;">Farmer</div>
        <div class="role-info-desc">Core user — registers land, shops for inputs, uploads crop photos for AI diagnosis, tracks market rates and subsidy applications.</div>
      </div>
    </div>
    <div class="role-row">
      <div class="role-ico">🛍️</div>
      <div>
        <div class="role-info-name" style="color:#2E7D32;">Buyer</div>
        <div class="role-info-desc">Purchases agricultural produce directly from the platform, manages cart, checkout, and order tracking.</div>
      </div>
    </div>
    <div class="role-row">
      <div class="role-ico">🛡️</div>
      <div>
        <div class="role-info-name" style="color:#6A1B9A;">Admin</div>
        <div class="role-info-desc">Superuser who manages all products, orders, market rates, schemes, complaints and views full audit trails.</div>
      </div>
    </div>
    <div class="role-row">
      <div class="role-ico">🏢</div>
      <div>
        <div class="role-info-name" style="color:#E65100;">Dept Admin</div>
        <div class="role-info-desc">Department-specific admin (Pesticide, Seed, Subsidy, MarketPrice, Orders, Help) with scoped access to their domain.</div>
      </div>
    </div>
  </div>
</div>

</div><!-- end bottom-band -->
</body>
</html>'''

with open('khedut_architecture.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Generated: khedut_architecture.html")
