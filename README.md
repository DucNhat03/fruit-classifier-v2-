# 🍎 Fruit Classification System
## Machine Learning-Powered E-commerce Platform

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.2.5-green.svg)](https://flask.palletsprojects.com/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.x-red.svg)](https://opencv.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.x-orange.svg)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> **An intelligent fruit classification system combining Machine Learning algorithms (Random Forest & SVM) with a modern e-commerce platform for academic research and practical applications.**

---

## 📋 Table of Contents

- [🎯 Project Overview](#-project-overview)
- [🏗️ Technical Architecture](#️-technical-architecture)
- [✨ Key Features](#-key-features)
- [🚀 Installation & Setup](#-installation--setup)
- [💻 Usage Guide](#-usage-guide)
- [🔬 AI Models & Performance](#-ai-models--performance)
- [📁 Project Structure](#-project-structure)
- [🔒 Security Features](#-security-features)
- [🛤️ Future Development](#️-future-development)
- [📚 References](#-references)
- [📞 Support](#-support)

---

## 🎯 Project Overview

The **Fruit Classification System** is an advanced academic project that demonstrates the practical application of Machine Learning in e-commerce environments. This system integrates computer vision, machine learning algorithms, and web technologies to create an intelligent fruit recognition and sales platform.

### 🎓 Academic Context
- **Course**: Pattern Recognition and Deep Learning (PTDL2)
- **Team**: NHOM3DM - DHKTPM17ATT
- **Objective**: Demonstrate ML/AI capabilities in real-world applications
- **Focus**: Comparative analysis of Random Forest vs SVM algorithms
- **Dataset**: Fruits-360 (15 fruit categories, standardized 45x45 pixel images)

### 🏆 Key Achievements
- ✅ **Dual Algorithm Implementation**: Random Forest & SVM comparison
- ✅ **Real-time Image Processing**: Instant fruit classification
- ✅ **Professional Web Interface**: Modern, responsive design
- ✅ **Complete E-commerce Integration**: User management, shopping cart, checkout
- ✅ **Academic Documentation**: Comprehensive analysis and reporting

---

## 🏗️ Technical Architecture

### ML Pipeline Architecture
```
Input Image (Any Size)
         ↓
   Preprocessing Layer
   (Resize → 45x45 → Normalize)
         ↓
   Feature Extraction
   (PCA: 6075 → 50 components)
         ↓
   Dual Model Prediction
   ┌─────────────┬─────────────┐
   │ Random Forest│     SVM     │
   │  (n_trees)   │ (RBF kernel)│
   └─────────────┴─────────────┘
         ↓             ↓
   Confidence Score & Class Prediction
         ↓
   Ensemble Analysis & Final Result
```

### System Architecture
```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Frontend      │    │   Backend       │    │   ML Engine     │
│   (HTML/CSS/JS) │────│   (Flask)       │────│   (sklearn)     │
│                 │    │                 │    │                 │
│ • Upload UI     │    │ • Route Handler │    │ • Model Loading │
│ • Results View  │    │ • Session Mgmt  │    │ • Preprocessing │
│ • Shopping Cart │    │ • Data Storage  │    │ • Prediction    │
│ • User Auth     │    │ • API Endpoints │    │ • Postprocessing│
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

---

## ✨ Key Features

### 🤖 AI Analysis Core
- **Dual Algorithm Classification**: Random Forest + SVM ensemble
- **Real-time Processing**: Instant image analysis and prediction
- **Confidence Scoring**: Detailed probability analysis for each model
- **Model Comparison**: Side-by-side algorithm performance analysis
- **Image Preprocessing**: Automated resizing, normalization, and feature extraction

### 🖥️ User Interface
- **Modern Web Design**: Responsive, professional layout
- **Interactive Upload**: Drag-and-drop image upload with preview
- **Live Results**: Real-time classification with confidence visualization
- **Technical Details**: Algorithm explanations and model insights
- **Academic Focus**: Detailed technical information for research purposes

### 👥 User Management
- **Account System**: User registration and authentication
- **Profile Management**: Personal information and order history
- **Session Management**: Secure login/logout functionality
- **Admin Controls**: Product and user management capabilities

### 🛒 E-commerce Integration
- **Product Catalog**: 15+ fruit varieties with detailed information
- **Shopping Cart**: Add/remove items with quantity management
- **Checkout System**: Complete order processing workflow
- **Receipt Generation**: Digital receipts for completed purchases
- **Inventory Management**: Real-time stock tracking

---

## 🚀 Installation & Setup

### Prerequisites
```powershell
Python 3.8+
pip (Python package manager)
```

### Quick Start
1. **Clone or Extract the Project**
   ```powershell
   cd d:\Studies\HK2_Y4\PTDL2\fruit-app\fruit-classifier
   ```

2. **Install Dependencies**
   ```powershell
   pip install -r requirements.txt
   ```

3. **Verify ML Models**
   Ensure these files exist in `models/` directory:
   - `random_forest_model.pkl`
   - `svm_model.pkl`
   - `pca.pkl`
   - `scaler.pkl`
   - `id_to_label_dict.pkl`

4. **Run the Application**
   ```powershell
   python app.py
   ```

5. **Access the System**
   Open your browser and navigate to: `http://localhost:5000`

### Demo Credentials
For testing purposes, you can use:
- **Username**: demo_user
- **Password**: demo123
- **Admin**: admin / admin_password

---

## 📚 References

### Academic Papers
1. **Breiman, L.** (2001). Random Forests. *Machine Learning*, 45(1), 5-32.
2. **Cortes, C., & Vapnik, V.** (1995). Support-vector networks. *Machine Learning*, 20(3), 273-297.
3. **Jolliffe, I. T.** (2002). Principal Component Analysis. *Springer Series in Statistics*.

### Datasets
- **Fruits-360**: [Kaggle Dataset](https://www.kaggle.com/moltean/fruits)
- **Original Paper**: Mureșan, H., & Oltean, M. (2018). Fruit recognition from images using deep learning.

### Libraries & Frameworks
- **Flask**: [Official Documentation](https://flask.palletsprojects.com/)
- **scikit-learn**: [User Guide](https://scikit-learn.org/stable/)
- **OpenCV**: [Documentation](https://docs.opencv.org/)
- **NumPy**: [Documentation](https://numpy.org/doc/)

### Technical Resources
- **Random Forest**: [sklearn.ensemble.RandomForestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html)
- **SVM**: [sklearn.svm.SVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html)
- **PCA**: [sklearn.decomposition.PCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html)

---


<div align="center">

**🍎 Fruit Classification System - Combining AI Excellence with Practical Applications 🚀**

*Developed with ❤️ for academic research and practical learning*

**© 2025 Đức Nhật - PTDL2 Course Project**

</div>
