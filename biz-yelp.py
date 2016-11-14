# Working with the yelp api to get info on businesses. 
import json
import requests
from requests_oauthlib import OAuth1          # https://github.com/requests/requests-oauthlib

# yelp requires OAuth 
consumerkey	= 'pnh2hlN4kBDkaf4TCCHX0Q'
consumersecret ='hjng3Z0Q33vyvq999tvD0sUkVnY'
token =	'K6RXGvphNoTZdkI-kyeXFEPYa6Uippck'
tokensecret ='lh2UsKGzs0i-0vWhRVm4nF0aib8'

def search_bizna(term, location):
    url = 'https://api.yelp.com/v2/search'
    args = {
        "term" : term,
        "location": location
    }
    authorize = OAuth1(consumerkey, consumersecret, token, tokensecret)
    r = requests.get(url, auth=authorize, params=args)
    return r.json()

finder = search_bizna('food', 'newyork')
for i in finder["businesses"]:
    print(i["name"])