import streamlit as st
from sentiment_analysis import analyze_sentiment
from test_yfinance import get_stock_data
from news_api import get_news
from stock_prediction import predict_stock_trend
st.title(":chart_with_upwards_trend: Stock Insights Dashboard")
stock_symbol = st.text_input("Enter Stock Symbol (e.g., AAPL):", "AAPL")
if st.button("Get Stock Data"):
    st.subheader(f"Stock Data for {stock_symbol}")
    stock_data = get_stock_data(stock_symbol)
    if stock_data is not None:
        st.line_chart(stock_data["Close"])
        predicted_price = predict_stock_trend(stock_data)
        if predicted_price:
            st.success(f":bar_chart: Predicted Next Day Price: ${predicted_price:.2f}")
    else:
        st.error(":warning: Could not fetch stock data.")
if st.button("Get Stock News"):
    st.subheader(f"News for {stock_symbol}")
    news_articles = get_news(stock_symbol)
    if news_articles:
        for article in news_articles[:5]:
            sentiment_score = analyze_sentiment(article["description"] or "")
            sentiment_label = "Positive" if sentiment_score > 0 else "Negative" if sentiment_score < 0 else "Neutral"
            st.write(f"**{article['title']}**")
            st.write(f":newspaper: {article['description']}")
            st.write(f":memo: Sentiment: {sentiment_label} (Score: {sentiment_score:.2f})")
            st.write("---")
    else:
        st.error(":warning: No news articles found.")