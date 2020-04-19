import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("6hugFc6I3FM3IXtkDScwNbynW", "XXsQ02PwGt0ouevudccaGXo69J58q0mNqOQ2Ad39SHAeoQcgQd")
auth.set_access_token("1189423905405992962-BF7bRfN4AR7ebFoGH7ADn7RnkhHDfj", "cBGlW6RVjAAgSFwCYh9d36liMAAi0m4166f7FfSqr9mkR")

# Create API object
api = tweepy.API(auth)

q=input("Enter the number of handles:" )
listhandle=[]

for x in q:
           listhandle.append(input("Enter the handles:" ))

listkword=[]
p=input("Enter the no. of keywords: ")

for x in p:
            listkword.append(input("Enter the keywords:" ))

            for x in listhandle:
	          kword=listkword[x]
	          tweets=api.list_timeline(include_rts=false, owner_id=listhandle[x], exclude_replies=true, count=200)
	          for x in tweets:
		y=tweets[x]
		if y!=kword:
			tweets.remove(x)
	          print(tweets)
