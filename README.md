### News generator - CLI triggered

###### This small script allows the user to call an API (newsAPI.org) to generate and save relevant news from the CLI argument.
----------

##### Table of Contents
- Requirements and Dependencies
- Installation
- How to use script
- Output

##### Requirements and Dependencies
In order to run the script, you must install the following dependencies first hand:

- **Python 3.6 (or higher)**
- **MongoDB Atlas account and credentials (Cloud version)**
- **pip**
- **API_KEY from NewsAPI.org**

##### Installation

1. `git clone` - [News scraper](https://github.com/devpladinc/news-fetch.git)
2. Create virtual environment `python -m virtualenv (environment-name)`
3. Install packages - `pip install -r requirements.text`

##### How to use script
1. locate `configs.py`, and input the following:
    - API_KEY - from newAPI.org
    - MONGODB_USERNAME, MONGODB_PASSWORD - from mongodb
    - DB_NAME = database name
  
```python
    config = {
    'BASE_URL' : "https://newsapi.org",
    'API_KEY' : <API_KEY>,
    'MONGO_STR' : "mongodb+srv://<MONGODB_USERNAME>:<MONGODB_PASSWORD>@cluster0.v13cn.mongodb.net/<DB_NAME>?retryWrites=true&w=majority"
}
```

1. Simply type `python main.py` and add the keywords and/or categories of news you wanted to scrape.

#### Example 1
```python
python main.py finance bitcoin texas
```

#### Example 2
```python
python main.py food,innovations,california
```

#### Example 3
```python
python main.py
Category: Business
Location: Silicon Valley
```


##### Output
On the backend, the scaper will send an API call to get the news. If relevant news found, there are 2 options to view the saved news.

1. via logs - `new_scrape_log.log`  contains the data saved in the database
2. Mongodb collection - the scraped data will be saved on the indicated database + collection



----------
**Dev: Cha Pladin**
- Tech stack: Python / MongoDB
- Initial creation date: June 26, 2021
- Private script/project





