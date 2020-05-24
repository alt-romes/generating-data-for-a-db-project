import generatePermissions

import random
import re
import requests

import matplotlib.pyplot as plt

import time

import math

# FINE TUNING PARAMETERS
MAX_GENERATIONS = 1000
MAX_PLAYERS = 20 #20
MAX_NUMBER_ITEMS = 53 #100
MAX_SIZE = MAX_PLAYERS

MAX_RANDOM_ADD_ITEMS = 30
MAX_MOVE_IN_DIRECTION = 20
PLAYER_DEFAULT_HEALTH = 60
INV_SIZE = 42
MAX_ITEMS_SOLD_OR_BOUGHT_AT_ONCE = 6
NUMBER_OF_FACTIONS = int(MAX_PLAYERS / 4)
FRIENDS_PER_PLAYER = int(MAX_PLAYERS / 6)

MIN_DISTANCE_BETWEEN_SHOPS = MAX_SIZE / 5
NEW_ITEM_CHANCE = 0.1
SEND_MESSAGE_CHANCE = 0.05
NEW_PLAYER_CHANCE = 0.03
NEW_FACTION_CHANCE = 0.002
CHANCE_FOR_DESCRIPTION_OR_HEADER = 0.32
# DATABASE STRINGS
INSERT_PLAYERS = "insert into players(name) values('{}')"
# INSERT_PLAYERS = "Created player {}"

SEND_MESSAGE = "begin new_message('{}','{}','{}'); end"

INSERT_ITEMS = "insert into items(item_name,item_description) values('{}','{}')"
# INSERT_ITEMS = "Created item {}: {}"

INSERT_ITEMS_INV = "insert into inventory (player_name,id_item,inv_amount) values('{}',{},{})"
# INSERT_ITEMS_INV = "Player {} acquired {}. Amount: {}"

UPDATE_ITEMS_INV = "update inventory set inv_amount=inv_amount+{} where player_name='{}' and id_item={}"
# UPDATE_ITEMS_INV = "Inventory now has {} more for user {}, of item {}"

INSERT_IN_FACTION = "insert into factions values ('{}',{},{},{},'{}')"

PLAYER_JOIN_FACTION = "begin join_faction('{}','{}'); end"

UPDATE_PLAYER_FACTION_OPTIONS = "update belongs set nickname='{}', entrance_quote='{}' where player_name='{}' and faction_name='{}'"

CREATE_SHOP = "begin add_shop('{}',{},{}); end"
# CREATE_SHOP = "Player {} created at {}, {} a new shop: {}"

UPDATE_SHOP_HEADER = "update shops set shop_header='{}' where player_name='{}' and id_shop={}"

PLAYER_KILLED = "insert into kills(waskilled_name,killer_name) values('{}','{}')"
# PLAYER_KILLED = "Player {} was killed by {}"
UPDATE_PLAYER_KILLED = "update kills set count_kills=count_kills+1 where waskilled_name='{}' and killer_name='{}'"


PROCEDURE_PUT_FOR_SALE = "begin put_item_for_sale('{}',{},{},{},{}); end"

# PUT_ITEM_FOR_SALE = "insert into for_sale values('{}',{},{},{},{})"
# PUT_ITEM_FOR_SALE = "Player {} in shop {} puts {} for sale for {}. {} available"

# UPDATE_ITEM_FOR_SALE = "update for_sale set sale_amount=sale_amount+{} where player_name='{}' and id_shop={} and id_item={}"
# UPDATE_ITEM_FOR_SALE = "{} more items restocked for player {} shop {} item {}"

# ITEM_WAS_BOUGHT_FROM_SHOP = "insert into transaction(buyer_name,seller_name,id_shop,id_item,bought_amount) values('{}','{}',{},{},{})"
# ITEM_WAS_BOUGHT_FROM_SHOP = "Player {} bought from {}, in shop {} the item {}. Amount: {}"

# ITEM_WAS_BOUGHT_AGAIN_FROM_SHOP = "update transaction set bought_amount=bought_amount+{} where buyer_name='{}' and seller_name='{}' and id_shop={} and id_item={}"
# ITEM_WAS_BOUGHT_AGAIN_FROM_SHOP = "{} more were bought by {} from {}, in shop {} of item {}"

