#!/usr/bin/python3
""" Returns a list of all hot articles for a given subreddit """
import requests


def recurse(subreddit, hot_list=[], after=""):
    """ Func Def """
    url = "https://www.reddit.com/r/" + subreddit + "/hot.json" +\
          "?after=" + after
    user_agent = {'User-agent': 'Christian'}
    req = requests.get(url, headers=user_agent, allow_redirects=False)

    if req.status_code == 200:
        about = req.json()
        hot_posts = about["data"]["children"]
        after = about["data"]["after"]
        for post in hot_posts:
            hot_list.append(post["data"]["title"])
        if (after):
            recurse(subreddit, hot_list, after)
        return(hot_list)
    else:
        return None
