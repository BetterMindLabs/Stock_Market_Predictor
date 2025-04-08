import requests

def get_news(stock_symbol):
    api_key = "a37c0b3268384a70ac0104dfffa36965"
    url = f'https://newsapi.org/v2/everything?q={stock_symbol}&apiKey={api_key}'
    response = requests.get(url)
    news_data = response.json()

    articles = [{"title": article["title"], "description": article["description"]} 
                for article in news_data.get("articles", [])]
    return articles