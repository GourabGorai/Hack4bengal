
# Stock Price Prediction System: ClarityTrade 📈
Tagline: Where data science meets investment strategy for better financial decisions

# 📊 ClarityTrade – Your AI Investment Assistant

🚀 **Live Demo:** https://obnoxious-erna-bfdfdgd-fc37455c.koyeb.app/

---

## 🧠 Project Overview

**ClarityTrade** is a powerful AI-driven stock analysis and investment decision support system built using **Python**, **Flask**, and advanced machine learning techniques. It helps investors make informed decisions by combining real-time stock predictions, technical analysis, interactive charts, and AI-powered insights—all within a secure and user-friendly web interface.

---

## 🔑 Key Features

### 📈 Real-Time Stock Predictions
- **Machine Learning Forecasting:** Utilizes Random Forest Regression along with technical indicators like RSI, MACD, and Moving Averages.
- **Historical Data Analysis:** Fetches and analyzes historical stock data using the **Alpha Vantage API** for better predictions.

### 💡 Investment Decision Support
- **AI Recommendations:** Integrates Google News API and Gemini AI to analyze market sentiment and provide actionable investment tips.
- **Formatted Reports:** Generates easy-to-read reports with bold highlights, bullet points, and clean HTML formatting.

### 📊 Interactive Visualizations
- **Plotly Charts:** Interactive graphs showing predicted vs. actual stock prices over time.
- **Dynamic Updates:** Real-time visualization updates based on user input.

### 🔐 Secure User Authentication
- **Login/Signup System:** Email verification and password protection.
- **Session Handling:** Secure data logging and user tracking.

### 🗓 Market Awareness
- **Holiday Detection:** Checks trading holidays using the Holiday API to prevent invalid predictions.

### 🤖 Chatbot Integration
- **Gemini AI Chatbot:** Provides contextual, smart responses to investment-related questions and gracefully handles unrelated queries.

### 📧 Email Notifications
- **Verification Emails:** Sends OTPs for account verification using SMTP.
- **Future Enhancements:** Plans to support custom stock alerts and updates via email.

### 🧩 Modular and Scalable Design
- **Flask Backend:** Lightweight yet powerful backend structure.
- **Clean Codebase:** Modular code for easy extension and feature integration.

### 🌐 Open Source and Extendable
- Contributions are welcome! Fork it, build on it, or suggest improvements through pull requests.

---

## 🚀 Hackathon Progress

1. Data Retrieval  
2. Data Preprocessing  
3. Random Forest Regressor Model  
4. Frontend Design  
5. Chatbot Integration  

---

## 🛠 Tech Stack

- **Languages & Frameworks:** Python, Flask  
- **Machine Learning:** Scikit-learn, Pandas, NumPy  
- **Visualization:** Plotly  
- **APIs Used:** Alpha Vantage, Google News, Gemini AI, Holiday API  
- **Authentication & Notifications:** SMTP (for email verification)  
- **Deployment:** Koyeb  

---

## 📂 Project Structure (Example)

claritytrade/
│
├── app/                             # Core application package
│   ├── __init__.py                  # Initializes the Flask app
│   ├── routes.py                    # Flask routes and endpoints
│   ├── models/                      # Machine learning models
│   │   ├── predictor.py             # Random Forest prediction logic
│   │   └── indicators.py            # RSI, MACD, Moving Average calculators
│   ├── services/                    # External service integrations
│   │   ├── news_fetcher.py          # Google News API integration
│   │   ├── chatbot.py               # Gemini AI chatbot logic
│   │   ├── holiday_checker.py       # Holiday API logic
│   │   └── email_service.py         # SMTP email verification
│   ├── utils/                       # Helper functions and data processing
│   │   ├── data_loader.py           # Fetch and preprocess stock data
│   │   └── visualizer.py            # Plotly chart functions
│   └── auth/                        # User authentication system
│       ├── auth_routes.py           # Login, Register routes
│       └── security.py              # Password hashing, validation
│
├── templates/                       # HTML templates (Jinja2)
│   ├── layout.html
│   ├── index.html
│   ├── dashboard.html
│   ├── login.html
│   └── register.html
│
├── static/                          # Static files (CSS, JS, images)
│   ├── css/
│   ├── js/
│   └── images/
│
├── main.py                          # Entry point to start the Flask server
├── config.py                        # App configuration settings
├── requirements.txt                 # Python dependencies
├── README.md                        # Project documentation
└── .env                             # Environment variables (API keys, secrets)

---

## 💡 Future Improvements

- 📬 Email alerts for stock surges or investment opportunities  
- 📝 Exportable investment reports (PDF, CSV)  
- 📱 Mobile-friendly design  
- 📌 Personalized dashboard with user watchlist  

---

## 📜 License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author
 CodeFusion Innovators

---

## ⭐ Show Your Support

If you like this project, give it a ⭐ on GitHub and share it with your network!