BUY_ITEMS_FROM_SHOP = "begin buy_items('{}','{}',{},{},{}); end"

UPDATE_PLAYER_PERMISSION = "update hasPermissions set identificator='{}' where player_name='{}' and identificator not like '%faction%'"



# FLAIR STRINGS
DESC_STARTERS = ["A normal", "An ordinary", "Simple", "A standard", "Your standard", "A cool looking", "An awesome", "A pretty cool", "Default", "An elementary", "Your usual", "A usual", "An everyday", "Your everyday", "An average looking", "An average", "A conventional", "Your average", "An OK", "A vanilla", "Unique", "A common", "Mainstream", "Your typical", "A typical", "A modest", "A neat", "A bland", "A serious looking", "A decent looking", "A decent", "Pretty nice", "A nice", "An undemanding", "A manageable", "An effortless", "A user-friendly", "A coherent", "An understandable", "An accessible", "Standard", "A basic", "A blunt", "Pure", "Candid", "Some honest", "Some demanding", "A piece of cake but its actually", "You wish itd make sound but it doesnt. Your", "Show it to your friends. Your", "Go crazy with this", "Looks better than you, a good", "But does it fly? A simple", "How will you explain this? Your cool", "A magnificient", "You cant drive it, its a non-drivable", "A sarcastic", "Funny looking", "Has no wheels, but its a decent", "A beautiful", "Youre just holding more", "How did you even get this", "A rare", "One more", "Close your eyes again, its still just one more", "A f*cking"]

# CODE
class DBC:
    EXECUTE_URL = 'https://apex.oracle.com/pls/apex/troyka/mod/execute' #I've disabled this endpoint now...

    def __init__(self):
        self.buffer = []

    def executeInDB(self, command):
        return
        r = requests.post(self.EXECUTE_URL, {"command": command})

        error = re.findall('<span style="font-size: 1\.1em;">\n\t\t.*?(ORA-.*?)\n', r.text)
        print("/* RESPONSE STATUS: ", r.status_code, ("ERROR: " + error[0] if len(error)>0 else ""), "*/")

    def printAndExecute(self, c):
        # print(c+";")

        if ((c.split(" ")[0] == "insert" or c.split(" ")[0] == "begin") and len(self.buffer)==0) or (c.split(" ")[0] == "insert" and self.buffer[0].split(" ")[2] == c.split(" ")[2]) or (c.split(" ")[0] == "begin" and self.buffer[0].split(" ")[0] == "begin"):
            self.buffer.append(c)
        else:
            if len(self.buffer) > 0:
                insertManyString = ""
                if len(self.buffer) == 1:
                    insertManyString = self.buffer[0]

                elif self.buffer[0].split(" ")[0] == "insert":
                    insertManyString = "insert all\n"
                    for b in self.buffer:
                        insertManyString += " ".join(b.split(" ")[1:]) + "\n"
                    insertManyString += "select * from dual"
                
                elif self.buffer[0].split(" ")[0] == "begin":
                    insertManyString = "begin\n"
                    for b in self.buffer:
                        insertManyString += " ".join(b.split(" ")[1:len(b.split(" "))-1]) + "\n"
                    insertManyString += "end"

                self.buffer.clear()

                print(insertManyString + ";" + ("" if insertManyString.split(" ")[0]=="insert" else "\n/"))
                self.executeInDB(insertManyString + ("" if insertManyString.split(" ")[0]=="insert" else ";"))

            if c.split(" ")[0] == "insert" or c.split(" ")[0] == "begin":
                self.buffer.append(c)
            else:
                
                print(c+";"+("\n/" if c.split(" ")[0]=="begin" else ""))
                self.executeInDB(c + (";" if c.split(" ")[0]=="begin" else ""))


    def insertPlayer(self, p):
        c = INSERT_PLAYERS.format(p.name)
        self.printAndExecute(c)

    def sendMessage(self, p, o, t):
        c = SEND_MESSAGE.format(p.name, o.name, t.replace("'", "")[:300])
        self.printAndExecute(c)

    def updateItemsInv(self, amount, pname, iid):
        c = UPDATE_ITEMS_INV.format(amount, pname, iid+1)
        self.printAndExecute(c)

    def insertItemsInv(self, pname, iid, amount):
        c = INSERT_ITEMS_INV.format(pname, iid+1, amount)
        self.printAndExecute(c)

    def insertFaction(self, f):
        c = INSERT_IN_FACTION.format(f.name, f.entrance_level, f.position[0], f.position[1], f.desc)
        self.printAndExecute(c)
    
    def playerJoinFaction(self, p, f):
        c = PLAYER_JOIN_FACTION.format(p.name, f.name)
        self.printAndExecute(c)
        if random.random() < CHANCE_FOR_DESCRIPTION_OR_HEADER:
            c = UPDATE_PLAYER_FACTION_OPTIONS.format(p.nickname.replace("'", "")[:30], p.makeEntranceQuote().replace("'", "")[:150], p.name, f.name)
            self.printAndExecute(c)
    
    def createShop(self, newShop):
        c = CREATE_SHOP.format(newShop.owner.name, newShop.position[0], newShop.position[1])
        self.printAndExecute(c)
        if random.random() < CHANCE_FOR_DESCRIPTION_OR_HEADER:
            c = UPDATE_SHOP_HEADER.format(newShop.shop_header.replace("'", "")[:150], newShop.owner.name, newShop.id_shop+1)
            self.printAndExecute(c)

    def playerKilled(self, deadName, attackerName):
        c = PLAYER_KILLED.format(deadName, attackerName)
        self.printAndExecute(c)

    def updatePlayerKilledCount(self, deadName, attackerName):
        c = UPDATE_PLAYER_KILLED.format(deadName, attackerName)
        self.printAndExecute(c)

    def insertItem(self, item):
        c = INSERT_ITEMS.format(item.name, item.desc)
        self.printAndExecute(c)

    def procedurePutForSale(self, pname, id_shop, id_item, price, amount):
        c = PROCEDURE_PUT_FOR_SALE.format(pname, id_shop+1, id_item+1, price, amount)
        self.printAndExecute(c) 

    # def putItemForSale(self, pname, id_shop, id_item, price, amount):
    #     c = PUT_ITEM_FOR_SALE.format(pname, id_shop+1, id_item+1, price, amount)
    #     self.printAndExecute(c)

    # def updateItemForSale(self, amount, pname, id_shop, id_item):
    #     c = UPDATE_ITEM_FOR_SALE.format(amount, pname, id_shop+1, id_item+1)
    #     self.printAndExecute(c)

    def shopSoldItem(self, buyerName, sellerName, id_shop, id_item, amount):
        c = BUY_ITEMS_FROM_SHOP.format(buyerName, sellerName, id_shop+1, id_item+1, amount)
        self.printAndExecute(c)
    
    def updatePermission(self, p, permission):
        c = UPDATE_PLAYER_PERMISSION.format(permission, p.name)
        self.printAndExecute(c)


