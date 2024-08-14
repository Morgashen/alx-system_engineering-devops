#!/usr/bin/python3
"""
Module for querying the Reddit API and printing titles of hot posts.
"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit.

    Args:
    subreddit (str): The name of the subreddit to query.

    Returns:
    None
    """
    # Set a custom User-Agent to avoid Too Many Requests errors
    headers = {'User-Agent': 'MyRedditBot/1.0'}

    # Construct the URL for the subreddit's hot posts
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    try:
        # Send a GET request to the Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check if the request was successful and the subreddit exists
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            
            for post in posts:
                print(post['data']['title'])
        else:
            # If the subreddit is invalid or there's an error, print None
            print(None)
    except requests.RequestException:
        # Handle any request exceptions (e.g., network errors)
        print(None)


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
