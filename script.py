# tweepy is a library to interact with Twitter API
import tweepy

# PIL is a reference to pillow package
# Import Image for basic functionalities like open, save, show
# Import ImageDraw to convert image into editable format
# Import ImageFont to choose the font style
from PIL import Image, ImageDraw, ImageFont

# To break a tweet into multiple lines, each of certain width
import textwrap

# To know the type of current OS
import platform
import time
os = platform.system()
if os == "Windows":
    import ctypes
else:
    import os

# Twitter API key
bearer = "Your_Bearer_token"
username = "naval"
wait = 3600 # secs

# Authentication
api = tweepy.Client(bearer_token=bearer)

# To search @naval tweets, exclude replies & retweets 
query = "from: {} -is:retweet -is:reply".format(username)

def get_new_tweet():
    response = api.search_recent_tweets(query)
    return response.data[0].text

def make_wallpaper(tweet, n):
    # open a template image
    img = Image.open('Background.png')

    # Image is converted into editable form using
    # Draw function and assigned to d1
    d1 = ImageDraw.Draw(img)

    # Font selection from the downloaded file
    myFont = ImageFont.truetype("Fonts/Roboto-Regular.ttf", 64)

    # Add text to image
    width = 230 # x-coordinate of text start
    height = 400 # y-coordinate of text start
    lines = textwrap.wrap(tweet, width=53) # list of lines of tweet
    for line in lines:
        line_width, line_height = myFont.getsize(line)
        d1.text((width, height), line, fill =(0, 0, 0), font=myFont)
        height += line_height

    # new wallpaper image
    new_wallpaper = "Wallpapers/{}.png".format(n)
    img.save(new_wallpaper)
    return new_wallpaper

def set_wallpaper(image):
    if os == "Windows":
        abs_path = r"C:\Users\smart\WorkingOn\tweet2wallpaper\{}".format(image)
        ctypes.windll.user32.SystemParametersInfoW(20, 0, abs_path, 0)
    elif os == "Linux":
        command = r"gsettings set org.gnome.desktop.background picture-uri file:///home/nikhilreddydev/tweet2wallpaper/" + image
        os.system(command)

# getting tweet & setting wallpaper for first time
n = 1
tweet = get_new_tweet()
print("{}. ".format(n) + tweet)
new_wallpaper = make_wallpaper(tweet, n)
set_wallpaper(new_wallpaper)

# check for new tweet every 1 hour
while True:
    time.sleep(wait)
    new_tweet = get_new_tweet()
    # if a new tweet, create a new wallpaper & set it as background
    if  new_tweet != tweet:
        n += 1     
        print("{}.".format(n) + tweet)
        new_wallpaper = make_wallpaper(tweet, n)
        set_wallpaper(new_wallpaper)
    else:
        print("No new tweet")