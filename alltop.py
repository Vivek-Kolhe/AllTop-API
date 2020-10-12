import requests
from bs4 import BeautifulSoup

def get_data():
    url = "https://alltop.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    news_containers = soup.findAll(class_ = "col-xs-12 col-md-4")
    data = []

    for i in range(len(news_containers)):
        news_site_tag = news_containers[i].find("a", style = "color: #ea2f10; font-size: 17px;")        # for news source sites
        news_site = news_site_tag.text
        news_url = news_site_tag["href"]                                                                # news source url

        temp_data = []
        news_items = news_containers[i].findAll(class_ = "one-line-ellipsis")
        for j in range(len(news_items)):
            news_title = news_items[j].text
            url = news_items[j]["href"]
            temp_data.append({"title" : news_title, "url" : url})
        
        data.append({"newsSite" : news_site, "newsSiteUrl" : news_url, "data" : temp_data})
    return data
