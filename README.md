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

## 💻 Usage Guide

### 🔬 AI Classification Demo
1. **Navigate to AI Recognition**
   - Click "AI Recognition" in the main navigation
   - View technical information about the ML models

2. **Upload Test Image**
   - Use the upload interface to select a fruit image
   - Supported formats: JPG, JPEG, PNG
   - Image will be automatically preprocessed

3. **Analyze Results**
   - View predictions from both Random Forest and SVM
   - Compare confidence scores and model agreement
   - Understand the technical analysis provided

### 🛍️ E-commerce Features
1. **Browse Products**
   - Explore the fruit catalog with prices and descriptions
   - View available stock and product details

2. **Make Purchases**
   - Add items to cart and adjust quantities
   - Complete checkout process with order summary
   - Receive digital receipt confirmation

### 👤 Account Management
1. **Create Account**
   - Register with username, email, and password
   - Access personalized features and order history

2. **User Dashboard**
   - View personal information and preferences
   - Track order history and account activity

---

## 🔬 AI Models & Performance

### Random Forest Algorithm
**Configuration:**
- **Estimators**: 100 decision trees
- **Features**: 50 PCA components
- **Criterion**: Gini impurity
- **Max Depth**: Auto-optimized

**Advantages:**
- ✅ Excellent handling of overfitting
- ✅ Robust to outliers and noise
- ✅ Feature importance analysis
- ✅ Fast training and prediction

### Support Vector Machine (SVM)
**Configuration:**
- **Kernel**: Radial Basis Function (RBF)
- **Regularization**: C parameter optimization
- **Gamma**: Auto-scaled
- **Features**: 50 PCA components

**Advantages:**
- ✅ Effective in high-dimensional spaces
- ✅ Memory efficient
- ✅ Versatile kernel functions
- ✅ Strong theoretical foundation

### Model Comparison Analysis
| Metric | Random Forest | SVM | Ensemble |
|--------|---------------|-----|----------|
| **Accuracy** | ~85-90% | ~80-85% | ~90-95% |
| **Speed** | Fast | Moderate | Fast |
| **Memory** | Moderate | Low | Moderate |
| **Interpretability** | High | Low | High |

### Dataset Information
- **Source**: Fruits-360 Dataset
- **Categories**: 15 fruit types
- **Image Size**: 45x45 pixels (standardized)
- **Preprocessing**: PCA dimensionality reduction (6075 → 50 features)
- **Training Split**: 80% training, 20% validation

### Supported Fruit Categories
1. **Apple 5** - Green apples
2. **Apple 6** - Red apples
3. **Apricot 1** - Fresh apricots
4. **Avocado 1** - Ripe avocados
5. **Banana 1** - Yellow bananas
6. **Blackberrie 1** - Fresh blackberries
7. **Blueberry 1** - Premium blueberries
8. **Carrot 1** - Fresh carrots
9. **Cherry 1** - Premium cherries
10. **Lemon 1** - Yellow lemons
11. **Lychee 1** - Vietnamese lychees
12. **Strawberry 1** - Fresh strawberries
13. **Strawberry Wedge 1** - Sliced strawberries
14. **Tomato 1** - Cherry tomatoes
15. **Watermelon 1** - Red watermelons

---

## 📁 Project Structure

```
fruit-classifier/
├── 📄 app.py                 # Main Flask application
├── 📄 requirements.txt       # Python dependencies
├── 📁 models/               # Pre-trained ML models
│   ├── random_forest_model.pkl
│   ├── svm_model.pkl
│   ├── pca.pkl
│   ├── scaler.pkl
│   └── id_to_label_dict.pkl
├── 📁 templates/            # HTML templates
│   ├── ai_recognition.html  # AI demo interface
│   ├── index.html          # Home page
│   ├── login.html          # User authentication
│   ├── purchase.html       # Product catalog
│   ├── checkout.html       # Order processing
│   ├── admin_dashboard.html # Admin interface
│   └── user_dashboard.html  # User profile
├── 📁 static/              # Static assets
│   ├── 📁 uploads/        # User uploaded images
│   └── 📁 receipts/       # Generated receipts
├── 📁 data/               # Application data
│   ├── products.json      # Product database
│   └── users.json         # User database
└── 📁 images/             # Sample test images
    ├── tao5.jpg           # Apple samples
    ├── chuoi.jpg          # Banana samples
    ├── dautay.jpg         # Strawberry samples
    └── ...                # Other fruit samples
```

### Key Components

#### Core Application (`app.py`)
- **Flask Routes**: Web endpoint management
- **ML Integration**: Model loading and prediction logic
- **User Authentication**: Login/logout and session management
- **Database Operations**: JSON-based data storage
- **Image Processing**: Upload handling and preprocessing

