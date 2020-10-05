import praw

import spacy





nlp = spacy.load("en_core_web_md")  # make sure to use larger model!
kin = nlp(input("Enter something"))

tokens = nlp("Hi my name is Cole. Who are you?")
hello = nlp("hello")
where = nlp("where")
who = nlp("who")
why = nlp("why")
how = nlp("how")
bye = nlp("bye")


print(kin.similarity(hello))
print(kin.similarity(bye))



intent = {
    "greeting": False,
    "question": False,
    "statement": False
}


for word in tokens:
    if word.similarity(hello) > 0.7:
        print("greetings")
    if word.similarity(where) > 0.7:
        print("where")

for sentence in tokens.sents:
    print(sentence.text)


#for token1 in tokens:
#    for token2 in tokens:
#        print(token1.text, token2.text, token1.similarity(token2))

'''
nlp = spacy.load('en_core_web_sm')

# Create an nlp object
doc = nlp("He went to play basketball")

# Iterate over the tokens
for token in doc:
    # Print the token and its part-of-speech tag
    print(token.text, "-->", token.pos_)
'''
'''

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
    counter += 1
    message.reply("Hello, this is a reply")
print(counter)
'''
