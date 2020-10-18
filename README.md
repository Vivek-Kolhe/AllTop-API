## What is AllTop.com?
[AllTop](https://alltop.com) aggregates all of the top news and information in real time.

## [Unofficial] AllTop API
This API is capable of fetching news from various sources as fetched by [AllTop](https://alltop.com).

## Dependencies
- Requests\
  ```pip3 install requests```
  
- BeautifulSoup4\
  ```pip3 install beautifulsoup4```
  
- Flask\
  ```pip3 install flask```

- Flask-Cors\
  ```pip3 install Flask-Cors```
  
## Available News Topics
- **Home**
  - home (fetches news from the homepage of [AllTop](https://alltop.com).)
  
- **News**
  - news
  - politics

- **Tech**
  - tech
  - cryptocurrency
  - apple
  - android
  - linux
  - ecommerce
  
- **Sports**
  - sports

- **Entertainment**
  - celebrity
  - funny
  - videos
  - gaming
  - television
  - movies
  - music
  - social-media

- **Lifestyle**
  - health
  - fitness
  - travel
  - beauty
  - homes
  - food
  - deals
  - photography
  - lifehacks
  - astrology

- **Business**
  - business
  - personal-finance
  - seo

- **Others**
  - education
  - autos
  - formula-1
  - science
  - religion
  
## Usage
The API is available at\
```https://alltopapi.herokuapp.com/```

Make a get request by specifying the topic of news you want\
```https://alltopapi.herokuapp.com/news?topic={topic_name}```\
Example - https://alltopapi.herokuapp.com/news?topic=gaming

To fetch viral articles from the site, make a get request to\
```https://alltopapi.herokuapp.com/viral```

## Sample Outputs
- **For topic wise news**
  ```
  {
  "category" : "home",
  "count" : 1,
  "data" : [
    "newsData" : [
    {
      "content" : "Welcome back to The TechCrunch Exchange, a weekly startups-and-markets newsletter for your weekend enjoyment. There was a steady drumbeat of bullish news for unicorns this week",
      "title" : "VCs reload ahead of the election as unicorns power ahead",
      "url" : "https://feedproxy.google.com/~r/Techcrunch/~3/fowIMj1hQdw/"
    }],
    "newsFrom" : "TechCrunch",
    "newsUrl" : "http://techcrunch.com"]
  }
  ```

- **For articles**
  ```
  {
  "articleCount" : 1,
  "category" : "viral",
  "data" : [
     {
      "content" : "YouTube is banning all QAnon related content, as well as conspiracy content that targets individuals. With barely two weeks until the presidential election, will this be a case of “better late than never” or “a day late and a buck short?” Perhaps every little bit helps slow down the craziness, but will it be enough? …",
      "postedBy": "\nThomas Bush",
      "postedOn": "October 16, 2020 ",
      "readMoreUrl": "https://alltop.com/viral/youtube-bans-qanon",
      "thumbnail": "https://alltop.com/viral/wp-content/uploads/2020/10/sgsdfsdeeee4-2020-10-15T163612.659.png",
      "title": "YouTube bans QAnon"
      }
    ]
  }
  ```
  
  ## Setup
  Install the above listed dependencies and start the server by running **app.py**.
  
  ## Deploying on Heroku
  - Make sure you've installed HerokuCLI and cloned the repository.
  - Create an app from heroku dashboard and run the following commands one by one.
    ```
    $ heroku login
    $ git init
    $ heroku git:remote -a <your_appname>
    $ git add .
    $ git commit -am "deploying"
    $ git push heroku master
    ```

***Note:*** *Before running second command make sure you're in the directory where all the repo files are present.*
