# Chirp tiny  Social App
# Backend Engineering  Assessment_2

users = {}
posts = {}

# CREATE USER FUNCTION

def create_user(username):
    username = username.strip().lower()

    if username == "":
        return {"ok" : False,
                "error" : "username cannot be empty."}
    
    if username in users:
        return {"ok" : False,
                "error" : f"User '{username}' already exists."}
    
    users[username] = {"following" : []}

    return {"ok" : True,
            "user" : username}

# TESTING THE CREATE USER FUNCTION
print(create_user("Obasi"))
print(create_user("Sunday"))
print(create_user("Omotosho"))


# CREATE POST FUNCTION

def create_post(username, text):
    username = username.strip().lower()
    text = text.strip()

    if username not in users:
        return{"ok" : False,
               "error" : f"User '{username}' does not exist."}
    
    if text == "":
        return {"ok" : False,
                "error" : "post text cannot be empty."}
    
    post_id = len(posts) + 1

    posts[post_id] = {
        "author" : username,
        "text" : text,
        "likes" : 0}
    
    return {
        "ok" : True,
        "post" : {
            "id" : post_id,
            **posts[post_id]}}

# TESTING THE CREATE POST FUNCTION

print(create_post("Obasi", "Happy to be on Chirp!"))
print(create_post("Omotosho", "Chirp is the App to beat!"))
print(create_post("Sunday", "Let us learn and use python"))

                  



# LIKE POST FUNCTION

def like_post(post_id):
    try:
        post_id = int(post_id)

    except ValueError:
        return{"ok" : False,
               "error" : "post ID must be a number."}
    
    if post_id not in posts:
        return{"ok" : False,
               "error" : "post not found."}
    
    posts[post_id]["likes"] += 1
    return{"ok" : True, 
           "post" : {
               "id" : post_id, **posts[post_id]}}

# TESTING THE LIKE POST FUNCTION

print(like_post(1))
print(like_post(1))
print(like_post(3))

# FOLLOW USER FUNCTION

def follow (follower, followee):

    follower = follower.strip().lower()
    followee = followee .strip() .lower()

    if follower not in users or followee not in users:
        return {"ok" : False,
                "error" : "one or both users do not exist."}
    
    if follower == followee:
        return {"ok" : False,
                "error" : "You cannot follow yourself."}
    
    if followee in users[follower]["following"]:
        return {"ok" : False,
                "error" : f"{follower} already follows {followee}."}
    
    users[follower]["following"] .append(followee)

    return {
        "ok" : True,
        "follower" : follower,
        "following" : users[follower]["following"]
    }

# TESTING THE FOLLOW USER FUNCTION
print(follow("Obasi", "Sunday"))
print(follow("Obasi", "Omotosho"))


# UNFOLLOW USER (AN OPTIONAL FUNCTION)

def unfollow (follower, followee):
    follower = follower . strip() . lower()
    followee = followee . strip() . lower()

    if follower not in users or followee not in users:
        return {"ok" : False,
                "error" : "one or both users do not exist."}
    
    if followee not in users[follower]["following"]:
        return {"ok" : False,
                "error" : f"{follower} is not following {followee}."}
    
    users[follower]["following"] .remove(followee)
    
    return {
        "ok" : True,
        "follower" : follower,
        "following" : users[follower]["following"]}

# TESTING THE UNFOLLOW USER FUNCTION

print(unfollow("Obasi", "Sunday"))

    

# GET PROFILE FUNCTION

def get_profile (username):
    username = username .strip() .lower()
    if username not in users:
        return {
            "ok" : False,
            "error" : "user does not exist."
        }
    
    user_posts = []

    for post_id, post in posts.items():

        if post["author"] == username:
            user_posts .append({"id" : post_id, **post})
    return {
        "ok" : True,
        "profile" : {"username" : username,
                     "following" : users[username]["following"],
                     "posts" : user_posts}
    }

# TESTING THE GET PROFILE FUNCTION
print(get_profile("Obasi"))

# GET FEED FUNCTION

def get_feed (username):

    username = username .strip() .lower()

    if username not in users:
        return {
            "ok" : False,
            "error" : "User not found."
        }
    feed = []

    following = users[username]["following"]

    for post_id, post in posts.items():
        if post["author"] in following:

            feed.append({
                "id" : post_id, **post
            })
    return{
            "ok" : True, "feed" : feed}

# TESTING THE GET FEED FUNCTION

print(get_feed("Obasi"))

# DELETE POST FUNCTION (OPTIONAL)

def delete_post(post_id):

    try:
        post_id = int(post_id)

    except ValueError:
        return {
            "ok" : False,
            "error" : "post ID must be a number."}
    
    if post_id not in posts:
        return {"ok" : False,
                "error" : "post not found,"}
    
    deleted = posts.pop(post_id)

    return {
        "ok" : True,
        "deleted_post" : {
            "id" : post_id, **deleted}}
        
    
                   
    
# TESTING THE DELETE POST FUNCTION

print(delete_post(2))
print(delete_post(2))


# SEARCH POSTS FUNCTION (OPTIONAL)

def search (term):

    term = term . strip() . lower()

    results = []

    for post_id, post in posts.items():

        if term in post["text"].lower():
            results.append({
                "id" : post_id, **post})
    
    return {
        "ok" : True,
        "results" : results}

# TESTING THE SEARCH POST FUNCTION

print(search("python"))
    

        
                

# TRENDING POSTS

def trending (n=6):

    ranking = []

# turples are used because they are ideal for sorting
# each turples stores likes, post_id

    for post_id, post in posts.items():
        ranking.append((post["likes"], post_id))

        ranking.sort(reverse = True)

        trending_posts = []

        for likes, post_id in ranking[ :n]:
            trending_posts.append({
                "id" : post_id, **posts[post_id]})
            
    return {"ok" : True,
            "trending" : trending_posts,
            "reason" : (
                "a list of tuples (likes, post_id is used because tuples)"
                "are lightweight and python naturally sorts them by the"
                "first value (likes), making ranking to be efficient.")}
                


# TESTING THE TRENDING FUNCTION

print(trending())
