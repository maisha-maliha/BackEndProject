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

