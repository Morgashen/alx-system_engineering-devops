#!/usr/bin/python3
"""
Using Reddit's API to retrieve hot post titles.
"""

import requests

after = None

def recurse(subreddit, hot_list=[]):
    """
    Recursively retrieves hot post titles from a subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): List to store the hot post titles.

    Returns:
        list: A list of hot post titles, or None if the request fails.
    """
    global after
    user_agent = {'User-Agent': 'api_advanced-project'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'after': after}
    
    try:
        response = requests.get(url, params=parameters, headers=user_agent, allow_redirects=False)
        response.raise_for_status()
    except requests.RequestException:
        return None

    data = response.json().get("data")
    after_data = data.get("after")
    
    if after_data is not None:
        after = after_data
        recurse(subreddit, hot_list)
    
    all_titles = data.get("children")
    for title_ in all_titles:
        hot_list.append(title_.get("data").get("title"))
    
    return hot_list
