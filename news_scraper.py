import sys
import requests
import pandas as pd
from bs4 import BeautifulSoup
import json
import random
from configs import config
import logging
import pymongo
import dns

class NewsScraper():

    def __init__(self):
        
        self.base_url = config['BASE_URL']
        self.api_key = config['API_KEY']

    def get_cmd_input(self):
        params = list(sys.argv)
        return params[1:]


    def fetch_data(self):
        client = pymongo.MongoClient(config['MONGO_STR'])
        db = client['python-news']
        coll = db['scrape-news']
        print("Collection:", coll)

        # headers = {
        #     'X-Api-Key' : self.api_key
        # }

        # params = self.get_cmd_input()
        # data = {
        #     'q' : " ".join(params)
        # }

        # url = self.base_url + '/v2/everything?q=' + data['q'] + '&apiKey=' + self.api_key
        # try:
        #     news_response = requests.get(url = url, headers=headers, data=json.dumps(data), verify=False)
        #     new_json = news_response.json()
        #     articles = new_json['status']['articles']

        #     if new_json['status'] == 'ok':
                
        #         for article in articles:
        #             data = {}
                    
        #             data['headline'] = articles['title']
        #             data['link'] = articles['url']
        #             data['summary'] = articles['description']

        # except Exception as e:
        #     print("Fetch news error:" , e)

