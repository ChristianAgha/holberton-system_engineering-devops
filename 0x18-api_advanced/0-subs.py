#!/usr/bin/python3
""" Get subscribers for subreddit from reddit API """
import requests


def number_of_subscribers(subreddit):
    """ Func Definition """
    url = "https://www.reddit.com/r/" + subreddit + "/about.json"
    req = requests.get(url)

    if req.status_code == 200:
        about = req.json()
        subscibers = about["data"]["subscribers"]
        return(subscibers)
    else:
        return 0
