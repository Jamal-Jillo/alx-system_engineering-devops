#!/usr/bin/python3

"""
Function that queries the Reddit API and prints the titles.

of the first 10 hot posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """Function that queries the Reddit API and prints the titles."""

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        for i in range(10):
            print(response.json().get('data').get('children')[i].get('data')
                  .get('title'))
    else:
        print("None")
