#!/usr/bin/python3

""" 2. Recurse it!
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """ Queries the Reddit API and returns a list containing the titles of
        all hot articles for a given subreddit. If no results are found for
        the given subreddit, the function should return None.
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
    params = {'after': after}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        after = data.get('data').get('after')
        for child in data.get('data').get('children'):
            hot_list.append(child.get('data').get('title'))
        if after is not None:
            recurse(subreddit, hot_list, after)
        return hot_list
    else:
        return None
