import sys
import requests
from datetime import date, time, timedelta
import json
import random
from configs import config
from utils import logging as log
import pymongo
import dns
import re

class NewsScraper():

    def __init__(self):
        
        self.base_url = config['BASE_URL']
        self.api_key = config['API_KEY']

    def get_cmd_input(self):
        params = list(sys.argv)
        print(len(params))

        if len(params) == 2:
            params = params[1].split(",")
            return params

        if len(params) == 1:
           category = input("Category:")
           location = input("Location:") 
           new_params = []
           new_params.append(category)
           new_params.append(location)
           return new_params

        return params[1:]



    def fetch_data(self):
        # connection via cloud
        try:
            client = pymongo.MongoClient(config['MONGO_STR'])
            db = client['python-news']
            coll = db['scrape-news']
        except Exception as e:
            log.warning('DB connection error %s', e)    

        headers = {
            'X-Api-Key' : self.api_key
        }

        params = self.get_cmd_input()        
        data = {
            'q' : " ".join(params)
        }

        url = self.base_url + '/v2/everything?q=' + data['q'] + '&apiKey=' + self.api_key
        try:
            news_response = requests.get(url = url, headers=headers, data=json.dumps(data), verify=False)
            new_json = news_response.json()

            articles = new_json['articles']

            if new_json['status'] == 'ok':
                
                for article in articles:
                    article_data = {}
                    
                    article_data['headline'] = article['title']
                    article_data['link'] = article['url']
                    article_data['summary'] = article['description']

                    log.info("Data: %s", article_data)
                    try:
                        coll.insert_one(article_data)
                        log.info('Article added %s', article_data)
                    except Exception as e:
                        log.warning('Article not saved %s', e)

            else:
                print("No revelant news with the corresponding keywords. Please try again.")
                log.info("No news match %s", params)                

        except Exception as e:
            log.warning('Fetch news error %s', e)
