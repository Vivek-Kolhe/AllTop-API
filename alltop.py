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
    newsDictionary = {"category" : category, "data" : []}

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
        
        newsDictionary["data"].append({"newsFrom" : news_site, "newsUrl" : news_url, "newsData" : temp_data})
    newsDictionary["count"] = len(newsDictionary["data"])
    return newsDictionary

def viral():
	data = []
	for page in range(1, 4):                                                                            # for fetching articles from only 3 pages
		url = f"https://alltop.com/viral/page/{page}"
		response = requests.get(url)
		soup = BeautifulSoup(response.text, "html.parser")
		articles = soup.findAll(class_ = "row-fluid row-featured")
		for i in range(len(articles)):
			title = articles[i].find(class_ = "post-title").text
			posted = articles[i].find(class_ = "posted-by").text
			posted = posted.split(" / ")
			posted_by, posted_on = posted[0][10:], posted[-1]
			thumbnail = articles[i].find("img")["src"]
			content = articles[i].find("p").text
			readmore = articles[i].find(class_ = "read-more")["href"]

			data.append({"content" : content, "title" : title, "postedBy" : posted_by, "postedOn" : posted_on, "thumbnail" : thumbnail, "readMoreUrl" : readmore})

	articleDictionary = {"category" : "viral", "articleCount" : len(data), "data" : data}
	return articleDictionary
