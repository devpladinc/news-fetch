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
- **MongoDB Atlas account (Cloud version)**
- **pip**

##### Installation

1. `git clone` - [News scraper](https://github.com/devpladinc/news-fetch.git)
2. Create virtual environment `python -m virtualenv (environment-name)`
3. Install packages - `pip install -r requirements.text`

##### How to use script
Simply type `python main.py` and add the keywords and/or categories of news you wanted to scrape.

#### Example
```python
python main.py finance bitcoin texas
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





