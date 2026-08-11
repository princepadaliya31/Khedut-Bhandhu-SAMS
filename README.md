# 🌿 Khedut Bandhu (Farmer's Friend)
### Smart Agriculture Management System & AI Crop Diagnostics Portal

Khedut Bandhu is a production-ready, full-stack monorepo designed to empower local farmers by providing direct peer-to-peer crop sales, real-time APMC market price analysis, localized smart weather forecasting, logistics management, and an AI-powered Crop Leaf Disease Diagnostic engine.

🚀 **Live Demo**: [khedut-bhandhu-sams-j6bx.vercel.app](https://khedut-bhandhu-sams-j6bx.vercel.app/)

🌐 **Deployment Hosting**:
* **Frontend**: Vercel
* **Backend**: Render
* **AI Service**: Hugging Face Spaces (or Render Paid Starter)
* **Database**: MongoDB Atlas
* **Email Service**: Brevo HTTP API

---

## 📌 Table of Contents
* [🌟 Key Features](#-key-features)
* [🤖 AI Diagnostics Engine](#-ai-diagnostics-engine)
* [🏗️ System Architecture](#-system-architecture)
* [🛠️ Tech Stack](#-tech-stack)
* [📂 Project Structure](#-project-structure)
* [🚀 Getting Started](#-getting-started)
* [🔑 Environment Variables](#-environment-variables)
* [📡 API Documentation](#-api-documentation)
* [☁️ Cloud Deployment Configuration](#%EF%B8%8F-cloud-deployment-configuration)
* [🤖 My AI Usage](#-my-ai-usage)
* [📄 License](#-license)
* [Author](#author)

---

## 🌟 Key Features

### 🤖 AI Crop Diagnostics
* Upload leaf photos to detect plant diseases (e.g., smut, rust, blast, tikka) instantly.
* Real-time image quality analyzer checks if image is too blurry or dark.
* Offers expert prevention methods, treatment recommendations, and severity alerts.
* Logs diagnosed cases in MongoDB for regional historical telemetry.

### 🌾 Peer-to-Peer Marketplace
* Direct farmer-to-buyer crop listing and purchasing.
* Integrated with **Razorpay Payment Gateway** for secure transactions.
* Automatic PDF invoice generation for order receipts and audits.

### 📈 APMC Price Ticker
* Live marquees displaying real-time commodity prices in regional APMC markets.
* Filter by crop and market location to get the best pricing options.

### 🌦️ Localized Weather & Subsidies
* Geo-location based weather widget offering localized agricultural advisories.
* Subsidies and welfare schemes portal to track active state/central government agricultural benefits.

### 🏛️ Grievance Routing & Admin Panel
* Automated complaint board with role-based routing (Farmer -> Dept Admin -> Supreme Admin).
* Admin telemetry dashboard displaying resolving rates, user counts, and platform sales.

---

## 🤖 AI Diagnostics Engine

The AI Diagnostics Engine operates as a high-performance Python FastAPI microservice that processes plant image submissions:

1. **Neural Network Model**: Uses an **EfficientNetB3 Convolutional Neural Network (CNN)** (`crop_disease_model.h5`) trained on the PlantVillage dataset, delivering 90%+ classification accuracy across crop diseases.
2. **CLAHE Image Preprocessing**: Enhances input image contrast dynamically using OpenCV **CLAHE** (Contrast Limited Adaptive Histogram Equalization). If OpenCV is missing, it runs a custom fallback preprocessing algorithm using Pillow filters.
3. **Quality Check Advisories**: Recommends fixes if a photo is too blurry (Laplacian variance check) or too dark, helping farmers take better diagnostic photos.

---

## 🏗️ System Architecture

```text
       ┌────────────────────────┐
       │   React SPA (Client)   │ (Vercel, i18n, Localized Weather)
       └───────────┬────────────┘
                    │
          HTTPS / JSON (Port 5000)
                    │
       ┌───────────▼────────────┐
       │   Node.js/Express API  │ (Render, Multer upload, Mongoose Schema)
       └─────┬───────────┬──────┘
             │           │
    MongoDB (Atlas)    REST / MultiPart (Port 8005)
             │           │
    ┌─────────▼─┐   ┌─────▼────────────────────┐
    │ Database  │   │ FastAPI AI Service       │ (Hugging Face / Docker
    └───────────┘   │ (Python TensorFlow Venv) │  EfficientNetB3 Inference)
                    └──────────────────────────┘
```

---

## 🛠️ Tech Stack

* **Frontend**: React.js (v18), React Router Dom (v6), i18next (Localization), Vanilla CSS (Glassmorphism UI).
* **Backend**: Node.js, Express, JWT, Multer, Nodemailer, Brevo HTTP API SDK.
* **AI Engine**: Python, FastAPI, TensorFlow 2.x, OpenCV, NumPy, Pillow.
* **Database**: MongoDB (Mongoose ODM).
* **Payment Gateway**: Razorpay Checkout SDK.

---

## 📂 Project Structure

```text
Khedut-Bhandhu/
├── frontend/                     # React Client App (Port 3000)
│   ├── public/                   # Static Assets
│   └── src/
│       ├── components/           # Dashboards, CropDiagnostics, Navbar, etc.
│       ├── App.js                # Router and view structures
│       └── apiConfig.js          # Centralized API configuration (Render/Local)
├── backend/                      # Node.js Express REST API (Port 5000)
│   ├── models/                   # Mongoose Schemas (User, DiseaseCase, Complaint)
│   ├── routes/                   # Endpoint routers (auth, user, market, schemes)
│   ├── services/                 # Brevo HTTP & Nodemailer email integrations
│   └── server.js                 # App configuration & FastAPI proxies
├── ai-service/                   # Python FastAPI AI Inference (Port 8005)
│   ├── main.py                   # Model Loader and inference endpoints
│   └── requirements.txt          # Python ML dependencies
├── render.yaml                   # 1-click Render blueprint specification
├── start_khedut_professional.bat # Combined multi-service launcher script
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites
* Node.js (v18 or higher)
* Python 3.10 to 3.12 (added to PATH)
* MongoDB (Atlas URL or Local instance)

### Local Launch (One-Click)

1. Open your terminal in the root folder and double-click the launcher script:
   ```powershell
   .\start_khedut_professional.bat
   ```
2. This opens three terminal windows launching the services:
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
EMAIL_PASS=your_gmail_app_password
BREVO_API_KEY=your_brevo_v3_api_key  # Optional: For bypass of Render SMTP block
```

Create a `.env` file in the `/frontend` folder:

```env
REACT_APP_API_URL=http://localhost:5000
```

---

## 📡 API Documentation

### Authentication & Authorization
| Method | Endpoint | Description |
|:---|:---|:---|
| **POST** | `/api/auth/signup` | Registers a new user |
| **POST** | `/api/auth/login` | Log in user (Sends OTP via secure SMTP/Brevo) |
| **POST** | `/api/auth/verify-otp` | Verifies login OTP code (Bypass code: 1234) |
| **POST** | `/api/auth/forgot-password`| Sends password-reset OTP code |

### AI Crop Diagnostics
| Method | Endpoint | Description |
|:---|:---|:---|
| **GET** | `/api/ai/health` | Checks if AI service and TensorFlow model are loaded |
| **POST**| `/api/ai/predict` | Uploads leaf photo to return class details & recommendations |

---

## ☁️ Cloud Deployment Configuration

### 1. Frontend (Vercel)
To successfully deploy the React application on Vercel without warnings interrupting the build:
* **Root Directory**: `frontend`
* **Build Command**: `CI=false npm run build`
* **Output Directory**: `build`
* **Install Command**: `npm install --legacy-peer-deps`
* **Environment Variables**: Add `REACT_APP_API_URL` set to your backend Render URL.

### 2. Backend (Render)
To deploy the Express server on Render:
* **Build Command**: `npm run build`
* **Start Command**: `npm start`
* **Environment Variables**: Add `MONGO_URI`, `JWT_SECRET`, `EMAIL_USER`, `EMAIL_PASS`, and `BREVO_API_KEY`.

### 3. AI Service (Hugging Face Spaces)
Because TensorFlow requires high memory, host the AI Service on Hugging Face Spaces (Docker SDK) for 16GB free RAM, exposing port `7860`. Change the `AI_SERVICE_URL` environment variable on Render to point to your space.

---

## 🤖 My AI Usage

During the development of this project, I paired with **Antigravity**, a Google DeepMind agentic coding assistant, to accelerate delivery and maintain clean standards:

1. **SMTP bypass on Render**: Worked together to integrate **Brevo's HTTP API** into the Node.js backend. This bypassed Render's port `587` SMTP outgoing block on the Free Tier, enabling OTP emails to send reliably.
2. **Robust Front-End Build**: Configured Vercel's build scripts with `CI=false` and `--legacy-peer-deps` to ensure successful compilation of React 19 dependencies.
3. **Decoupled AI Proxying**: Integrated native Express `FormData` pipelines to stream binary leaf image uploads seamlessly to the Python FastAPI server.

---

## 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

---

## 👨‍💻 Author
**Prince Padaliya**
* [GitHub](https://github.com/princepadaliya31)
* [LinkedIn](https://linkedin.com/in/princepadaliya)
* Email: princepadaliya31@gmail.com
