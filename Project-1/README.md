Rushiraj Herma [rherma@stevens.edu](mailto:rherma@stevens.edu)

# the URL of your public GitHub repo
https://github.com/Rushiraj0608

# an estimate of how many hours you spent on the project
50 hours

# a description of how you tested your code
These are the steps of how I tested my code:
Testing with valid input:
The code was first tested using valid inputs, to ensure that it was functioning as intended. The input data was entered into the code, and the output was verified to be correct. The results were compared to expected values, and any discrepancies were analyzed to determine if there was a problem with the code.

Verifying appropriate answer:
Once the valid inputs had been successfully tested, the output was checked to ensure that it was appropriate for the input. Any necessary adjustments were made to the code.

Testing with incorrect input:
After verifying that the code was functioning properly with valid input, testing was then shifted to using incorrect input. This was done to ensure that the code did not break and was still functioning as intended.

Checking that code is not breaking:
During the testing with incorrect input, the code was checked to ensure that it did not break or produce any errors. Any errors or issues that were identified were analyzed and resolved.

Playing around in terminal:
Finally, the code was played around with in the terminal to ensure that it was functioning properly in different scenarios.

# bugs and issues
I am having trouble passing all the autograder test cases. I am passing only eleven test cases. I am not sure what is causing these test cases to fail, I tried but just couldn't figure out.

# resolved issue
In the **adventure.py** function, Initially I was using end in print function to print the output without generating new line. but because of this at the end of printing line I was having extra space, which made autograder fail my all test cases, after a while of debugging I realized my mistake. And then I used join function of string to get my desired string and then printed that to get accurate answer.

# Implemented extensions
# 1) drop
The drop extension is designed to provide players with the ability to remove items from their inventory. This can be useful in situations where the player no longer needs the item or wants to free up space in their inventory. The drop extension is described as the opposite of the "get" functionality, which is typically used to add items to a player's inventory. The drop extension, on the other hand, allows the player to remove items from their inventory.
Before an item can be dropped, it needs to be in the player's inventory. If it does not exist in their inventory, the drop command will promp appropriate message that player is not carrying that item.

These are the following steps through you can test this extension :
1) started game - which lend player in first room and printed details of first room.
rushirajherma@Rushirajs-Air project-1 % python3 new.py new_map.map
> A white room

You are in a simple room with white walls.

Items: efude, aisukyubutorei, hanga, ito, amerika, yokitori, ramen, tempura, katana, shuriken, kunai, jaberin

Exits: north east

2) pick up an item using get and added to an inventory, it shows a little discription about picked item in my custom map.
What would you like to do? get kunai
Cool!! You picked 'kunai' which is 'dagger' in 'japanese language' and it's is of category weapons 

3) went to another room
What would you like to do? go north
You go north.

> A blue room

This room is simple, too, but with blue walls.

Items: malaking-lubid, mga-proteksiyon-na-suite, kahon, banga, abodo, pancit-palabok, arroz-caldo, kare-kare, itak-tagalog, hagibis, karambit, tanto

Exits: east south

4)picked up one more item
What would you like to do? get tanto
Cool!! You picked 'tanto' which is 'Long knife' in 'filipino language' and it's is of category weapons 

5)got the contents of inventory to check all the picked items are in inventory
What would you like to do? inventory
Inventory:
  kunai
  tanto

6)dropped an item
What would you like to do? drop kunai
You drop the kunai.

7)checked inventory to find that item is actually dropped from inventory
What would you like to do? inventory
Inventory:
  tanto

8)tried dropping an item which is not in inventory
What would you like to do? drop table
table is not in the inventory or no item that starts with table

9)dropped all the items from inventory
What would you like to do? drop tanto
You drop the tanto.

10)checking if the inventory is empty or not after dropping all the items
What would you like to do? inventory
You're not carrying anything.
What would you like to do? 


# 2) Winning and loosing condition.
below are the conditions of winning and loosing the game.

In this game, the player needs to collect one or more items from each room and maintain their health above 100. They also need to find the secret key to enter the monster's room, which will only be visible after collecting the key. If the player reaches the monster's room with less than 100 health, they will lose the game, even if they have collected all the required items.

There are three types of items in the game: weapons, food items, and random items. To eat the food item you have to have get the food item in you inventory. And only food items can increase the player's health, and if the player tries to eat anything else, the game will display an appropriate message.

To win the game, the player needs to collect all the necessary items while maintaining their health above 100. They also need to find the secret key and the monster's room, which will only be visible after collecting the key. If the player fails to collect all the necessary items, cannot find the secret key and the monster's room, or reaches the monster's room with less than 100 health, they will lose the game. Therefore, the key to winning the game is careful exploration, management of health, and finding the necessary items and the monster's room.


