import sys
import json

mapName = sys.argv[1]
gameMapJSON = ''

with open(mapName,"r") as f:
    gameMapJSON = f.read()

f.close()
try:
   gameMapDecoded= json.loads(gameMapJSON)
except:
    print("JSON is not in proper format")


def is_valid(file):
    for i in file:
        if('name' in i and 'desc' in i and 'exits'  in i):
            if ((not isinstance(i['exits'], dict) or not isinstance(i['name'], str) or not isinstance(i['desc'], str))):
                raise Exception('every room must have a name, desc, and exits of appropriate type!') 
        else:
            raise Exception("every room must have a name, desc, and exits!")    

try:
    is_valid(gameMapDecoded)
except Exception as e :
    print(e)
    sys.exit()
     



playerHealth= 100
def play():
    global playerHealth
    won = False
    currentRoom = 0
    inventory=[]
    verbs = ["go","get","look","inventory","help","quit","eat","drop","hp"]



    def checkWon(inventory,playerHealth):
        impItems=["dreizack","talwar","hagibis","shuriken","katana"]
        impItems.sort()
        inventory.sort()
        if(impItems == inventory and playerHealth>=100):
            print("Congratulation!!! You won the game")
            print("REASON : You have all the items required to slay the Monster")
            print("REASON: You won because you hp was above 100")
            return True
        else:
            print("You died fighting monster")
            if(impItems != inventory):
                print("REASON : You were missing the items required to fight Monster")
            if(playerHealth < 100):
                print("REASON: You died because you hp was below 100")
                print("You should have recharged your hp before entering the room")
            return True
        
    def printRoomData(roomNumber):
        if(roomNumber >= 4):
            print("Oops: You are in {name}".format(name=gameMapDecoded[roomNumber]["name"]))
            
        else:
            print(">",gameMapDecoded[roomNumber]["name"])
            print()
            print(gameMapDecoded[roomNumber]["desc"])
            print()
            
            if('items' in gameMapDecoded[roomNumber]):
                if(len(gameMapDecoded[roomNumber]["items"])>0):
                    items_str = "Items: " + ", ".join(gameMapDecoded[roomNumber]["items"])
                    print(items_str)
                    print()
                
            exits_str = "Exits: " + " ".join(gameMapDecoded[roomNumber]["exits"].keys())
            print(exits_str)
            print()

    def checkUserInput(verb,value):
        if verb=='go':
            if(value is None):
                print("Sorry, you need to 'go' somewhere.")
                return currentRoom
            keys=[]
            matching_dir=[]
            for k,v in gameMapDecoded[currentRoom]["exits"].items():
                keys.append(k)
                
            for item in keys:
                # print(value,"value")
                if item == value:
                    # print("going {direc}".format(direc=item))
                    print("You go {val}.".format(val=value))
                    print()
                    # return currentRoom
                    return gameMapDecoded[currentRoom]["exits"][item]
                else:
                    # print("in else!")
                    for key in keys:
                        if(key.startswith(value)):
                            matching_dir.append(key)
                
                    if len(matching_dir) == 0:
                        print("There's no way to go {val}.".format(val=value))
                        return currentRoom
                    elif len(matching_dir) == 1:
                        # print("in elif")
                        # print(matching_dir[0],"hdshfh")
                        print("You go {val}.".format(val=value))
                        print()
                        return gameMapDecoded[currentRoom]["exits"][matching_dir[0]]
                    else:
                        print("in else else")
                        st = "Do you mean "
                        if len(matching_dir) == 2:
                            for i,item in enumerate(matching_dir):
                                if(i == len(matching_dir)-1):
                                    st+= "{item}".format(item=item)+" ?"
                                else:
                                    st+="{item}".format(item=item)+" or "
                        elif len(matching_dir) > 2:
                            for i,item in enumerate(matching_dir):
                                if(i== len(matching_dir)-1):
                                    st+="{item}".format(item=item)+" ?"
                                else:
                                    st+="{item}".format(item=item)+" or "
                        print(st)
                        return currentRoom
               
        

        elif verb == 'get':
            obj = gameMapDecoded[currentRoom]
            itemsByCategoryPresent=False
            keyOfItemsByCategory = ""
            ItemsByCategoryList = ["weapons","foodItems","randomItems"]
            languageOfRoom = ["japanese","gujarati","filipino","german"]
            for k,v in obj.items():
                if(k=="items"):
                    matching_items=[]
                    for item in obj[k]:
                        if(item.lower().startswith(value) == True):
                            matching_items.append(item.lower())
                    

                    if len(matching_items) == 0:
                        # print("{val} is not in the room".format(val=value))
                        if(value is not None):
                            print("There's no {val} anywhere.".format(val = value))
                        else:
                            print("Sorry, you need to 'get' something.")
                    elif len(matching_items) == 1:
                        st=""
                        for key,v in obj.items():
                            if(key=="itemsByCategory"):
                                itemsByCategoryPresent=True

                        if itemsByCategoryPresent:
                            for lang in languageOfRoom:
                                if lang in obj["itemsByCategory"][0]:
                                    keyOfItemsByCategory = lang

                            for category in ItemsByCategoryList:
                                for idx,i in enumerate(obj["itemsByCategory"][0][keyOfItemsByCategory][category][keyOfItemsByCategory]):
                                    if(matching_items[0] == i):
                                        obj[k].remove(matching_items[0])
                                        inventory.append(matching_items[0])
                                        if(category == "weapons"):
                                            print("Cool!! You picked '{item}' which is '{eng}' in '{key} language' and it's is of category {weapon} ".format(item=matching_items[0],eng=obj["itemsByCategory"][0][keyOfItemsByCategory][category]["english"][idx],key=keyOfItemsByCategory,weapon=category))
                                        elif(category == "foodItems"):
                                            print("Yumm!! You picked '{item}' which is '{eng}' in '{key} language' and it's is of category {foodItem} ".format(item=matching_items[0],eng=obj["itemsByCategory"][0][keyOfItemsByCategory][category]["english"][idx],key=keyOfItemsByCategory,foodItem=category))
                                        elif(category == "randomItems"):
                                            print("Interesting!! You picked '{item}' which is '{eng}' in '{key} language' and it's is of category {randomItem} ".format(item=matching_items[0],eng=obj["itemsByCategory"][0][keyOfItemsByCategory][category]["english"][idx],key=keyOfItemsByCategory,randomItem=category))
                                                                           
                                        return currentRoom
                        else:
                            obj[k].remove(matching_items[0])
                            inventory.append(matching_items[0])
                            print("You pick up the {item}.".format(item=matching_items[0]))
                            return currentRoom
                    else:
                        st='Did you want to get the '
                        if len(matching_items) == 2:
                            for i,item in enumerate(matching_items):
                                if(i == len(matching_items)-1):
                                    st+= "{item}".format(item=item)+" ?"
                                else:
                                    st+="{item}".format(item=item)+" or "
                        elif len(matching_items) > 2:
                            for i,item in enumerate(matching_items):
                                if(i== len(matching_items)-1):
                                    st+="{item}".format(item=item)+" ?"
                                else:
                                    st+="{item}".format(item=item)+" or "
                        print(st)
                        return currentRoom
                    return currentRoom
            else:
                print("There's no rose anywhere.")  
                return currentRoom
        elif verb == 'eat':
            print("vjsdhvjvvbjbjlnkjbsdkjbjkcbjkbk")
            obj = gameMapDecoded[currentRoom]
            itemsByCategoryPresent=False
            keyOfItemsByCategory = ""
            ItemsByCategoryList = ["weapons","foodItems","randomItems"]
            languageOfRoom = ["japanese","gujarati","filipino","german"]
     
            matching_items=[]
            for item in inventory:
                if(item.lower().startswith(value) == True):
                    matching_items.append(item.lower())
            

            if len(matching_items) == 0:
                print("{val} is not in the inventory".format(val=value))
            elif len(matching_items) == 1:
                st=""
                for key,v in obj.items():
                    if(key=="itemsByCategory"):
                        itemsByCategoryPresent=True

                if itemsByCategoryPresent:
                    for lang in languageOfRoom:
                        if lang in obj["itemsByCategory"][0]:
                            keyOfItemsByCategory = lang

                    for category in ItemsByCategoryList:
                        for idx,i in enumerate(obj["itemsByCategory"][0][keyOfItemsByCategory][category][keyOfItemsByCategory]):
                            if(matching_items[0] == i):
                                # obj[k].remove(matching_items[0])
                                # inventory.append(matching_items[0])
                                if(category == "weapons"):
                                    print("Wth!! why do you want to eat '{eng}'?? Have you gone crazy?".format(eng=obj["itemsByCategory"][0][keyOfItemsByCategory][category]["english"][idx]))
                                elif(category == "foodItems"):
                                    print("Yumm!! You just ate '{item}' which is '{eng}'".format(item=matching_items[0],eng=obj["itemsByCategory"][0][keyOfItemsByCategory][category]["english"][idx]))
                                    global playerHealth
                                    playerHealth = playerHealth + 25
                                    inventory.remove(matching_items[0])
            
                                elif(category == "randomItems"):
                                    print("Why the hell do you want to eat '{eng}'".format(eng=obj["itemsByCategory"][0][keyOfItemsByCategory][category]["english"][idx]))
                                                                    
                                return currentRoom    
            else:
                st='What do you want to eat '
                if len(matching_items) == 2:
                    for i,item in enumerate(matching_items):
                        if(i == len(matching_items)-1):
                            st+= "{item}".format(item=item)+" ?"
                        else:
                            st+="{item}".format(item=item)+" or "
                elif len(matching_items) > 2:
                    for i,item in enumerate(matching_items):
                        if(i== len(matching_items)-1):
                            st+="{item}".format(item=item)+" ?"
                        else:
                            st+="{item}".format(item=item)+" or "
                print(st)
                return currentRoom
            

        elif verb == 'drop':
            matching_items=[]
            if len(inventory) == 0:
                print("Inventory is empty nothing to drop,First get something")
                return currentRoom
            else:
                for item in inventory:
                        if(item.startswith(value) == True):
                            matching_items.append(item)
                    
                if len(matching_items) == 0:
                    print("{val} is not in the inventory or no item that starts with {val}".format(val=value))
                elif len(matching_items) == 1:
                    inventory.remove(matching_items[0])
                    gameMapDecoded[currentRoom]["items"].append(matching_items[0])
                    print("You drop the {item}.".format(item=matching_items[0]))
                    return currentRoom
                else:
                    st='Did you want to drop the '
                    if len(matching_items) == 2:
                        for i,item in enumerate(matching_items):
                            if(i == len(matching_items)-1):
                                st+= "{item}".format(item=item)+" ?"
                            else:
                                st+="{item}".format(item=item)+" or "
                    elif len(matching_items) > 2:
                        for i,item in enumerate(matching_items):
                            if(i== len(matching_items)-1):
                                st+="{item}".format(item=item)+" ?"
                            else:
                                st+="{item}".format(item=item)+" or "
                    print(st)
                    return currentRoom
                return currentRoom      

        else:
            print("Bad input")
            return currentRoom
    
    
    printRoomData(currentRoom)
    while(not won): 
        try:
            userInput = input("What would you like to do? ").strip().split()
        except EOFError as e:
            print()
            print("Use 'quit' to exit.")
            userInput = input("What would you like to do? ").strip().split()
        for i in inventory:
            if i=="geheimer-schlussel":
                gameMapDecoded.append({"name":"Monster's room"})
                gameMapDecoded[2]["exits"]["northsoutheastwest"]=4
                inventory.remove("geheimer-schlussel")

        if len(userInput) == 2:
            verb = userInput[0].lower()
            value = userInput[1].lower()
        elif len(userInput) == 1:
            verb = userInput[0].lower()
            value = None
        else:
            print("The input is not correct expected 1 or 2 but received {len}".format(len = len(userInput)))
            return currentRoom

        matching_verbs = []
        for item in verbs:
            if(item.startswith(verb) == True):
                matching_verbs.append(item)
        
        if len(matching_verbs) == 0:
            # print(userInput[0],"user_input")
            print("no verb found with this name",userInput[0])
            # print("no verb like {val} ".format(val=value))

        elif len(matching_verbs) == 1:
            if matching_verbs[0] == "look":
                printRoomData(currentRoom)
            elif matching_verbs[0] == "help":
                for verb in verbs:
                    if verb == "go" or verb == "get":
                        print("{verb} ...".format(verb=verb))
                    else:
                        print("{verb}".format(verb=verb))
            elif matching_verbs[0] == "inventory":
                if len(inventory)>0:
                    print("Inventory:")
                    for item in inventory:
                        print(" ",item)
                else:
                    print("You're not carrying anything.")
            elif matching_verbs[0] == "quit":
                print("Goodbye!")
                won = True
            elif matching_verbs[0] == "hp":
                print("Your hp is {hp}".format(hp=playerHealth))
            elif matching_verbs[0] == "result":
                print("Your result")
            else:
                previousRoom = currentRoom
                prevInventory = len(inventory)                
                currentRoom = checkUserInput(matching_verbs[0],value)
                newInventory = len(inventory)
                if(currentRoom != previousRoom): 
                    printRoomData(currentRoom)
                    if(currentRoom == 4):
                        won = checkWon(inventory,playerHealth)
                    if(len(inventory) > 0):
                        playerHealth-=len(inventory)
                    else:
                        playerHealth-=1
                if(prevInventory != newInventory):
                    if matching_verbs[0] == "drop":
                        playerHealth-=1
        
        else:
            st='Did you want to do '
            if len(matching_verbs) == 2:
                for i,item in enumerate(matching_verbs):
                    if(i == len(matching_verbs)-1):
                        st+= "{item}".format(item=item)+" ?"
                    else:
                        st+="{item}".format(item=item)+" or "
            elif len(matching_verbs) > 2:
                for i,item in enumerate(matching_verbs):
                    if(i== len(matching_verbs)-1):
                        st+="{item}".format(item=item)+" ?"
                    else:
                        st+="{item}".format(item=item)+" or "
            print(st)
                 

play()