DBC = DBC()

class Util:
    def calculateDistance(p1, p2):
        return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

class Graphics:
    def __init__(self, max_size):
        self.max_size = max_size

    def drawState(self, players):
        plt.axis([-self.max_size, self.max_size, -self.max_size, self.max_size])
        self.plotplayersX = list()
        self.plotplayersY = list()

        self.plotshopsX = list()
        self.plotshopsY = list()

        for player in players:
            self.plotplayersX.append(player.position[0])
            self.plotplayersY.append(player.position[1])
            for shop in player.shops:
                self.plotshopsX.append(shop.position[0])
                self.plotshopsY.append(shop.position[1])
    
        plt.plot(self.plotplayersX, self.plotplayersY, "ro", self.plotshopsX, self.plotshopsY, "go")
        plt.draw()
        plt.pause(0.01)
        plt.clf()

class Item:
    def __init__(self, iid, name, minecraft_id):
        self.id = iid
        self.name = name
        self.minecraft_id = minecraft_id
        self.desc = self.makeDescription()

    def makeDescription(self):
        return random.choice(DESC_STARTERS) + " " + self.name.lower()

class Shop:
    def __init__(self, owner, id_shop, position):
        self.owner = owner
        self.id_shop = id_shop
        self.position = position
        self.shop_header = self.makeShopHeader()
        self.for_sale = {}
        self.was_shopped_by = []
    
    def makeShopHeader(self):
        return random.choice(["We interrupt this program to annoy you and make things generally more irritating.", "He's not the Messiah—he's a very naughty boy!", "Strange women lying in ponds, distributing swords, is no basis for a system of government!", "And finally…", "The mill's closed…", "But kids were different in them days…", "… They didn't have their heads filled with all this Cartesian Dualism!", "Shut up, you American…", "We use only the finest baby frogs…", "My brain hurts!", "There's nothing wrong with you that an expensive operation can't prolong.", "This is a vegetarian restaurant…", "Tonight, instead of discussing the existence or non-existence of God, they have decided to fight for it.", "She's a witch! Burn her already!", "It's just gone eight o'clock and time for the penguin on top of your television set to explode.", "Welcome to my shop! Enjoy!", "This is my shop! Welcome!", "The greatest shop you'll ever know", "An ambitious shop for an ambitious person", "The next level shop", "The next big thing shop", "An OK shop, don't you think?", "My shop tastes purple", 'May the Force be with you.', "There's no place like home.", "I'm the king of the world!", "Carpe diem. Seize the day, boys. Make your lives extraordinary.", "Elementary, my dear Watson.", "It's alive! It's alive!", "I'll be back.", "You're gonna need a bigger boat.", "Here's looking at you, kid.", "Houston, we have a problem.", "There's no crying in baseball!", "You can't handle the truth!", "A martini. Shaken, not stirred."])
    
    def putItemForSale(self, iid, amount):
        if iid in self.for_sale:
            self.for_sale[iid]['amount'] += amount
        else:
            self.for_sale[iid] = {}
            self.for_sale[iid]['bought'] = {}
            self.for_sale[iid]['amount'] = amount
            self.for_sale[iid]['price'] = random.randrange(5, 100) #TODO maybe make this in a way that the economy isn't random
        
        DBC.procedurePutForSale(self.owner.name, self.id_shop, iid, self.for_sale[iid]['price'], amount)

    def playerPurchase(self, buyerID, buyerName, iid, amount):
        self.for_sale[iid]['amount'] -= amount
        self.owner.balance += amount*self.for_sale[iid]['price']

        DBC.shopSoldItem(buyerName, self.owner.name, self.id_shop, iid, amount) 
        self.owner.level += amount