here for this game,
secret key is : "geheimer-schlussel" in red room
necessary items to collect to kill monster : "dreizack","talwar","hagibis","shuriken","katana"

below is the step by step guide to play in my custom map

1) Loosing condition: Here I am not collecting any necessary weapons to kill the monster so even though after collecting secret key "geheimer-schlussel" from red room and finding monsters room by going northsoutheastwest from green room. I am unable to win as monster kills me.


rushirajherma@Rushirajs-Air project-1 % python3 new.py new_map.map
> A white room

You are in a simple room with white walls.

Items: efude, aisukyubutorei, hanga, ito, amerika, yokitori, ramen, tempura, katana, shuriken, kunai, jaberin

Exits: north east

What would you like to do? go n
You go n.

> A blue room

This room is simple, too, but with blue walls.

Items: malaking-lubid, mga-proteksiyon-na-suite, kahon, banga, abodo, pancit-palabok, arroz-caldo, kare-kare, itak-tagalog, hagibis, karambit, tanto

Exits: east south

What would you like to do? go e
You go e.

> A green room

You are in a simple room, with bright green walls.

Items: talwar, chappu, gada, trishul, katri, safarjan, khichdi, kelu, dakan-ni-ulti, pustak, ghadi

Exits: west south

What would you like to do? go s
You go s.

> A red room

This room is fancy. It's red!

Items: brot, eintopf, brezel, schwarzwalder-kirschtorte, riesiger-abfallbeutel-fur-haustiere, schutzmaske, geheimer-schlussel, schnurrbart-hitlers, riesiger-haustierabfallbeutel, keule, dreizack

Exits: north west

(--- I am collecting secret key here---)

What would you like to do? get geh
Interesting!! You picked 'geheimer-schlussel' which is 'secret key' in 'german language' and it's is of category randomItems 
What would you like to do? go n
You go n.

> A green room

You are in a simple room, with bright green walls.

Items: talwar, chappu, gada, trishul, katri, safarjan, khichdi, kelu, dakan-ni-ulti, pustak, ghadi

Exits: west south northsoutheastwest

What would you like to do? go northso
You go northso.

Oops: You are in Monster's room
You died fighting monster
REASON : You were missing the items required to fight Monster
REASON: You died because you hp was below 100
You should have recharged your hp before entering the room



----Now Loosing condition with health less than 100 condition----
rushirajherma@Rushirajs-Air project-1 % python3 new.py new_map.map
> A white room

You are in a simple room with white walls.

Items: efude, aisukyubutorei, hanga, ito, amerika, yokitori, ramen, tempura, katana, shuriken, kunai, jaberin

Exits: north east

What would you like to do? get kat
Cool!! You picked 'katana' which is 'sword' in 'japanese language' and it's is of category weapons 
What would you like to do? get shu
Cool!! You picked 'shuriken' which is 'ninja blades' in 'japanese language' and it's is of category weapons 
What would you like to do? go e
You go e.

> A red room

This room is fancy. It's red!

Items: brot, eintopf, brezel, schwarzwalder-kirschtorte, riesiger-abfallbeutel-fur-haustiere, schutzmaske, geheimer-schlussel, schnurrbart-hitlers, riesiger-haustierabfallbeutel, keule, dreizack

Exits: north west

What would you like to do? get dre
Cool!! You picked 'dreizack' which is 'trident' in 'german language' and it's is of category weapons 
What would you like to do? go n
You go n.

> A green room

You are in a simple room, with bright green walls.

Items: talwar, chappu, gada, trishul, katri, safarjan, khichdi, kelu, dakan-ni-ulti, pustak, ghadi

Exits: west south

What would you like to do? get tal
Cool!! You picked 'talwar' which is 'sword' in 'gujarati language' and it's is of category weapons 
What would you like to do? go s
You go s.

> A red room

This room is fancy. It's red!

Items: brot, eintopf, brezel, schwarzwalder-kirschtorte, riesiger-abfallbeutel-fur-haustiere, schutzmaske, geheimer-schlussel, schnurrbart-hitlers, riesiger-haustierabfallbeutel, keule

Exits: north west

What would you like to do? get geh
Interesting!! You picked 'geheimer-schlussel' which is 'secret key' in 'german language' and it's is of category randomItems 
What would you like to do? go n
You go n.

> A green room

You are in a simple room, with bright green walls.

Items: chappu, gada, trishul, katri, safarjan, khichdi, kelu, dakan-ni-ulti, pustak, ghadi

Exits: west south northsoutheastwest

What would you like to do? go w
You go w.

> A blue room

