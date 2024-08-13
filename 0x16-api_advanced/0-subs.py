#!/usr/bin/python3
"""
Retrieve the number of subscribers for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers for the subreddit, or 0 if the
        subreddit is invalid or an error occurs.
    """
    if not subreddit or not isinstance(subreddit, str):
        return 0

    user_agent = {'User-Agent': 'api_advanced_project'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)

    try:
        response = requests.get(url, headers=user_agent, allow_redirects=False)
        response.raise_for_status()
        results = response.json()
        return results.get('data', {}).get('subscribers', 0)

    except requests.RequestException:
        return 0
