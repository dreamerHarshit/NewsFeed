from newsfeeds import *

if __name__ == "__main__":
    newsfeed = NewsFeed()
    while 1:
        command = str(raw_input("enter your input: \n"))
        command = command.split('~')
        if command[0] == "signup":
            newsfeed.signup(command[1])
        elif command[0] == "login":
            newsfeed.signin(command[1])
        elif command[0] == "post":
            newsfeed.add_post(command[1])
        elif command[0] == "follow":
            newsfeed.follow(command[1])
        elif command[0] == "shownewsfeed":
            newsfeed.show_news_feed()
        elif command[0] == "upvote":
            newsfeed.upvote(command[1])
        elif command[0] == "downvote":
            newsfeed.downvote(command[1])
        elif command[0] == "reply":
            newsfeed.reply(command[1])