This room is simple, too, but with blue walls.

Items: malaking-lubid, mga-proteksiyon-na-suite, kahon, banga, abodo, pancit-palabok, arroz-caldo, kare-kare, itak-tagalog, hagibis, karambit, tanto

Exits: east south

What would you like to do? get hag
Cool!! You picked 'hagibis' which is 'dagger' in 'filipino language' and it's is of category weapons 
What would you like to do? go e
You go e.

> A green room

You are in a simple room, with bright green walls.

Items: chappu, gada, trishul, katri, safarjan, khichdi, kelu, dakan-ni-ulti, pustak, ghadi

Exits: west south northsoutheastwest

What would you like to do? go norths
You go norths.

Oops: You are in Monster's room
You died fighting monster
REASON: You died because you hp was below 100
You should have recharged your hp before entering the room


---------winning-----

rushirajherma@Rushirajs-Air project-1 % python3 new.py new_map.map
> A white room

You are in a simple room with white walls.

Items: efude, aisukyubutorei, hanga, ito, amerika, yokitori, ramen, tempura, katana, shuriken, kunai, jaberin

Exits: north east

What would you like to do? get kat
Cool!! You picked 'katana' which is 'sword' in 'japanese language' and it's is of category weapons 
What would you like to do? get shu
Cool!! You picked 'shuriken' which is 'ninja blades' in 'japanese language' and it's is of category weapons 
What would you like to do? go n
You go n.

> A blue room

This room is simple, too, but with blue walls.

Items: malaking-lubid, mga-proteksiyon-na-suite, kahon, banga, abodo, pancit-palabok, arroz-caldo, kare-kare, itak-tagalog, hagibis, karambit, tanto

Exits: east south

What would you like to do? get hag
Cool!! You picked 'hagibis' which is 'dagger' in 'filipino language' and it's is of category weapons 
What would you like to do? go e
You go e.

> A green room

You are in a simple room, with bright green walls.

Items: talwar, chappu, gada, trishul, katri, safarjan, khichdi, kelu, dakan-ni-ulti, pustak, ghadi

Exits: west south

What would you like to do? get talw
Cool!! You picked 'talwar' which is 'sword' in 'gujarati language' and it's is of category weapons 
What would you like to do? go w
You go w.

> A blue room

This room is simple, too, but with blue walls.

Items: malaking-lubid, mga-proteksiyon-na-suite, kahon, banga, abodo, pancit-palabok, arroz-caldo, kare-kare, itak-tagalog, karambit, tanto

Exits: east south

What would you like to do? go e
You go e.

> A green room

You are in a simple room, with bright green walls.

Items: chappu, gada, trishul, katri, safarjan, khichdi, kelu, dakan-ni-ulti, pustak, ghadi

Exits: west south

What would you like to do? go s
You go s.

> A red room

This room is fancy. It's red!

Items: brot, eintopf, brezel, schwarzwalder-kirschtorte, riesiger-abfallbeutel-fur-haustiere, schutzmaske, geheimer-schlussel, schnurrbart-hitlers, riesiger-haustierabfallbeutel, keule, dreizack

Exits: north west

What would you like to do? get dre
Cool!! You picked 'dreizack' which is 'trident' in 'german language' and it's is of category weapons 
What would you like to do? get geh
Interesting!! You picked 'geheimer-schlussel' which is 'secret key' in 'german language' and it's is of category randomItems 
What would you like to do? inventory
Inventory:
  katana
  shuriken
  hagibis
  talwar
  dreizack
What would you like to do? go north
You go north.

> A green room

You are in a simple room, with bright green walls.

Items: chappu, gada, trishul, katri, safarjan, khichdi, kelu, dakan-ni-ulti, pustak, ghadi

Exits: west south northsoutheastwest

What would you like to do? hp 
Your hp is 78
What would you like to do? get khi
Yumm!! You picked 'khichdi' which is 'hotchpotch' in 'gujarati language' and it's is of category foodItems 
What would you like to do? eat khic
vjsdhvjvvbjbjlnkjbsdkjbjkcbjkbk
Yumm!! You just ate 'khichdi' which is 'hotchpotch'
What would you like to do? hp
Your hp is 103
What would you like to do? go norths
You go norths.

Oops: You are in Monster's room
Congratulation!!! You won the game
REASON : You have all the items required to slay the Monster
REASON: You won because you hp was above 100



# 3) Abbreviations for verbs, directions, and items
It is common for text adventures to accept abbreviated forms of commands: for example, i might suffice to indicate inventory. It’s important that abbreviations only work when they are unambiguous: if you just typed g, would that indicate get or go?

example of Abbreviations can be seen in above example.