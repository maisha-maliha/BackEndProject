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

### STEP 1:
Create a .env file and put this code inside. Make sure to put your credentials. Also make sure the .env file is in the root folder where *main.py* exists.

```
DB_USER=root
DB_PASSWORD=YOURPASSWORD
DB_HOST=db               # Set this to 'db' for Docker container communication
DB=newsapi
SECRET_KEY= 'YOUR SECRETKEY'           # openssl rand -hex 32
NEWSAPI_KEY= 'YOUR NEWSAPI.ORG KEY'
MYSQL_ROOT_PASSWORD=yourpassword
```

Generate secret key by typing the follwing in your terminal:
`openssl rand -hex 32`

### STEP 2:
Make sure you have docker installed in you pc. Now you open the docker desktop application if you are in windows.
Make sure you have nothing running in you PORT: `:8000` and `:3307`. Because FastAPI will be running in PORT: 8000 and MySQL will run in PORT:3307.
To check if anything is running in these port, type in you terminal:
`netstat -ano | findstr :8000`

Now you will see if anything is occupying the port. If you get nothing then that means your port is clear. If now then close those applications or change
in your docker-compose.yml file. To stop the application running in port :8000 you type in your terminal
`taskkil /PID /{here you put your the pid number you got in result} /F`

If you want to change docker-compose.yml file then
```
api:
    ports:
      - "8000:8000"
```
change the port number and give whatever you want.
```
api:
    ports:
      - "8500:8000"
```

and now do the above to check for MySQL as well. We are going to run MySQL in PORT: 3307. This shouldnt cause any issue. but if it does then either change the port number.
```
db:
    ports:
      - "3307:3306" 
```
change the number to if you want.
```
db:
    ports:
      - "3377:3306" 
```

now that the project is setup we can now build the whole project and run it.

### STEP 3:
In you terminal run
`docker-compose up --build`

This will take some time and once all is setup. To check if its working visit
`http://localhost:8000/docs`

You should be getting this:
![FastAPI docs](https://raw.githubusercontent.com/maisha-maliha/BackEndProject/refs/heads/master/image.png)

### STEP 4: