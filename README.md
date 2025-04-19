
# Stock Price Prediction System: ClarityTrade 📈
Tagline: Where data science meets investment strategy for better financial decisions

A comprehensive web application for stock price prediction using machine learning, technical analysis, and AI-powered investment recommendations.

## Technical Architecture 🏗️

### 1. Machine Learning Model
- **Random Forest Regressor**: Ensemble learning method for prediction
- **Features Used**:
  - Closing Prices
  - Moving Averages (5, 10, 50 days)
  - Volatility
  - RSI (Relative Strength Index)
  - MACD (Moving Average Convergence Divergence)

### 2. Technical Indicators 📊

#### RSI (Relative Strength Index)
```python
RSI = 100 - (100 / (1 + RS))
where RS = Average Gain / Average Loss
```
- Measures momentum and oversold/overbought conditions
- 14-day period used for calculations
- Values > 70 indicate overbought, < 30 indicate oversold

#### MACD (Moving Average Convergence Divergence)
```python
MACD = Fast EMA - Slow EMA
Signal Line = 9-day EMA of MACD
```
- Shows relationship between two moving averages
- Default periods: 12-day and 26-day EMAs
- Helps identify trend direction and momentum

### 3. Data Processing Pipeline 🔄

1. **Data Fetching**
   - AlphaVantage API for historical stock data
   - Daily time series with OHLCV data
   - Holiday API integration for market closure days

2. **Feature Engineering**
   - Technical indicator calculations
   - Data normalization using StandardScaler
   - Missing value handling

3. **Model Training**
   - Train-test split based on temporal order
   - Feature scaling for numerical stability
   - Cross-validation for model robustness

### 4. Security Implementation 🔐

1. **User Authentication**
   - Email verification system
   - PostgreSQL database for user management
   - Session management for secure access

2. **API Security**
   - Secure API key storage
   - Rate limiting implementation
   - HTTPS for data transmission

### 5. Investment Analysis 💹

1. **News Integration**
   - Google News API for market sentiment
   - Real-time news aggregation
   - Sentiment analysis for decision support

2. **AI-Powered Recommendations**
   - Gemini AI integration for advanced analysis
   - Natural language processing for queries
   - Context-aware response generation

## Implementation Details 🛠️

### Database Schema
```sql
CREATE TABLE stockhistory (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255),
    stock_symbol VARCHAR(10),
    prediction_date DATE,
    prediction_timestamp TIMESTAMP,
    predicted_value FLOAT
);
```

### Performance Metrics
- R² Score for model accuracy
- Real-time prediction tracking
- Historical prediction logging

## Mathematical Foundations 📐

### 1. Moving Averages
```
Simple Moving Average (SMA) = Σ(prices) / n
Exponential Moving Average (EMA) = α × price + (1 - α) × previous_EMA
where α = 2/(n + 1)
```

### 2. Volatility Calculation
```
Daily Volatility = High Price - Low Price
```

### 3. Random Forest Model
- Ensemble of decision trees
- Bootstrap aggregating (bagging)
- Feature importance scoring

## Error Handling ⚠️

1. **Data Validation**
   - Input sanitization
   - Date range verification
   - Symbol existence check

2. **API Fallbacks**
   - Retry mechanisms
   - Alternative data sources
   - Error logging

## Future Enhancements 🚀

1. **Advanced Features**
   - Additional technical indicators
   - Market sentiment analysis
   - Portfolio optimization

2. **Model Improvements**
   - Deep learning integration
   - Real-time model updates
   - Automated hyperparameter tuning

## Dependencies 📦

```python
flask==2.0.1
pandas==1.3.0
scikit-learn==0.24.2
plotly==5.3.1
psycopg2==2.9.1
requests==2.26.0
numpy==1.21.0
```