class Player:
    def __init__(self, uid, name, position):
        self.hp = PLAYER_DEFAULT_HEALTH
        self.uid = uid
        self.name = name
        self.position = position
        self.balance = 500
        self.inv = {}
        self.shops = []
        self.faction = None
        self.nickname = self.makeNickname()
        self.level = 0
        self.friends = []
        self.hasBeenKilledBy = []

    def makeFriends(self, possibleFriends):
        newFriends = random.choices(possibleFriends, k=(FRIENDS_PER_PLAYER if FRIENDS_PER_PLAYER <= len(possibleFriends) else len(possibleFriends)))
        for f in newFriends:
            f.addFriend(self)
        self.friends = random.choices(possibleFriends, k=(FRIENDS_PER_PLAYER if FRIENDS_PER_PLAYER <= len(possibleFriends) else len(possibleFriends)))
    
    def addFriend(self, friend):
        self.friends.append(friend)
    
    def makeNickname(self):
        return random.choice(["Biggus Dickus", "Crazy Joe", "Ruth", "Runnerman", "Cereal Killer", "Floyd", "Turner", "Money Bags", "The Boss", "Mafia", "Dingletron", "Jackie Chan", "The Ninja", "The Sniper", "Camper", "One Shot", "Bowman", "Lucky", "The Man"])

    def makeEntranceQuote(self):
        return random.choice(["We interrupt this program to annoy you and make things generally more irritating.", "He's not the Messiah—he's a very naughty boy!", "Strange women lying in ponds, distributing swords, is no basis for a system of government!", "And finally…", "The mill's closed…", "But kids were different in them days…", "… They didn't have their heads filled with all this Cartesian Dualism!", "Shut up, you American…", "We use only the finest baby frogs…", "My brain hurts!", "There's nothing wrong with you that an expensive operation can't prolong.", "This is a vegetarian restaurant…", "Tonight, instead of discussing the existence or non-existence of God, they have decided to fight for it.", "She's a witch! Burn her already!", "It's just gone eight o'clock and time for the penguin on top of your television set to explode."])

    def invIsFull(self):
        return len(self.inv) >= INV_SIZE

    def addToInv(self, item, amount):
        if item.id in self.inv:
            self.inv[item.id] += amount
            DBC.updateItemsInv(self.inv[item.id], self.name, item.id)
        else:
            self.inv[item.id] = amount
            DBC.insertItemsInv(self.name, item.id, amount)
        # print('{} of {} added to {}'.format(amount, item.name, self.name))

    def moveSomewhere(self, game):
        changedPosition = False
        while not changedPosition:
            randomX = random.randrange(-MAX_MOVE_IN_DIRECTION, MAX_MOVE_IN_DIRECTION)
            randomY = random.randrange(-MAX_MOVE_IN_DIRECTION, MAX_MOVE_IN_DIRECTION)
            if self.position[0]+randomX <= game.max_size and self.position[1]+randomY <= game.max_size and self.position[0]+randomX >= -game.max_size and self.position[1]+randomY >= -game.max_size:
                newX = self.position[0] + randomX
                newY = self.position[1] + randomY
                self.position = (newX, newY)
                changedPosition = True

    def thinkOfCreatingShop(self, game):
        if all([MIN_DISTANCE_BETWEEN_SHOPS < Util.calculateDistance(self.position, shop.position) for shop in self.shops]) and len(self.shops) < 3 and self.position not in game.gameMap:
            newShop = Shop(self, len(self.shops), self.position)
            DBC.createShop(newShop)
            self.shops.append(newShop)

    def receiveHit(self, dmg, attacker, game):
        self.hp -= dmg
        if self.hp <= 0:
            if attacker in self.hasBeenKilledBy:
                DBC.updatePlayerKilledCount(self.name, attacker.name)
            else:
                DBC.playerKilled(self.name, attacker.name)
                self.hasBeenKilledBy.append(attacker)
            self.position = (random.randrange(-game.max_size, game.max_size), random.randrange(-game.max_size, game.max_size))
            self.hp = PLAYER_DEFAULT_HEALTH

    def sellItemsInShop(self, shop):
        if len(self.inv)>0:
            for i in range(random.randrange(1, 1+(MAX_ITEMS_SOLD_OR_BOUGHT_AT_ONCE if len(self.inv) >= MAX_ITEMS_SOLD_OR_BOUGHT_AT_ONCE else len(self.inv)))):
                chosenItem=random.choice(list(self.inv))
                if self.inv[chosenItem] > 0:
                    amount = random.randrange(1, 1+self.inv[chosenItem])
                    shop.putItemForSale(chosenItem, amount)
                    self.inv[chosenItem] -= amount

    def buyItemsFromShop(self, shop):
        if len(shop.for_sale)>0:
            for i in range(random.randrange(1, 1+(MAX_ITEMS_SOLD_OR_BOUGHT_AT_ONCE if len(shop.for_sale) >= MAX_ITEMS_SOLD_OR_BOUGHT_AT_ONCE else len(shop.for_sale)))):
                chosenItem=random.choice(list(shop.for_sale))
                if(shop.for_sale[chosenItem]['amount']>0 and self.balance>=shop.for_sale[chosenItem]['price']):
                    amount = random.randrange(1, 1+shop.for_sale[chosenItem]['amount'])
                    if amount*shop.for_sale[chosenItem]['price'] > self.balance:
                        amount = int(self.balance/shop.for_sale[chosenItem]['price'])
                    shop.playerPurchase(self.uid, self.name, chosenItem, amount)
                    if chosenItem in self.inv:
                        self.inv[chosenItem] += amount
                    else:
                        self.inv[chosenItem] = amount
                    self.balance -= amount*shop.for_sale[chosenItem]['price']
                    self.level += amount

    def interactWithNeighbour(self, nb, game):
        if nb != self:
            if isinstance(nb, Shop):
                if nb.owner.uid != self.uid:
                    # print("{} buying from {}'s shop".format(self.name, nb.owner.name))
                    self.buyItemsFromShop(nb)
                else:
                    self.sellItemsInShop(nb)
            if isinstance(nb, Player) and random.random() < 0.5:
                hitDmg = random.randrange(1, 20)
                # print("{} deals {} damage to {}".format(self.name, hitDmg, nb.name))
                nb.receiveHit(hitDmg, self, game)

    def interactwithNeighbours(self, game):
        """
        Interacts with neighbours and returns a tuple of arrays, with x coords and y coords in separate arrays, representing coords where events happened
        """
        for i in range(-3, 4):
            for j in range(-3, 4):
                if i != 0 or j != 0:
                    if (self.position[0] + i, self.position[1] + j) in game.gameMap:
                        self.interactWithNeighbour(game.gameMap[(self.position[0]+i, self.position[1]+j)], game)

