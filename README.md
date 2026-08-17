# ⚡ ApexScout AI — AI-Powered Sports Talent Assessment Platform

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![AI Video Engine](https://img.shields.io/badge/AI%20Engine-Biomechanical%20HUD-00F2FE.svg)](#)
[![Deepfake Forensics](https://img.shields.io/badge/Deepfake%20Filter-Anti--Tamper%20Active-39FF14.svg)](#)
[![Anti-Doping](https://img.shields.io/badge/Anti--Doping-24h%20WADA%20Verified-FF6B00.svg)](#)

> **ApexScout AI** is an end-to-end sports talent identification and scouting platform that combines **Computer Vision Biomechanical Motion Analysis**, **AI Deepfake & Speed-Tampering Detection**, **24-Hour Synchronized Medical/Anti-Doping Verification**, and a **Certified Coach-Athlete Marketplace**.

---

## 🌟 Key Features

### 1. 🎥 AI Video Motion & Biomechanics Analysis
- **Dribbling Speed & Cadence**: Measures ball oscillation frequency ($Hz$), hand alternation symmetry, and control height consistency.
- **Vertical Leap / Jump Height**: Calculates apex elevation ($h = \frac{1}{8} g t_{\text{air}}^2$), hang-time ($ms$), takeoff velocity, and landing knee flexion absorption angle.
- **Sprint & Agility Velocity**: Real-time ground speed ($km/h$) and acceleration curves ($m/s^2$).
- **Live Canvas HUD**: Dynamic skeletal pose tracking and telemetry overlay.
- **Multiple Video Sources**: Preset benchmark drills, custom `.mp4`/`.webm` upload, or live webcam combine.

### 2. 🛡 AI Deepfake & Speed-Tampering Forensics
- **Temporal Speed Verification**: Scans video frames for artificial $1.1\times - 2.0\times$ playback acceleration (preventing faked speed/dribbling).
- **Generative AI Filter**: Detects synthetic frame morphing, unnatural limb interpolation, and Sora/Runway generation artifacts.
- **Physics Gravitational Check**: Cross-references parabolic trajectory against Earth gravity ($g = 9.81\text{ m/s}^2$).
- **Integrity Score**: Generates an authenticity audit report (e.g., `99.4% Authentic`).

### 3. 🧪 24-Hour Medical & Anti-Doping Verification Hub
- **24-Hour Time-Sync Window**: Validates that medical testing was conducted within **24 hours** of the video recording ($\Delta t \le 24\text{ hours}$). Flags outdated reports.
- **WADA Prohibited Substance Screen**: Verifies panels for Anabolic Agents, Peptide Hormones (EPO/hGH), Beta-2 Agonists, SARMs, and Stimulants.
- **Official Verification Token**: Generates unique `APEX-MED-XXXX-XXXX` tokens with QR verification mockup.

### 4. 👥 Coaches & Talent Scouts Marketplace
- Filter top certified scouts and development directors by sport (Basketball, Soccer, Track/Athletics, Cricket, Tennis).
- **1-Click Dossier Dispatch**: Send verified AI video telemetry + 24h medical clearance directly to coaches.
- **Interactive Direct Messaging**: Real-time simulated communication with scouts.

### 5. 🏆 Verified Talent Leaderboard
- Global rankings sorted by Jump Height, Dribble Frequency, Sprint Velocity, or Overall Combine Rating.
- Clear trust badges: **`✓ AI Authenticated`** and **`🛡 24h Med Cleared`**.

### 6. 📞 24/7 Helpline & Sports Physio AI
- **Emergency Directory**: Direct hotlines for Sports Trauma, Mental Wellness, Concussion Protocol, and CleanSport Advisory.
- **AI Sports Physio Bot**: Interactive medical assistant providing instant guidance on **RICE injury protocol**, **patellar tendon pain**, and **WADA regulations**.
- **SOS Emergency Ticket System**: High-priority dispatch form with tracking IDs.

---

## 🚀 Quick Start (Local Setup)

### Option A: Run with Built-in Python Server (Recommended)
```bash
# Navigate to the project directory
cd sports-talent-ai

# Start the local server
python server.py
```
Open your browser and navigate to: **`http://localhost:8000`**

### Option B: Open Directly in Browser
Double-click `index.html` in your file explorer to run the standalone web application.

---

## 📦 How to Upload & Push to GitHub

Follow these simple steps to push the entire codebase to your GitHub account:

### Step 1: Create a New Repository on GitHub
1. Go to [GitHub.com](https://github.com) and click **"New repository"**.
2. Name the repository (e.g., `sports-talent-ai` or `apexscout-ai`).
3. Set the repository to **Public** (or Private).
4. **Do NOT** initialize with a README, .gitignore, or License (these are already included in this project).
5. Click **"Create repository"** and copy the repository URL (e.g., `https://github.com/YOUR_USERNAME/sports-talent-ai.git`).

### Step 2: Initialize Git and Push from Terminal
Run the following commands in PowerShell inside the `sports-talent-ai` folder:

```powershell
# 1. Initialize Git repository
git init -b main

# 2. Add all project files
git add .

# 3. Commit the initial release
git commit -m "Initial commit: AI Sports Talent Assessment Platform with 24h Medical & Deepfake Detection"

# 4. Link your remote GitHub repository (replace with your actual URL)
git remote add origin https://github.com/YOUR_USERNAME/sports-talent-ai.git

# 5. Push code to GitHub
git push -u origin main
```

---

## 🌐 Deploying to GitHub Pages (Free 1-Click Hosting)

1. In your GitHub repository, go to **Settings** > **Pages**.
2. Under **Build and deployment** > **Source**, select **GitHub Actions** (or select **Deploy from a branch** > branch: `main` > folder: `/ (root)`).
3. The pre-configured `.github/workflows/deploy.yml` workflow will automatically build and publish your site at:
   `https://YOUR_USERNAME.github.io/sports-talent-ai/`

---

## 🏗 Directory Architecture

```
sports-talent-ai/
├── .github/
│   └── workflows/
│       └── deploy.yml              # Automatic GitHub Pages CI/CD deployment
├── assets/
│   ├── css/
│   │   ├── style.css               # Kinetic dark sports-tech design system
│   │   └── responsive.css          # Mobile/tablet responsiveness
│   ├── js/
│   │   ├── app.js                  # Central controller & tab router
│   │   ├── ai-engine.js            # Video canvas HUD & pose estimation
│   │   ├── deepfake-detector.js    # AI video tampering & speedup detector
│   │   ├── medical-verifier.js     # 24-hour medical & anti-doping verification
│   │   ├── coaches.js              # Coach directory & direct chat
│   │   ├── leaderboard.js          # Talent rankings & scout modals
│   │   ├── helpline.js             # 24/7 hotlines & AI Physio chatbot
│   │   └── sample-data.js          # Benchmarks, coaches & sample datasets
│   └── images/
├── index.html                      # Single Page Application
├── server.py                       # Python 3 local server with REST API
├── .gitignore                      # Git ignore rules
└── README.md                       # Documentation & GitHub guide
```

---

## 📄 License
This project is open-source and available under the [MIT License](LICENSE).
