#!/usr/bin/python3

"""
prints the titles of the first 10 hot posts listed for a given subreddit
"""
import requests

def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts for a given subreddit.
    If the subreddit is invalid or private, prints None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "python:MyRedditApp:v1.0 (by /u/your_reddit_username)"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return

    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]
        for post in posts:
            title = post["data"]["title"]
            print(title)
    elif response.status_code == 302:
        print(None)
    else:
        print(f"Error: {response.status_code} - {response.text}")
