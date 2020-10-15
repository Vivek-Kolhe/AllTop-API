import requests
from bs4 import BeautifulSoup

def get_data(category):
    if category == "home":
        url = "https://alltop.com/"
    else:
        url = f"https://alltop.com/{category}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    news_containers = soup.findAll(class_ = "col-xs-12 col-md-4")
    jsonData = {"category" : category, "data" : []}

    for i in range(len(news_containers)):
        news_site_tag = news_containers[i].find("a", style = "color: #ea2f10; font-size: 17px;")        # for news source sites
        news_site = news_site_tag.text
        news_url = news_site_tag["href"]                                                                # news source url

        temp_data = []
        news_items = news_containers[i].findAll(class_ = "one-line-ellipsis")
        for j in range(len(news_items)):
            news_title = news_items[j].text
            url = news_items[j]["href"]
            text = news_items[j]["data-content"].split("<br>")[-1]
            y = text.find("<div")
            content = text[:y]
            if content == "":
                content = None
            temp_data.append({"content" : content, "title" : news_title, "url" : url})
        
        jsonData["data"].append({"newsFrom" : news_site, "newsUrl" : news_url, "newsData" : temp_data})
    return jsonData
