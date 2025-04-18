# BackEndProject

## Introduction:
This project is a built using FastAPI and MySQL. In this project I have used thirdparty API named [News API](https://newsapi.org/). 

The following API end points were implemented in FastAPI:

* GET /news: Fetch all news with pagination support.

* POST /news/save-latest: Fetch the latest news and save the top 3 into a database.

* GET /news/headlines/country/{country_code}: Fetch top headlines by country.

* GET /news/headlines/source/{source_id}: Fetch top headlines by source.

* GET /news/headlines/filter: Fetch top headlines by filtering both country and source (use query parameters country and source). 

Schemas have been created to save articles in database. 


## Setup Instruction:
Create a .env file and put this code inside. Make sure to put your credentials. Also make sure the .env file is in the root folder where *main.py* exists.

```
DB_USER = 'your username'
DB_PASSWORD = 'your password'
DB_HOST = '127.0.0.1'
DB = 'newsapi'
SECRET_KEY = 'generate secret key'
NEWSAPI_KEY = 'your_newsapi.org_key'
```

Generate secret key by typing the follwing in your terminal:
`openssl rand -hex 32` 