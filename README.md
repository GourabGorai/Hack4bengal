
# Stock Price Prediction System: ClarityTrade 📈
Tagline: Where data science meets investment strategy for better financial decisions

# ClarityTrade - Stock Prediction and Investment Analysis Platform

![ClarityTrade Logo](static/favicon.png)

ClarityTrade is a data-driven investment analysis platform that combines machine learning predictions with real-time market news to provide actionable investment insights.

## Features

- **Stock Price Prediction**: Uses Random Forest Regressor to predict future stock prices
- **Technical Indicators**: Calculates MA, RSI, MACD, and volatility metrics
- **Investment Recommendations**: Provides AI-generated investment decisions
- **Real-time News Integration**: Fetches relevant stock news for context
- **Interactive Visualization**: Displays predicted vs actual prices with Plotly
- **AI Chatbot**: Allows users to ask questions about investment decisions
- **User Authentication**: Email-based verification system
- **Prediction History**: Stores user predictions in a PostgreSQL database

## Technologies Used

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, JavaScript
- **Machine Learning**: Scikit-learn, Pandas, NumPy
- **Data Visualization**: Plotly
- **Database**: PostgreSQL
- **APIs**: Alpha Vantage (stock data), Google News API
- **Email**: SMTP with SSL
- **AI Chatbot**: Gemini integration

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ClarityTrade.git
   cd ClarityTrade

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   Create a `.env` file in the root directory with the following variables:
   ```
   DB_URL=your_postgresql_connection_string
   ALPHA_VANTAGE_API_KEY=your_alpha_vantage_api_key
   GOOGLE_NEWS_API_KEY=your_google_news_api_key
   HOLIDAY_API_KEY=your_holiday_api_key
   EMAIL_ADDRESS=your_email@gmail.com
   EMAIL_PASSWORD=your_email_password
   ```

5. Initialize the database:
   ```bash
   python init_db.py
   ```

6. Run the application:
   ```bash
   python app.py
   ```

## Usage

1. Access the application at `http://localhost:5000`
2. Log in with your email (a verification code will be sent)
3. Select a stock symbol and future date
4. View the prediction results, investment decision, and relevant news
5. Use the chatbot to ask questions about the investment decision

## Project Structure

```
ClarityTrade/
├── app.py                # Main Flask application
├── test.py               # Helper functions (investment decision, news, chatbot)
├── requirements.txt      # Python dependencies
├── static/               # Static files (CSS, images, plots)
│   ├── style.css
│   ├── favicon.png
│   └── background-video.mp4
├── templates/            # HTML templates
│   └── index.html
├── .env                  # Environment variables
└── README.md             # Project documentation
```

## API Keys Required

- Alpha Vantage API (for stock data)
- Google News API (for stock news)
- Holiday API (for market holiday checks)

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


