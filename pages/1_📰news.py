import streamlit as st
import requests

NEWS_API_KEY = f"https://newsapi.org/v2/everything?domains=wsj.com&apiKey=422c54e38f88485aae9c12296a8fdc6c"

def get_news():
    url = f"https://newsapi.org/v2/everything?domains=wsj.com&apiKey=422c54e38f88485aae9c12296a8fdc6c"
    response = requests.get(url)
    data = response.json()
    if "articles" in data:
        articles = data["articles"]
        return articles
    else:
        return []

def display_articles(articles):
    if not articles:
        st.write("No articles found.")
    else:
        for article in articles:
            st.subheader(article["title"])
            st.image(article["urlToImage"])
            st.write(article["description"])
            st.write("Source:", article["source"]["name"])
            st.write("Published at:", article["publishedAt"])
            st.write("Read more:", article["url"])
            st.markdown("---")

# Streamlit App
st.title("Latest News")
articles = get_news()
display_articles(articles)


