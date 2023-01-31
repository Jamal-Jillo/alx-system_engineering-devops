#!/usr/bin/python3

""" 100. Count it!
"""

import requests


def count_words(subreddit, word_list, hot_list=[], after=None):
    """ Queries the Reddit API, parses the title of all hot articles, and
        prints a sorted count of given keywords (case-insensitive, delimited
        by spaces. Javascript should count as javascript, but java should not).
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
    params = {'after': after}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        return None
    data = response.json()
    for post in data['data']['children']:
        hot_list.append(post['data']['title'])
    after = data['data']['after']
    if after is None:
        word_dict = {}
        for word in word_list:
            word_dict[word] = 0
        for title in hot_list:
            for word in word_list:
                word_dict[word] += title.lower().split().count(word.lower())
        for word in sorted(word_dict, key=word_dict.get, reverse=True):
            if word_dict[word] > 0:
                print('{}: {}'.format(word, word_dict[word]))
    else:
        count_words(subreddit, word_list, hot_list, after)
