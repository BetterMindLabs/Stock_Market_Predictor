def predict_stock_trend(data):
    """
    Placeholder that predicts next price as the average of last 5 closing prices.
    """
    if "Close" in data and len(data) >= 5:
        return data["Close"].tail(5).mean()
    return None