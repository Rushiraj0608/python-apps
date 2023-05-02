from flask import Flask, request
import secrets
from secrets import randbelow
from datetime import datetime
import string
from threading import Lock
import json

app = Flask(__name__)

with open("posts.json","r") as f:
    postFile = f.read()

with open("users.json","r") as f:
    userFile = f.read()

# print(postFile)
f.close()
posts = json.loads(postFile)
users = json.loads(userFile)
lock = Lock()

print(posts)

@app.post("/user")
def create_user():
    o = request.get_json(force=True)

    user_email = o.get("user_email", None)
    user_firstname = o.get("user_firstname", None)
    user_lastname = o.get("user_lastname", None)

    # Generate a new user id and private key
    alpha = string.ascii_letters
    random_string = []
    for i in range(10):
        random_string += secrets.choice(alpha)
    user_id = "".join(random_string)
    user_key = secrets.token_hex(16)
    with lock:
        for i in range(len(users)):
            if user_email in i["user_email"]:
                return {"err": "email already exists"}, 400

        # Add the user to the users dictionary
        users[user_id] = {"user_id":user_id,"user_key":user_key, "user_email":user_email, "user_firstname":user_firstname, "user_lastname":user_lastname}

    print(users,"users in post request")
    return {"user_id": user_id, "user_key": user_key}


@app.patch("/user/<user_id>")
def update_user(user_id):
    
    o = request.get_json(force=True)

    user_email = o.get("user_email", None)
    user_firstname = o.get("user_firstname", None)
    user_lastname = o.get("user_lastname", None)

    print(users,"user")
    print(user_email,user_firstname,user_lastname)
    values = users.get(user_id)
    if user_id not in users:
        return {"err": "user not found"}, 404

    if user_email is None and user_firstname is None and user_lastname is None:
        return {"err": "need a field to update"}, 400

    if user_firstname is not None:
        if isinstance(user_firstname, str) is False:
            return {"err": "firstname must be a string"}, 400

    if user_lastname is not None:
        if isinstance(user_lastname, str) is False:
            return {"err": "lastname must be a string"}, 400

    with lock:
        if user_firstname is not None:
            print("in user>patch>fn")
            # print(users[user_id][user_firstname],"id")
            # print(users["user_id"][user_firstname],"bfsbkjv")
            users[user_id]["user_firstname"] = user_firstname
            # users[user_id] = {user_key, user_email, user_firstname, user_lastname}
            # values.remove()

        if user_lastname is not None:
            users[user_id]["user_lastname"] = user_lastname
            # users[user_id] = {user_key, user_email, user_firstname, user_lastname}

    return users[user_id]


@app.post("/post")
def post():
    print("in post")
    o = request.get_json(force=True)

    msg = o.get("msg", None)
    print(msg)
    user_id = o.get("user_id", None)
    user_key = o.get("user_key", None)

    print(msg, user_id, user_key)
    if user_id is not None:
        print(users[user_id]["user_id"],user_id,"user id n.df v, xc")
        # if user_id not in users[user_id]["user_id"]:
        if not users[user_id]["user_id"]:    
            print("dsv hbdkjsn     jkfnjklc")
            return {"err": "user not found"}, 404
    if user_key is not None:
        # print(users[user_key],"bsdckn")
        # if user_key != users[user_id]:
        if not users[user_id]["user_key"]:
            if not user_key == users[user_id]["user_key"]:
                return {"err": "incorrect user key"}, 403

    if msg is None:
        return {"err": "need a message"}, 400

    if isinstance(msg, str) is False:
        return {"err": "message must be a string"}, 400

    alpha = string.ascii_letters
    random_string = []
    for i in range(10):
        random_string += secrets.choice(alpha)

    key = "".join(random_string)

    timestamp = datetime.now().isoformat()

    with lock:
        id = randbelow(1000000)
        print(user_id,user_key,"sdfghjkl;8754")
        if user_id is None or user_key is None:
            print("in if>post")
            posts[id] = {"id": id, "key": key, "timestamp": timestamp, "msg": msg}
            # posts.append({id:{"id": id, "key": key, "timestamp": timestamp, "msg": msg}})
        else:
            print("in else>post")
            posts[id] = {
                "id": id,
                "key": key,
                "timestamp": timestamp,
                "msg": msg,
                "user_id": user_id,
                "user_key": user_key,
            }
            print(posts)

    print(posts)
    print("______________")
    # print(id, key, timestamp, msg)
    if user_id is None or user_key is None:
        print("*******")
        return {"id": id, "key": key, "timestamp": timestamp, "msg": msg}
    else:
        return {
            "id": id,
            "key": key,
            "timestamp": timestamp,
            "msg": msg,
            "user_id": user_id,
            "user_key": user_key,
        }

