#!/usr/bin/python3
"""
This module contains a function that queries the Reddit API
and returns the number of subscribers for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    for a given subreddit.

    Args:
    subreddit (str): The name of the subreddit to query.

    Returns:
    int: The number of subscribers. Returns 0 for invalid subreddits.
    """
    # Set a custom User-Agent to avoid Too Many Requests errors
    headers = {'User-Agent': 'MyRedditBot/1.0'}

    # Construct the URL for the subreddit's about.json
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    try:
        # Send a GET request to the Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check if the request was successful and the subreddit exists
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            # If the subreddit is invalid or there's an error, return 0
            return 0
    except requests.RequestException:
        # Handle any request exceptions (e.g., network errors)
        return 0


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        result = number_of_subscribers(sys.argv[1])
        print(result)
