# tweet2wallpaper
Sets your desktop wallpaper to a user's recent tweet.

## Dependencies
```
pip install tweepy
pip install Pillow
pip install textwrap3
```
1. You need a twitter API key (bearer_token), in order to run this script.
   - You can get it [here](https://developer.twitter.com/)
2. Fork this Repo & clone it into your local machine
   - cd into tweet2wallpaper folder
3. Open script.py in any editor
   - set **bearer** variable to your **Bearer_token** at line 23.
   - set **username** variable to the one, whose tweets you want to receive.
   - set **wait** variable to your desired value. This checks for new tweet on each loop.
4. Now run script.py
5. This should change your wallpaper with a recent tweet of user. If not, please raise a issue [here](https://github.com/nikhilreddydev/tweet2wallpaper/issues)
