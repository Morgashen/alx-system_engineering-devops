#!/usr/bin/python3
"""
Prints the titles of the first 10 hot posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first
    10 hot posts listed for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
    
    Returns:
        None: Prints the titles of the hot posts or "None" if the subreddit is invalid.
    """
    if not subreddit or not isinstance(subreddit, str):
        print("None")
        return

    user_agent = {'User-Agent': 'api_advanced_project'}
    params = {'limit': 10}
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)

    try:
        response = requests.get(url, headers=user_agent, params=params, allow_redirects=False)
        response.raise_for_status()

        results = response.json()
        posts = results.get('data', {}).get('children', [])

        if not posts:
            print("None")
            return

        for post in posts:
            print(post.get('data', {}).get('title', 'None'))

    except requests.RequestException:
        print("None")
