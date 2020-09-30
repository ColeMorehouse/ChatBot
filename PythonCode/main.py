import praw

reddit = praw.Reddit(client_id = 'aFAU9vtHS4EJNQ',
                     client_secret = 'Dr2UM_C-F8YBR-b3IwuiklJEpVY',
                     username = 'Coletana',
                     password = 'Tetradigm1!',
                     user_agent = 'chatbot by cole'
                     )

subreddit = reddit.subreddit('words')

keyphrase = '!Coletana'

for comment in subreddit.stream.comments():
    if keyphrase in comment.body:
        comment.reply("Summoned")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