@app.get("/post/<int:id>")
# If the post does not exist, it should return an error message with a 404 exit status (indicating ‘not found’).
def get(id):
    print("id is", id)
    # global posts
    if id is None:
        return {"err": "need an id"}, 400

    if isinstance(id, int) is False:
        return {"err": "id must be an integer"}, 400

    if id < 0:
        return {"err": "id must be positive"}, 400

    if id > 1000000:
        return {"err": "id must be less than 1000000"}, 400

    with lock:
        if id not in posts:
            return {"err": "post not found"}, 404
        print("post is ", posts[id])

        # return id, timestamp and msg
        posta = {}
        posta[id] = {
            "id": posts[id]["id"],
            "timestamp": posts[id]["timestamp"],
            "msg": posts[id]["msg"],
        }
        return posta[id]

@app.delete("/post/<int:id>/delete/<key>")
# If the post does not exist, it should return an error message with a 404 exit status (indicating ‘not found’).
def delete(id, key):
    # global posts
    if id is None or key is None:
        return {"err": "need an id and key"}, 400

    if isinstance(id, int) is False:
        return {"err": "id must be an integer"}, 400

    if id < 0:
        return {"err": "id must be positive"}, 400

    if id > 1000000:
        return {"err": "id must be less than 1000000"}, 400

    if id not in posts:
            return {"err": "post not found"}, 404

    # if key != posts[id]["key"]:
    #         return {"err": "incorrect key"}, 403


            
    with lock:

        
        if "user_key" in posts[id] and posts[id]["user_key"] is not None:
            if key == posts[id]["user_key"]:
                id = posts[id]["id"]
                key = posts[id]["key"]
                timestamp = posts[id]["timestamp"]
                del posts[id]
                print("Deleted by user key")
                return {"id": id, "key": key, "timestamp": timestamp}
            
        
        
        elif key == posts[id]["key"]:
                id = posts[id]["id"]
                key = posts[id]["key"]
                timestamp = posts[id]["timestamp"]
                del posts[id]
                print("Deleted by post key")
                return {"id": id, "key": key, "timestamp": timestamp}
        
        
        # if key in users.values():
    
        else:
            return {"err":"incorrect key"}, 403


@app.post("/post/search")
def search():
    # global posts
    o = request.get_json(force=True)

    startTimeStamp = o.get("startTime", None)
    endTimeStamp = o.get("endTime", None)
    print(startTimeStamp, endTimeStamp)
    print("post>search")
    endResult = []

    if startTimeStamp is not None and endTimeStamp is not None:
        for i in posts.values():
            print("1")
            if startTimeStamp <= i["timestamp"] <= endTimeStamp:
                endResult.append(i)

    if startTimeStamp is None and endTimeStamp is not None:
        for i in posts.values():
            print("2")
            if i["timestamp"] <= endTimeStamp:
                endResult.append(i)

    if startTimeStamp is not None and endTimeStamp is None:
        print("3")
        print("===========================================")
        print(posts.values(),"post values")
        for i in posts.values():
            print((i["timestamp"]), startTimeStamp)
            print(i,"i")
            if startTimeStamp <= i["timestamp"]:
                endResult.append(i)
    print(endResult)
    return endResult


@app.get("/post/user/<string:id>")
def user(id):
    print("vdhsjvhcvfhsd bdskjbfgksjdbfk.kj kjsbgkj")
    print(users,"users")
    print(id,"idddd")
    print(posts,"post")
    print(posts.values(),"post values")
    if not users[id]:
        return {"err": "user not found"}, 404

    endResult = []

    for i in posts.values():
        print(i,"iiiiiiiiiiiii")
        if i["user_id"] == id:
            endResult.append(i)

    return endResult

@app.get("/post/searchbymsg/<string:msg>")
def searchByMsg(msg):
    global posts
    print(posts,"posts")
    print(msg)
    if msg is None:
        return {"err": "need a message"}, 400

    if isinstance(msg, str) is False:
        return {"err": "message must be a string"}, 400

    endResult = []
    print(endResult)
    print(posts,"posts")
    for i in posts.values():
        print("in for loop")
        if msg in i["msg"]:
            print("in if cdn")
            endResult.append(i)

    print(endResult)
    return endResult
