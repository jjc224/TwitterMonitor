# Author:   Joshua Coleman
# Filename: twittermonitor.py
# Purpose of the program: Program monitors tweets for provided handle in command line.

import sys
import json
import time
import GetOldTweets3 as got

def print_user_manual():
    print("-----\t---------------------------\t-----")
    print("*****\tTwitter Monitor Version 1.0\t*****")
    print("-----\t---------------------------\t-----")

def get_handle():
    # Check the count of arguments
    arg_count = len(sys.argv)

    # If missing handle, return error
    if not arg_count == 2:
        stderr("Missing handle, try running the program again like this:\n"
            "$python3 twittermonitor.py <user_handle>")
        return 1

    # Otherwise return the handle as string
    if sys.argv[1]:
        return str(sys.argv[1])

    return 1

def get_latest_tweets(handle, tweets_list):
    # Set criteria for tweet search with GetOldTweets3
    tweetCriteria = got.manager.TweetCriteria().setUsername(handle)\
                                           .setMaxTweets(5)
    # Get tweets                                      
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)

    # Loop throughh new 5 tweets and add them to the list
    for tweet in tweets:
        tweet_formatted = "\n{content} - By {author} @ {time}".format(content=tweet.text, author=tweet.username, time=tweet.date)
        # Print tweet
        print(tweet_formatted)
        # Append new tweet to the list
        tweets_list.append(tweet_formatted)

def main():
    handle = None               # User provided as command line arg
    latest_tweets = None        # Latest 5 Tweets
    tweets_list = []            # List of all tweets collected during execution time for bounus task

    # 1. Print program instructions
    print_user_manual()

    # 2. Get handle
    handle = get_handle()

    # Repeat every 10 min
    while True:    
        # 3. Get and print new 5 tweets and add them to the list
        get_latest_tweets(handle, tweets_list)
        # 4. Sleep for 10 min
        time.sleep(600) # 10 * 60sec


if __name__ == "__main__":
    main()