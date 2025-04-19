import requests
import google.generativeai as genai
from googletrans import Translator
from datetime import datetime, timedelta

# Initialize the translator
translator = Translator()

# Function to translate text to English using googletrans
def translate_to_english(text):
    try:
        translated = translator.translate(text, dest='en')
        return translated.text
    except Exception as e:
        print(f"Error translating text: {e}")
        return text  # Return the original text if translation fails

# Function to fetch stock news using Finnhub API
def fetch_stock_news(stock_symbol, finnhub_api_key):
    # Set date range (last 7 days)
    to_date = datetime.now()
    from_date = to_date - timedelta(days=7)
    
    url = f"https://finnhub.io/api/v1/company-news?symbol={stock_symbol}&from={from_date.strftime('%Y-%m-%d')}&to={to_date.strftime('%Y-%m-%d')}&token={finnhub_api_key}"
    response = requests.get(url)
    
    if response.status_code == 200:
        news_data = response.json()
        # Extract headlines and ensure they're in English
        headlines = [article['headline'] for article in news_data if 'headline' in article]
        
        return headlines # Return top 10 headlines
    else:
        print(f"Error fetching stock news from Finnhub: {response.status_code}")
        return []

# Function to fetch current stock price using Alpha Vantage API
def fetch_current_price(stock_symbol, alpha_vantage_api_key):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={stock_symbol}&interval=1min&apikey={alpha_vantage_api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        price_data = response.json()
        # Extract the last closing price
        try:
            time_series = price_data.get("Time Series (1min)", {})
            latest_timestamp = max(time_series.keys())
            latest_data = time_series[latest_timestamp]
            return float(latest_data["4. close"])
        except (KeyError, ValueError):
            print("Error parsing stock price data.")
            return None
    else:
        print("Error fetching current stock price:", response.status_code, response.text)
        return None

# Function to use Gemini's generative model for suggestion
def get_financial_suggestion(predicted_price, current_price, stock_news):
    # Configure and create the generative model
    genai.configure(api_key="AIzaSyDYTE6N19xUpjUanmKtbR4ymkmOXcxG8OA")
    model = genai.GenerativeModel("gemini-1.5-flash")

    # Create payload
    payload = {
        "predicted_price": predicted_price,
        "current_price": current_price,
        "stock_news": stock_news,
        "accuracy of prediction": 99.2
    }

    # Generate text suggestion based on the payload
    response = model.generate_content(f"Provide me your financial suggestion according to {payload}")
    return response.text  # Return the generated suggestion

# Function to interact with the Gemini API as a chatbot
def chat_with_gemini(user_question):
    """Function to interact with the Gemini API and return chatbot response."""
    try:
        # Configure and create the generative model
        genai.configure(api_key="AIzaSyDYTE6N19xUpjUanmKtbR4ymkmOXcxG8OA")
        model = genai.GenerativeModel("gemini-1.5-flash")

        # Generate response from Gemini API
        response = model.generate_content(user_question)
        return response.text if response else "No response from Gemini."
    except Exception as e:
        return f"Error: {str(e)}"

# Main function to fetch data and make a suggestion
def make_investment_decision(predicted_price, stock_symbol, finnhub_api_key):
    # Fetch current stock price
    current_price = fetch_current_price(stock_symbol, 'LZIWKUHDC0XBETMU')
    if current_price is None:
        return "Unable to fetch current stock price. Decision cannot be made."

    # Fetch stock news from Finnhub
    stock_news = fetch_stock_news(stock_symbol, finnhub_api_key)
    if not stock_news:
        return "Unable to fetch stock news. Decision cannot be made."

    # Print stock news for context
    print("\nStock News Headlines:")
    for i, news in enumerate(stock_news, 1):
        print(f"{i}. {news}")

    # Get financial suggestion using Gemini's generative model
    suggestion = get_financial_suggestion(predicted_price, current_price, stock_news)
    data1 = f"\nFinancial Suggestion: {suggestion}"
    print(f"\nFinancial Suggestion: {suggestion}")

    # Disclaimer
    print("Disclaimer: This is a suggestion based on the provided information and should not be considered financial advice. Please consult with a financial professional before making any investment decisions.")
    return data1

# Example usage
if __name__ == "__main__":
    finnhub_api_key = "cvvsfh1r01qod00luea0cvvsfh1r01qod00lueag"  # Your Finnhub API key
    predicted_price = 150.0  # Example predicted price for AAPL
    stock_symbol = "AAPL"    # Example stock symbol
    
    decision = fetch_stock_news(stock_symbol=stock_symbol,finnhub_api_key=finnhub_api_key)
    print(decision)