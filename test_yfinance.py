import yfinance as yf

def get_stock_data(stock_symbol):
    
    stock = yf.Ticker(stock_symbol)
    data = stock.history(period="30d")
    return data


