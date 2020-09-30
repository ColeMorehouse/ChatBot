import praw

#Want to see if this works? Send a message to /u/Coletana

reddit = praw.Reddit(client_id = 'aFAU9vtHS4EJNQ',
                     client_secret = 'Dr2UM_C-F8YBR-b3IwuiklJEpVY',
                     username = 'Coletana',
                     password = 'Tetradigm1!',
                     user_agent = 'chatbot by cole'
                     )

subreddit = reddit.subreddit('words')

keyphrase = '!Colebot'

counter = 0
for message in reddit.inbox.unread():
    print(message.body)
    counter+=1
    message.reply("Hello, this is a reply")
print(counter)