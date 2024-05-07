#!/usr/bin/python3
"""Function to query a list of all hot posts on a given Reddit subreddit."""

import requests

def recurse(subreddit, hot_list=None, after=None):
    """
    Returns a list containing the titles of all hot posts for a given subreddit.
    If the subreddit is invalid or private, returns None.
    """
    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    if after:
        url += f"&after={after}"

    headers = {"User-Agent": "python:MyRedditApp:v1.0 (by /u/your_reddit_username)"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]
        after = data["data"]["after"]

        for post in posts:
            title = post["data"]["title"]
            hot_list.append(title)

        if after:
            hot_list = recurse(subreddit, hot_list, after)

        return hot_list

    elif response.status_code == 302:
        return None
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None
