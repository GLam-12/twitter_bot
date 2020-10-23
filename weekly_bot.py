import tweepy
import os
import time

# Authenticate to Twitter
auth = tweepy.OAuthHandler("T0d2VwT3fHGbQp54ZkvhEPmhY", "tc9f46CKzoa1k39BawUqVr5KWOZ88ebEP3oapjxpkqjs4BUjCc")
auth.set_access_token("1319009520849485825-pFSbiB0i9NETgYlfFIAT6isBolWv6T", "XMwOlPW6bRQUZXB85JFB45Du2XX6XsjgfxsYcoBfUqsoE")

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")


os.chdir('weekly')
def post_images():
    filenames = []
    media_ids = []
    for image in os.listdir('.'):
        img = str(image)
        filenames.append(img)
    for filename in filenames:
        upload = api.media_upload(filename)
        media_ids.append(upload.media_id)
    api.update_status(status = 'Top memes of the week!', media_ids = media_ids)

post_images()