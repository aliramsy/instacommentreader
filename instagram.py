from datetime import datetime
from itertools import dropwhile, takewhile
import instaloader


L = instaloader.Instaloader()


USER = ""
PROFILE = USER
L.load_session_from_file(USER)

profile = instaloader.Profile.from_username(L.context, PROFILE)

#likes = set()
#print("Fetching likes of all posts of profile {}.".format(profile.username))
#for post in profile.get_posts():
    #print(post)
    #likes = likes | set(post.get_likes())
    #print(likes)
must_checks = []
with open("must-checks.txt","r") as f:
    allcommenterslist = f.readlines()
    for onecommenter in allcommenterslist:
        newcommenter = onecommenter.replace("\n","")
        must_checks.append(newcommenter)
    

print("Fetching comments of all posts of profile {}.".format(profile.username))
#print(must_checks)
#must_checks = []
comments = set()
num = 0
for post in profile.get_posts():
    #print(post)
    num = num + 1
    comments = set(post.get_comments())
    commenters = []
    for comment in comments:
        
        for item in comment:
            res = isinstance(item, instaloader.structures.Profile)
            if res == True:
                commenters.append(item.username)
    print(f"creating file for post number {num}")
    with open(f"results/{num}.txt", 'w') as f:
        print(f"this is the users who have not commented on post number {num}!:",file=f)
        #print("\n",file=f)
        uncommented = []
        for must_check in must_checks:
            if must_check in commenters:
                pass
            else :
                uncommented.append(must_check)
                #print(f"{must_check} has not commented on post {num}!")
                print(f"{must_check} has not commented on post {num}!", file=f)
        #print("\n",file=f)
        print(f"this is the list of all users who were supposed to comment but have not commented on post {num}",file=f)
        print(uncommented,file=f)
        print(f"this is the list of all users who have commented on post {num}:",file=f)
        #print("\n",file=f)
        print(commenters,file=f)

#print("Fetching followers of profile {}.".format(profile.username))
#followers = set(profile.get_followers())

#ghosts = followers - likes
#print(ghosts)
#for i in ghosts:
    #print(i)
#print("Storing ghosts into file.")
#with open("inactive-users.txt", 'w') as f:
    #for ghost in ghosts:
        #print(ghost.username, file=f)


