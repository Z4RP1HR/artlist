import requests
from bs4 import BeautifulSoup

def search_articles(topic):
    url = f"https://www.google.com/search?q={topic}&tbm=nws"
    headers = {'User-Agent': 'Mozilla/5.0'}
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    articles = soup.find_all('div', class_='dbsr')
    results = []
    for article in articles:
        title = article.find('div', class_='JheGif nDgy9d').get_text()
        link = article.find('a')['href']
        source = article.find('div', class_='XTjFC WF4CUc').get_text()
        results.append({'title': title, 'link': link, 'source': source})
    return results

topic = input("Enter a topic: ")
articles = search_articles(topic)
print(f"Articles related to {topic}:")
for i, article in enumerate(articles):
    print(f"{i+1}. {article['title']}")
    print(f"   Source: {article['source']}")
    print(f"   Link: {article['link']}")
