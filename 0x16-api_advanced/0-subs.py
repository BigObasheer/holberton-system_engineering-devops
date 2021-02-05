#!/usr/bin/python3
""" 0x16. API advanced """
from requests import get


def number_of_subscribers(subreddit):
    """ Return number of subs a subreddit has """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    sub = get(url, allow_redirects=False, headers={'User-agent': ''}).json()

    sub_count = sub['data']['subscribers'] if 'data' in sub else 0

    return sub_count
