# 🚀 Stock Price Prediction System: ClarityTrade 📈  
**✨ Where data science meets investment strategy for better financial decisions 💰**  

---

# 🔍 ClarityTrade - Stock Prediction & Investment Analysis Platform  

![ClarityTrade Website](https://github.com/GourabGorai/Hack4bengal/blob/main/static/Screenshot%202025-04-27%20104306.png)  

ClarityTrade is a cutting-edge 💻, data-driven 📊 investment analysis platform that combines 🤖 machine learning predictions with real-time market news 📰 to provide actionable investment insights.  

**Have a try :- https://obnoxious-erna-bfdfdgd-fc37455c.koyeb.app/**

---

## 🌟 Key Features  

- **📈 Stock Price Prediction**: Uses Random Forest Regressor to predict future stock prices with 90%+ accuracy  
- **📊 Technical Indicators**: Calculates MA, RSI, MACD, and volatility metrics 🔢  
- **💡 Smart Recommendations**: AI-generated investment decisions 🤖 → 📈 → 💵  
- **🗞️ Real-time News Integration**: Fetches relevant stock news for context 📰🔥  
- **📊 Interactive Visualization**: Beautiful Plotly graphs showing predicted vs actual prices 📉 ↔️ 📈  
- **🤖 AI Chatbot Assistant**: Get instant answers about your investments 💬❓  
- **🔒 Secure Authentication**: Email-based verification system ✉️ → 🔑  
- **📅 Prediction History**: Tracks all your predictions in PostgreSQL database 💾  

---

## ⚙️ Tech Stack  

| Category              | Technologies Used                          |
|-----------------------|-------------------------------------------|
| **🧱 Backend**        | Python 🐍, Flask 🌶️                      |
| **🎨 Frontend**       | HTML5, CSS3, JavaScript                   |
| **🧠 Machine Learning**| Scikit-learn, Pandas 🐼, NumPy            |
| **📊 Data Viz**       | Plotly 📈                                 |
| **🗃️ Database**       | PostgreSQL 🐘                             |
| **🔌 APIs**           | Alpha Vantage, Google News API            |
| **✉️ Email**          | SMTP with SSL 🔐                          |
| **🤖 AI**             | Gemini integration 🧠                     |

---

## 🛠️ Installation Guide  

1. **Clone the repository**  
   ```bash
   git clone https://github.com/yourusername/ClarityTrade.git
   cd ClarityTrade

2. **Set up virtual environment**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # 🪟 Windows: `venv\Scripts\activate`
   ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment**  
   Create `.env` file with:  
   ```
   DB_URL=your_postgresql_connection_string
   ALPHA_VANTAGE_API_KEY=your_key_here
   GOOGLE_NEWS_API_KEY=your_key_here
   HOLIDAY_API_KEY=your_key_here
   EMAIL_ADDRESS=your_email@gmail.com
   EMAIL_PASSWORD=your_app_password
   ```

5. **Initialize database**  
   ```bash
   python init_db.py
   ```

6. **Launch application**  
   ```bash
   python app.py
   ```

---

## 🖥️ Usage Instructions  

1. Access at `http://localhost:5000` 🌐  
2. Login with email (verification code sent) ✉️ → 🔢  
3. Select stock symbol (e.g., AAPL, TSLA) and future date 📅  
4. View predictions, decisions, and news 📊💡🗞️  
5. Chat with AI assistant about investments 💬🤖  

---

## 📂 Project Structure  

```bash
ClarityTrade/
├── app.py                # 🚀 Flask application core
├── test.py               # 🛠️ Helper functions
├── requirements.txt      # 📦 Dependencies
├── static/               # 🖼️ Static assets
│   ├── style.css         # 🎨 Styles
│   ├── favicon.png       # 🏷️ Logo
│   └── background.mp4    # 🎥 BG video
├── templates/            # 📄 HTML views
│   └── index.html        # 🏠 Main page
├── .env                  # 🔐 Config
└── README.md             # 📖 This file
```

---

## 🔑 Required API Keys  

| Service          | Purpose                  |
|------------------|--------------------------|
| Alpha Vantage    | Stock market data 📈     |
| Google News      | Financial news 📰        |
| Holiday API      | Market calendar 🗓️      |

---
## 👨‍💻Meet Our Team:
![team](https://github.com/GourabGorai/Hack4bengal/blob/main/static/hack4bengal%20CodeFusion%20Innovators%20.png)
---

## 🤝 Contributing  

We welcome contributions! 🎉  
1. Fork the repo 🍴  
2. Create your feature branch 🌿  
3. Commit changes 💾  
4. Push to the branch 🚀  
5. Open a PR 📬  

---

## 📜 License  

MIT Licensed - See [LICENSE](LICENSE) for details.  