class Faction:
    def __init__(self, name, entrance_level, position, desc):
        self.name = name
        self.entrance_level = entrance_level
        self.position = position
        self.desc = desc
        self.members = {}

class Game:
    def __init__(self, rules, max_iterations, max_players, max_size):
        self.rules = rules
        self.max_iterations = max_iterations
        self.max_players = max_players
        self.max_size = max_size

    def genPlayers(self):
        names = set()
        names.update(map(lambda e: e.replace("_", "").replace('-', "").replace("'", ""), requests.get("http://names.drycodes.com/{}?nameOptions=starwarsFirstNames&combine=2&case=lower".format(self.max_players)).json()))
        names.update(map(lambda e: e.replace("_", "").replace('-', "").replace("'", ""), requests.get("http://names.drycodes.com/{}?nameOptions=starwarsLastNames&combine=2".format(self.max_players)).json()))
        names.update(map(lambda e: e.replace("_", ""), requests.get("http://names.drycodes.com/{}?nameOptions=girl_names&combine=1&case=lower".format(self.max_players)).json()))
        names.update(map(lambda e: e.replace("_", ""), requests.get("http://names.drycodes.com/{}?nameOptions=boy_names&combine=1&case=lower".format(self.max_players)).json()))
        names.update(map(lambda e: e.replace("_", "").replace('.', ""), requests.get("http://names.drycodes.com/{}?nameOptions=presidents&combine=1".format(self.max_players)).json()))
        names.update(map(lambda e: e.replace("_", "").replace("'", ""), requests.get("http://names.drycodes.com/{}?nameOptions=cities&combine=1&case=lower".format(self.max_players)).json()))
        self.players = list()
        for i in range(self.max_players):
            x = random.randrange(-self.max_size, self.max_size)
            y = random.randrange(-self.max_size, self.max_size)
            name = names.pop()
            p = Player(i, name[:30], (x, y))
            self.players.append(p)
            DBC.insertPlayer(p)
        
        for p in self.players:
            p.makeFriends(self.players)

        DBC.updatePermission(self.players[0], "admin")
        DBC.updatePermission(self.players[1], "moderator")
        DBC.updatePermission(self.players[2], "moderator")

    def createPlayer(self):
        names = set()
        names.update(map(lambda e: e.replace("_", ""), requests.get("http://names.drycodes.com/1?nameOptions=boy_names&combine=1&case=lower").json()))
        x = random.randrange(-self.max_size, self.max_size)
        y = random.randrange(-self.max_size, self.max_size)
        name = names.pop()
        if name not in names:
            p = Player(len(self.players), name[:30], (x, y))
            self.players.append(p)
            DBC.insertPlayer(p)
            p.makeFriends(self.players)
            return p
        
        
    def genItems(self):
        allitemsHTML = requests.get('https://minecraft-ids.grahamedgecombe.com/').text

        items = re.findall('class="name">(.*?)<.*?class="text-id">\((.*?)\)</', allitemsHTML.replace("'", ""))[:MAX_NUMBER_ITEMS]

        self.items = {"population": [], "weights": []}
        for i in range(len(items)):
            item = Item(i, items[i][0], items[i][1])
            self.items['population'].append(item)
            self.items['weights'].append(random.random())
            DBC.insertItem(item)

    def getFactionNames(self):
        factions_string = '1. Mystique - (Mystic in French) 2. Vortex 3. Dynamic 4. Wintersong 5. Villigence 6. Revenge 7. Twisted 8. Kryptic 9. Komorebi - (The Light that seeks through the trees) 10. Twizzle 11. Ethreal 12. Aurora 13. Solitude 14. Echo 15. Twighlight 16. Dawn 17. NecoCrypt 18. Keepers 19. Guardians 20. Purge 21. Velocity 22. Desire 23. Nexus 24. Dimlight 25. Wicked 26. Nefarious - (another word for wicked) 27. Nemophilists - (hunters of the woods) 28. Ukiyo - (Living in the moment; floating world) 29. Exo 30. Mythic - (or just Myth) 31. Kalopsia 32. Irusu - (another word for hiding) 33. Silence 34. Demonic 35. Defiance 36. Enlightment 37. Yoisho - (A world without meaning) 38. Brinille - (a twig) 39. Fernweh 40. Fallen 41. Darkened 42. Elysian - (beautiful) 43. Fresco 44. Amazon 45. Avalanche 46. Nova 47. Bimyou - (not bad, "meh) 48. Savage 49. Resistance 50. Evolved'
        self.faction_names = re.findall(r".*?\. (.*?) (- \((.*?)\) |)", factions_string)

    def genFactions(self):
        self.getFactionNames()

        self.factions = list()
        self.chosenLeaders = [None]
        for i in range(NUMBER_OF_FACTIONS):
            namearr = self.faction_names.pop()
            f = Faction(namearr[0], random.randrange(5, 8), (random.randrange(-MAX_SIZE, MAX_SIZE), random.randrange(-MAX_SIZE, MAX_SIZE)), (namearr[2] if namearr[2] != '' else 'This is our faction!'))
            leader = None
            while leader in self.chosenLeaders:
                leader = random.choice(self.players)
            self.chosenLeaders.append(leader)
            f.members[leader] = leader
            self.factions.append(f)
            leader.faction = f
            DBC.insertFaction(f)
            DBC.playerJoinFaction(leader, f)

    def createFaction(self):
        namearr = self.faction_names.pop()
        f = Faction(namearr[0], random.randrange(5, 8), (random.randrange(-MAX_SIZE, MAX_SIZE), random.randrange(-MAX_SIZE, MAX_SIZE)), (namearr[2] if namearr[2] != '' else 'This is our faction!'))
        leader = random.choice(self.players)
        i = 0
        while leader.faction != None and i<len(self.players):
            leader = random.choice(self.players)
            i += 1

        if i==len(self.players):
            leader = self.createPlayer()

        self.chosenLeaders.append(leader)
        f.members[leader] = leader
        self.factions.append(f)
        leader.faction = f
        DBC.insertFaction(f)
        DBC.playerJoinFaction(leader, f) 



    def genMessages(self):
        with open("movie_lines.txt", "r") as f:
            txt = f.read()
        self.pmessages=re.findall(".*\+\+\+\$\+\+\+ (.*)\n", txt)

    def generateStart(self):
        generatePermissions.generatePermissions()
        self.genPlayers()
        self.genItems()
        self.genFactions()
        self.genMessages()

    def nextState(self):
        self.gameMap = dict()
        for player in self.players:
            self.gameMap[player.position] = player
            for shop in player.shops:
                self.gameMap[shop.position] = shop
                
        chosenItems = random.choices(population=self.items["population"], weights=self.items["weights"], k=len(self.players))
        for i, player in enumerate(self.players):
            if random.random() <= NEW_ITEM_CHANCE and not player.invIsFull(): #TODO limit inv size?
                #TODO make items have different chances of being obtained. Dirt is more likely than gold
                player.addToInv(chosenItems[i], random.randrange(1, MAX_RANDOM_ADD_ITEMS))
            player.moveSomewhere(self)
            player.thinkOfCreatingShop(self)
            player.interactwithNeighbours(self)

            if player.faction == None:
                # for i in range(3)
                f = random.choice(self.factions)
                if player.level/5 >= f.entrance_level:
                    player.faction = f
                    f.members[player] = player
                    DBC.playerJoinFaction(player, f)
                    # break
            
            if random.random() < SEND_MESSAGE_CHANCE:
                other = random.choice(player.friends)
                if other != player:
                    m = random.choice(self.pmessages)
                    if len(m) > 1:
                        DBC.sendMessage(player, other, m)


        if random.random() < NEW_PLAYER_CHANCE:
            self.createPlayer()
        
        if random.random() < NEW_FACTION_CHANCE:
            self.createFaction()

    def run(self):
        # self.graphics = Graphics(self.max_size)
        self.generateStart()
        for i in range(MAX_GENERATIONS):
            self.nextState()
            # self.graphics.drawState(self.players)


if __name__ == "__main__":
    game = Game(0, 0, MAX_PLAYERS, MAX_SIZE)
    game.run()