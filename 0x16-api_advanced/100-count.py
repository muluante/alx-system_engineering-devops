#!/usr/bin/python3
"""
    Queries Reddit's API to print the number of occurences specified words in
    all the hot posts for a given subreddit.
"""


import requests

def count_words(subreddit, word_list, after=None, word_counter={}):

  try:
    # API request
    
  except Exception as e:
    print(f"Error: {e}")
  
  else:
    if resp.status_code == 200:

      data = resp.json()
      
      if 'data' in data:
        children = data['data']['children']

        for post in children:
          
          title = post['data']['title']

          if title:

            # Count frequencies
              
    else:
      # Recursive call
      count_words(subreddit, word_list, after, word_counter)

  # Print words and frequencies
