# 🌿 Khedut Bandhu (Farmer's Friend)
### Smart Agriculture Management System & AI Crop Diagnostics Portal

Khedut Bandhu is a production-ready, full-stack monorepo designed to empower local farmers by providing direct peer-to-peer crop sales, real-time APMC market price analysis, localized smart weather forecasting, logistics management, and an AI-powered Crop Leaf Disease Diagnostic engine. 

---

## 📌 Table of Contents
* [About The Project](#about-the-project)
* [Features](#features)
* [System Architecture](#system-architecture)
* [Tech Stack](#tech-stack)
* [Project Structure](#project-structure)
* [Getting Started](#getting-started)
* [Environment Variables](#environment-variables)
* [API Documentation](#api-documentation)
* [Key Engineering Challenges Faced](#key-engineering-challenges-faced)
* [Key Learnings](#key-learnings)
* [Future Enhancements](#future-enhancements)
* [License](#license)
* [Author](#author)

---

## 📖 About The Project

### Problem it Solves
Smallholder farmers face critical challenges: lack of transparent APMC market prices, middleman exploitation during crop sales, slow response times from local grievance departments, and devastating crop yield losses due to plant diseases that go undiagnosed.

### The Solution
Khedut Bandhu unifies a secure multi-role portal where:
1. **Farmers** can run instant AI diagnostics on plant leaves, check current APMC market prices, sell crops directly, book transportation, and track subsidies.
2. **Buyers** can browse listings and buy directly from farmers with secure online payment integration.
3. **Admins/Department Leads** can monitor complaints, track regional resolutions, and analyze platform telemetry.

---

## ✨ Features

### Farmer Features
* **🤖 AI Crop Diagnostics**: Upload leaf photos to detect plant diseases (smut, rust, blast, tikka) instantly with expert prevention and treatment recommendations.
* **🌾 Peer-to-Peer Marketplace**: Direct crop listings for sale, bypassing intermediaries.
* **📈 APMC Price Ticker**: Live marquee ticker tracking commodity prices in local markets.
* **🌦️ Smart Weather Widget**: Geo-location based weather widget offering localized agricultural advisories.
* **🚛 Logistics Booking**: Select regional transport companies and book trucks directly for harvest transport.
* **🏛️ Welfare Schemes**: Track and apply for active state/central government agricultural subsidies.

### Buyer Features
* **🛒 Secure Purchasing**: Browse farm-fresh crop listings and buy directly using **Razorpay Payment Gateway**.
* **🧾 Invoice Generation**: View, track order history, and download PDF invoices for auditing.

### Admin & Department Features
* **📊 Analytics Dashboard**: Charts showing complaint resolution rates, regional user statistics, and P2P sales performance.
* **🛡️ Grievance Routing**: Actionable complaint board with automated role-based routing (e.g., Complaint Dept, Supreme Admin).

### Security & Localization
* **🔑 Role-based Access Control (RBAC)**: Custom panels for `Farmer`, `Buyer`, `Admin`, and `Dept Admin`.
* **🔒 API Security**: JWT-based authorization, rate limiting, and input sanitization (Helmet, Mongo-Sanitize).
* **🌐 Tri-lingual Interface**: Localized translation system supporting **Gujarati, Hindi, and English** via `i18next`.

---

## 🏗️ System Architecture

```text
       ┌────────────────────────┐
       │   React SPA (Client)   │ (i18n Translation, Localized Weather)
       └───────────┬────────────┘
                   │
         HTTPS / JSON (Port 5000)
                   │
       ┌───────────▼────────────┐
       │   Node.js/Express API  │ (Routing, Multer upload, Mongoose Schema)
       └─────┬───────────┬──────┘
             │           │
   MongoDB (Atlas)    REST / MultiPart (Port 8005)
             │           │
   ┌─────────▼─┐   ┌─────▼────────────────────┐
   │ Database  │   │ FastAPI AI Service       │ (EfficientNetB3 CNN,
   └───────────┘   │ (Python TensorFlow Venv) │  CLAHE Preprocessing)
                   └──────────────────────────┘
```

---

## 🛠️ Tech Stack

* **Frontend**: React.js (v18), React Router Dom (v6), i18next (Localization), Vanilla CSS (Custom Glassmorphism & Dark Green Theme).
* **Backend**: Node.js, Express, JWT, Multer (file handling), Nodemailer (secure SMTP OTP logins).
* **AI Engine**: Python, FastAPI, TensorFlow 2.x, OpenCV (CLAHE preprocessing), NumPy, Pillow.
* **Database**: MongoDB (Mongoose ODM).
* **Payment Gateway**: Razorpay Checkout SDK.

---

## 📂 Project Structure

```text
Khedut-Bhandhu/
├── frontend/                     # React Client App (Port 3000)
│   ├── public/                   # Static Assets (favicon.svg, index.html)
│   └── src/
│       ├── components/           # Dashboard views, CropDiagnostics, Navbar, etc.
│       ├── App.js                # Routing & Dynamic document title logic
│       ├── App.css               # Premium layout & responsive styles
│       └── i18n.js               # Translation dictionaries (EN, HI, GU)
├── backend/                      # Node.js Express REST API (Port 5000)
│   ├── models/                   # Mongoose Schemas (User, DiseaseCase, Complaint)
│   ├── routes/                   # Endpoint routers (auth, user, market, schemes)
│   ├── middleware/               # Token validators & Route guards
│   └── server.js                 # App configuration & FastAPI API proxies
├── ai-service/                   # Python FastAPI AI Inference (Port 8005)
│   ├── main.py                   # Model Loader, CLAHE preprocess, and classification
│   └── requirements.txt          # Python ML dependencies (TensorFlow, Pillow, FastAPI)
├── start_khedut_professional.bat # Combined multi-service launcher script
├── .gitignore                    # Excludes node_modules, .env, and large .h5 ML models
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites
* Node.js (v18 or higher)
* Python 3.10 to 3.12 (with `python.exe` added to PATH)
* MongoDB (Atlas URL or Local instance)

### Installation & Launch

You can start the entire project (AI service, Node Backend, and React Frontend) with a single click using the launcher file in the root folder:

1. Double-click the **`start_khedut_professional.bat`** file in your file explorer.
2. This will automatically open separate terminal windows and run all three servers simultaneously!

* **React Frontend**: `http://localhost:3000`
* **Node Backend**: `http://localhost:5000`
* **AI Service**: `http://localhost:8005`

---

## 🔑 Environment Variables

Create a `.env` file in the `/backend` folder:

```env
PORT=5000
MONGO_URI=mongodb+srv://your_username:your_password@cluster.mongodb.net/khedut
JWT_SECRET=your_jwt_secret_key
EMAIL_USER=your_email@gmail.com
EMAIL_PASS=your_app_password
```

Create a `.env` file in the `/frontend` folder:

```env
REACT_APP_API_URL=http://localhost:5000
```

---

## 📡 API Documentation

### Authentication & Authorization
| Method | Endpoint | Description | Auth Required |
|:---|:---|:---|:---|
| **POST** | `/api/auth/signup` | Registers a new user | No |
| **POST** | `/api/auth/login` | Log in user (Sends OTP via secure SMTP) | No |
| **POST** | `/api/auth/verify-otp` | Verifies login OTP code (Bypass option: 1234) | No |
| **POST** | `/api/auth/forgot-password`| Sends a password-reset OTP code | No |
| **POST** | `/api/auth/reset-password` | Verifies reset OTP & saves new password | No |

### AI Crop Diagnostics
| Method | Endpoint | Description | Auth Required |
|:---|:---|:---|:---|
| **GET** | `/api/ai/health` | Checks if AI service & TensorFlow model are loaded | No |
| **POST**| `/api/ai/predict` | Uploads leaf photo to return class details & recommendations | No |

---

## 🚧 Key Engineering Challenges Faced

### 1. Windows Shell Unicode Encoding Crashes in Python logs
* **Challenge**: When running `main.py` inside standard Windows CMD or PowerShell terminals, the system crashed during initialization with a `UnicodeEncodeError`. The default console encoding (cp1252) could not parse the emoji characters (`✅`, `❌`, `⚠️`) printed by Python.
* **Solution**: Cleaned and refactored the Python server print commands to use standard ASCII-safe prefixes (`[OK]`, `[ERROR]`, `[WARN]`), preventing shell crashes and ensuring smooth application startup on Windows.

### 2. State Confusion inside Authentication Forms
* **Challenge**: The frontend Login and Forgot Password forms originally shared the same state variables for the user account identifier. If an admin user typed `admin`, clicking "Forgot Password" prefilled the form with the admin credentials, routing the reset email incorrectly to the admin's database email.
* **Solution**: Separated the state bindings in React (`forgotEmail` vs `username`), removing form overlap and ensuring OTPs are sent strictly to the email entered during the reset request.

### 3. Asynchronous Node Proxying for Multipart AI Payloads
* **Challenge**: The React frontend sent crop diagnostics requests directly to the Node backend. Express needed to pipe these multipart uploads to the Python service. The initial proxy was crashing due to missing npm packages (`node-fetch` and `form-data`).
* **Solution**: Upgraded the Express routes (`server.js`) to use Node's native **`fetch`**, **`FormData`**, and **`Blob`** APIs (built-in in Node 18+). This eliminated third-party package dependencies and enabled native binary file stream forwarding to FastAPI.

---

## 📚 Key Learnings
* **Microservice Orchestration**: Designing a unified backend proxy pattern that handles file streaming between Node.js and Python servers.
* **Robust Multi-Language Config**: Structuring dictionary resources dynamically across dashboards without causing layout shifts.
* **Securing Enterprise REST APIs**: Practical execution of password hashing, secure SMTP bindings, rate limiting, and role-based route guard structures.

---

## 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

---

## 👨‍💻 Author
**Prince Padaliya**
* [GitHub](https://github.com/princepadaliya31)
* [LinkedIn](https://linkedin.com/in/princepadaliya)
* Email: princepadaliya31@gmail.com
