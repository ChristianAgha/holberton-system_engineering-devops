#!/usr/bin/python3
""" Prints the titles of the first 10 hot posts of subreddit. """
import requests


def top_ten(subreddit):
    """ Func Def """
    url = "https://www.reddit.com/r/" + subreddit + "/hot.json"
    user_agent = {'User-agent': 'Christian'}
    req = requests.get(url, headers=user_agent)

    if req.status_code == 200:
        about = req.json()
        hot_posts = about["data"]["children"]
        counter = 0
        for post in hot_posts:
            counter += 1
            if counter > 10:
                return
            print(post["data"]["title"])
    else:
        print("None")
