#Super Simple, does nothing but get the users comment karma
#Note, as of 03/08/2015 this should stop working, as the Reddit api will be entirely OAUTH from that date. I might fix this to use OAUTH, but unfortunately I have a deepseated hatred for OAUTH.

import praw

reddit = praw.Reddit("KrismazBot")

reddit.login()

print(reddit.user.comment_karma)