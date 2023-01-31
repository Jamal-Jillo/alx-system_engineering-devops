#!/usr/bin/python3

""" A function that queries the Reddit API and returns the number of subscribers
for a given subreddit """


def number_of_subscribers(subreddit):
    """ Returns the number of subscribers for a given subreddit """
    import requests

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        return response.json().get('data').get('subscribers')
    elif response.status_code == 404:
        return 0
    else:
        raise Exception('Error: {}'.format(response.status_code))
