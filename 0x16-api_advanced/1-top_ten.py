#!/usr/bin/python3
""" 0x16. API advanced """
from requests import get


def top_ten(subreddit):
    """ Prints the titles of the first 10 hot posts listed for a subreddit """
    top_posts = get('https://api.reddit.com/r/{}/hot'.format(subreddit),
                    headers={'User-Agent': 'FancyRancy'}).json()
    try:
        i = 0
        while (i < 10):
            post = top_posts['data']['children'][i]
            print(post['data']['title'])
            i += 1
    except:
        print(None)
