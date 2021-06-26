import sys
import requests
from datetime import date, time, timedelta
import json
import random
from configs import config
from utils import logging as log
import pymongo
import dns

class NewsScraper():

    def __init__(self):
        
        self.base_url = config['BASE_URL']
        self.api_key = config['API_KEY']

    def get_cmd_input(self):
        params = list(sys.argv)

        if len(params) == 2:
            params = params[1].split(",")
            return params
            
        return params[1:]


    def fetch_data(self):
        # client = pymongo.MongoClient(config['MONGO_STR'])
        # db = client['python-news']
        # coll = db['scrape-news']
        # print("Collection:", coll)

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

                    try:
                        # coll.update(article_data)
                        log.info('Article added %s', article_data)
                    except Exception as e:
                        log.warning('Article not saved %s', e)

            else:
                print("No revelant news with the corresponding keywords. Please try again.")                

        except Exception as e:
            log.warning('Fetch news error %s', e)  