#### Machine Learning Models (`models/`)
- **Random Forest**: Ensemble decision tree classifier
- **SVM**: Support vector machine with RBF kernel
- **PCA**: Principal component analysis for dimensionality reduction
- **Scaler**: Feature normalization and standardization
- **Label Dictionary**: Class mapping for predictions

#### User Interface (`templates/`)
- **Responsive Design**: Mobile-friendly layouts
- **Interactive Elements**: Dynamic content and user feedback
- **Professional Styling**: Modern, academic-appropriate design
- **Technical Documentation**: In-built explanations and analysis

---

## 🔒 Security Features

### Data Protection
- **Session Management**: Secure user session handling
- **Password Security**: Hashed password storage (recommended)
- **Input Validation**: File type and size restrictions
- **SQL Injection Prevention**: JSON-based data storage

### File Security
- **Upload Restrictions**: Limited file types and sizes
- **Safe File Handling**: UUID-based filename generation
- **Directory Protection**: Isolated upload directories

### User Privacy
- **Data Minimization**: Only essential user data collection
- **Session Timeout**: Automatic logout for inactive sessions
- **Secure Routes**: Protected admin and user areas

### Recommendations for Production
- [ ] Implement HTTPS encryption
- [ ] Add database encryption
- [ ] Enable CSRF protection
- [ ] Implement rate limiting
- [ ] Add comprehensive logging

---

## 🛤️ Future Development

### Planned Enhancements

#### 🤖 AI & ML Improvements
- [ ] **Deep Learning Integration**: CNN-based classification models
- [ ] **Model Ensemble**: Advanced voting and stacking methods
- [ ] **Real-time Training**: Online learning capabilities
- [ ] **Augmentation Pipeline**: Data augmentation for improved accuracy
- [ ] **Explainable AI**: LIME/SHAP integration for model interpretability

#### 🖥️ Platform Features
- [ ] **Mobile Application**: Native iOS/Android apps
- [ ] **REST API**: Full API for third-party integrations
- [ ] **Real-time Analytics**: Dashboard with live statistics
- [ ] **Multi-language Support**: Internationalization features
- [ ] **Cloud Deployment**: AWS/Azure/GCP integration

#### 📊 Analytics & Monitoring
- [ ] **Performance Metrics**: Detailed model performance tracking
- [ ] **User Analytics**: Behavior analysis and insights
- [ ] **A/B Testing**: Model comparison and optimization
- [ ] **Error Monitoring**: Automated error detection and reporting

#### 🔧 Technical Improvements
- [ ] **Database Migration**: PostgreSQL/MongoDB integration
- [ ] **Caching Layer**: Redis for improved performance
- [ ] **Microservices**: Containerized architecture
- [ ] **CI/CD Pipeline**: Automated testing and deployment

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

## 📞 Support

### Getting Help
- **Issues**: Report bugs and feature requests via GitHub Issues
- **Documentation**: Refer to inline code comments and this README
- **Academic Support**: Contact course instructors for academic guidance

### Contributing
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Contact Information
- **Developer**: Đức Nhật
- **Team**: NHOM3DM
- **Course**: Pattern Recognition and Deep Learning (PTDL2)
- **Class**: DHKTPM17ATT
- **Institution**: [Your University]

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Copyright Notice
**© 2025 Đức Nhật - All Rights Reserved**

This project is the intellectual property of Đức Nhật, developed as part of the PTDL2 course academic requirements.

### Academic Use
This project is developed for academic purposes as part of a university course. Feel free to use it as a reference for learning and research, but please provide appropriate attribution when using any part of this work.

---

## 🎯 Project Demo

### Quick Demo Steps
1. **Start the application**: `python app.py`
2. **Open browser**: Navigate to `http://localhost:5000`
3. **Test AI Recognition**: Upload a fruit image from the `images/` folder
4. **Compare Models**: View Random Forest vs SVM predictions
5. **Explore E-commerce**: Browse products and test the shopping functionality

### Demo Images Available
- `tao5.jpg`, `tao6.jpg` - Apple varieties
- `chuoi.jpg` - Banana
- `dautay.jpg` - Strawberry
- `chanh.jpg` - Lemon
- `cherry.jpg` - Cherry
- `bo.jpg`, `bo2.jpg` - Avocado
- And many more in the `images/` directory

---

<div align="center">

**🍎 Fruit Classification System - Combining AI Excellence with Practical Applications 🚀**

*Developed with ❤️ for academic research and practical learning*

**© 2025 Đức Nhật - PTDL2 Course Project**

</div>
