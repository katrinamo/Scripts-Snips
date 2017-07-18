# Author: Katie Long
# Description: Figure out who follows you back. If they don't follow back, you
#               have an option to unfollow. Doesn't support batch unfollowing
#               or unfollowing of those not on the list.
# Based on scripts by jamiesonbecker (http://pastebin.com/CxUDMtMi) & audreyr
# (https://github.com/audreyr/tweepy-utils/blob/master/scripts/unfollow-nonfollowers.py)

import tweepy
import time
import sys


def main():
    auth = tweepy.auth.OAuthHandler(
            consumer_key='key',
            consumer_secret='secret')
     
    auth.set_access_token('token', 'secret')
 
    api = tweepy.API(auth_handler=auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    me = api.me()
    print "Followers of",me.screen_name, ":"
    print "(You have", me.followers_count, "followers)"
 
    follows = [followers for followers in tweepy.Cursor(api.followers).items()]
    answer = raw_input( "Would you like to view followers? [Y/n] " ).lower()
    
    if answer == "y":
        for f in follows:
            print "\t%s" % f.screen_name

    print "You have", me.friends_count, "friends"
    friends = [fr for fr in tweepy.Cursor(api.friends).items()]
    answer = raw_input( "Would you like to view friends? [Y/n] " ).lower()
    if answer == "y":
        for fr in friends:
            print "\t%s" % fr.screen_name
           
    friends_d = {}
    for friend in friends:
        friends_d[friend.id] = friend
    follower_d = {}
    for follower in follows:
        follower_d[follower.id] = follower
    
    nonfriend = []
    for friend in friends_d:
        if friend not in follower_d:
            nonfriend.append(friend)
    print "%d people do not follow you back." % len(nonfriend)
    for sad in nonfriend:
        u = api.get_user(sad)
        print "\t%s" % u.screen_name

    quit = False
    while quit == False:
        usrIn = raw_input( "Would you like to unfollow one of the above? \n(Y)es (Q)uit: ").lower()
        if usrIn == "q":
            quit = True
        else:
            toUnfollow = raw_input( "Enter the username of the person to unfollow: ")
            if toUnfollow in nonfriend:
                tU = api.get_user(toUnfollow)
                tU.unfollow()
                print "%s was unfollowed." % tU.screen_name
            else:
                print "This program doesn't support unfollowing those not in the above list (functionally or mo    rally) :("      
    print "Thanks for using!"
    return
main()
