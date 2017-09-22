#!/usr/bin/python3
""" Queries the Reddit API, parses the title of all hot articles """
import requests

def count_words(subreddit, word_list, hot_list=[], after=""):
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
            count_words(subreddit, word_list, hot_list, after)
        else:
            parse_titles(hot_list, word_list)
    else:
        return None

def parse_titles(hot_list, word_list):
    """ Parse the title list """
    d = {}
    for word in word_list:
        count = 0
        for title in hot_list:
            if word.lower() in title.lower():
                count += 1
        d[word] = count
    sorted_d = sorted(d.items(), key=lambda x: x[1], reverse=True)
    for tupl in sorted_d:
        if tupl[1] > 0:
            print("{}: {}".format(tupl[0], tupl[1]))
