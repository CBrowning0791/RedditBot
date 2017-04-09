#This bot should reply to anyone saying sauce and reply only nine more seasons, in reference to the Rick and Morty April's fool day episode
import praw
import pdb
import re
import os
import time
bot = praw.Reddit(user_agent='Szechuan_Sauce_Bot v0.1', client_id='ClientIFHere',client_secret='ClientSecretHere', username='Szechuan_Sauce_Bot',password='Passwordhere')
if not os.path.isfile("I_replied_to.txt"):#checking for the file first, if found load from it, if not create
    I_replied_to =[]
else:
    with open("I_replied_to.txt", "r") as f:
        I_replied_to = f.read()
        I_replied_to = I_replied_to.split("\n")
        I_replied_to = list(filter(None, I_replied_to))


mySubreddit = bot.subreddit('Menthro+mwo')
myComments = mySubreddit.stream.comments()
for comment in myComments:
    text = comment.body
    author = comment.author
    if comment.id not in I_replied_to and comment.is_root == True:
        if 'sauce' == text.lower() or 'sauce?' == text.lower():
            I_replied_to.append(comment.id)
            message = "*uurrrpp* Nine more seasons, u/{0}, then we get our sauce!".format(author)
            comment.reply(message)
            with open("I_replied_to.txt", "w") as f:
                for comment_id in I_replied_to:
                    f.write(comment_id + "\n")
                print("I made a comment boss")
                print("Going to sleep for ten minutes boss")
                time.sleep(600)

        if 'PGI' in text:
            I_replied_to.append(comment.id)
            message = "PGI? *tttthhhhhpppppphhhhhtttttt".format(author)
            comment.reply(message)
            with open("I_replied_to.txt", "w") as f:
                for comment_id in I_replied_to:
                    f.write(comment_id + "\n")
                print("I made a rasberry boss")
                print("Going to sleep for ten minutes boss")
                time.sleep(600)
    print("I looped boss")