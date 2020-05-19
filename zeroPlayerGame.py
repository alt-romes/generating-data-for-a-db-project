#TODO: Perguntar ao professor sobre o multiple insert INSERT ALL

import generatePermissions

import random
import re
import requests

import matplotlib.pyplot as plt

import time

import math  

# FINE TUNING PARAMETERS
MAX_GENERATIONS = 1100
MAX_PLAYERS = 200
MAX_SIZE = MAX_PLAYERS*2

MAX_RANDOM_ADD_ITEMS = 30
MAX_MOVE_IN_DIRECTION = 15
PLAYER_DEFAULT_HEALTH = 60
INV_SIZE = 36
MAX_ITEMS_SOLD_OR_BOUGHT_AT_ONCE = 5
NUMBER_OF_FACTIONS = int(MAX_PLAYERS / 20)

MIN_DISTANCE_BETWEEN_SHOPS = MAX_SIZE / 4
NEW_ITEM_CHANCE = 0.45
SEND_MESSAGE_CHANCE = 0.02

# DATABASE STRINGS
INSERT_PLAYERS = "insert into players(name) values('{}');"
# INSERT_PLAYERS = "Created player {}"

SEND_MESSAGE = "insert into sendsText(sender_ID, receiver_ID, message) values ({}, {}, '{}');"

INSERT_ITEMS = "insert into items(item_name, item_description) values ('{}', '{}');"
# INSERT_ITEMS = "Created item {}: {}"

INSERT_ITEMS_INV = "insert into inventory (id, id_item, inv_amount) values ({}, {}, {});"
# INSERT_ITEMS_INV = "Player {} acquired {}. Amount: {}"

UPDATE_ITEMS_INV = "update inventory set inv_amount=inv_amount+{} where id={} and id_item={};"
# UPDATE_ITEMS_INV = "Inventory now has {} more for user {}, of item {}"

INSERT_IN_FACTION = "insert into factions values ('{}',{},{},{},'{}');"

PLAYER_JOIN_FACTION = "insert into belongs(id, faction_name) values ({},'{}');"

CREATE_SHOP = "insert into shops(id, coordx, coordy, shop_header) values ({}, {}, {}, '{}');"
# CREATE_SHOP = "Player {} created at {}, {} a new shop: {}"

PLAYER_KILLED = 'insert into kills (waskilled_ID, killed_ID) values ({}, {});'
# PLAYER_KILLED = "Player {} was killed by {}"

PUT_ITEM_FOR_SALE = 'insert into for_sale values({},{},{},{},{});'
# PUT_ITEM_FOR_SALE = "Player {} in shop {} puts {} for sale for {}. {} available"

UPDATE_ITEM_FOR_SALE = "update for_sale set sale_amount = sale_amount + {} where id={} and id_shop={} and id_item={};"
# UPDATE_ITEM_FOR_SALE = "{} more items restocked for player {} shop {} item {}"

ITEM_WAS_BOUGHT_FROM_SHOP = "insert into transaction(buyer_id,seller_id,id_shop,id_item,bought_amount) values({},{},{},{},{});"
# ITEM_WAS_BOUGHT_FROM_SHOP = "Player {} bought from {}, in shop {} the item {}. Amount: {}"

ITEM_WAS_BOUGHT_AGAIN_FROM_SHOP = "update transaction set bought_amount = bought_amount + {} where buyer_id={} and seller_id={} and id_shop={} and id_item={};"
# ITEM_WAS_BOUGHT_AGAIN_FROM_SHOP = "{} more were bought by {} from {}, in shop {} of item {}"

# FLAIR STRINGS
DESC_STARTERS = ["A normal", "An ordinary", "Simple", "A standard", "Your standard", "A cool looking", "An awesome", "A pretty cool", "Default", "An elementary", "Your usual", "A usual", "An everyday", "Your everyday", "An average looking", "An average", "A conventional", "Your average", "An OK", "A vanilla", "Unique", "A common", "Mainstream", "Your typical", "A typical", "A modest", "A neat", "A bland", "A serious looking", "A decent looking", "A decent", "Pretty nice", "A nice", "An undemanding", "A manageable", "An effortless", "A user-friendly", "A coherent", "An understandable", "An accessible", "Standard", "A basic", "A blunt", "Pure", "Candid", "Some honest", "Some demanding", "A piece of cake but its actually", "You wish itd make sound but it doesnt. Your", "Show it to your friends. Your", "Go crazy with this", "Looks better than you, a good", "But does it fly? A simple", "How will you explain this? Your cool", "A magnificient", "You cant drive it, its a non-drivable", "A sarcastic", "Funny looking", "Has no wheels, but its a decent", "A beautiful", "Looks better than your ex, but youre just holding one more", "How did you even get this", "A rare", "One more", "Close your eyes again, its still just one more", "A f*cking"]

# CODE
class DBC:
    def insertPlayer(p):
        print(INSERT_PLAYERS.format(p.name))

    def sendMessage(p, o, t):
        print(SEND_MESSAGE.format(p.uid+1, o.uid+1, t.replace("'", "")))

    def updateItemsInv(amount, uid, iid):
        print(UPDATE_ITEMS_INV.format(amount, uid+1, iid+1))

    def insertItemsInv(uid, iid, amount):
        print(INSERT_ITEMS_INV.format(uid+1, iid+1, amount))

    def insertFaction(f):
        print(INSERT_IN_FACTION.format(f.name, f.entrance_level, f.position[0], f.position[1], f.desc))
    
    def playerJoinFaction(p, f):
        print(PLAYER_JOIN_FACTION.format(p.uid+1, f.name))
    
    def createShop(newShop):
        print(CREATE_SHOP.format(newShop.owner.uid+1, newShop.position[0], newShop.position[1], newShop.shop_header))

    def playerKilled(deadID, attackerID):
        print(PLAYER_KILLED.format(deadID+1, attackerID+1))

    def insertItem(item):
        print(INSERT_ITEMS.format(item.name, item.desc))

    def putItemForSale(id, id_shop, id_item, price, amount):
        print(PUT_ITEM_FOR_SALE.format(id+1, id_shop+1, id_item+1, price, amount))

    def updateItemForSale(amount, id, id_shop, id_item):
        print(UPDATE_ITEM_FOR_SALE.format(amount, id+1, id_shop+1, id_item+1))

    def shopSoldItem(buyerID, sellerID, id_shop, id_item, amount):
        print(ITEM_WAS_BOUGHT_FROM_SHOP.format(buyerID+1, sellerID+1, id_shop+1, id_item+1, amount))

    def shopSoldItemToReturningCustomer(amount, buyer_id, seller_id, id_shop, id_item):
        print(ITEM_WAS_BOUGHT_AGAIN_FROM_SHOP.format(amount, buyer_id+1, seller_id+1, id_shop+1, id_item+1))


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
        # plt.pause(0.01)
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
        return random.choice(DESC_STARTERS) + " shop."
    
    def putItemForSale(self, iid, amount):
        if iid in self.for_sale:
            self.for_sale[iid]['amount'] += amount
            DBC.updateItemForSale(amount, self.owner.uid, self.id_shop, iid)
        else:
            self.for_sale[iid] = {}
            self.for_sale[iid]['bought'] = {}
            self.for_sale[iid]['amount'] = amount
            self.for_sale[iid]['price'] = random.randrange(5, 100) #TODO maybe make this in a way that the economy isn't random
            DBC.putItemForSale(self.owner.uid, self.id_shop, iid, self.for_sale[iid]['price'], amount)

    def playerPurchase(self, buyerID, iid, amount):
        self.for_sale[iid]['amount'] -= amount
        self.owner.balance += amount*self.for_sale[iid]['price']

        if 'bought' in self.for_sale[iid] and buyerID in self.for_sale[iid]['bought']:
            self.for_sale[iid]['bought'][buyerID] += amount
            DBC.shopSoldItemToReturningCustomer(amount, buyerID, self.owner.uid, self.id_shop, iid)
        else:
            self.for_sale[iid]['bought'][buyerID] = amount
            DBC.shopSoldItem(buyerID, self.owner.uid, self.id_shop, iid, amount)
        self.owner.level += 1


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
        self.level = 0

    def invIsFull(self):
        return len(self.inv) >= INV_SIZE

    def addToInv(self, item, amount):
        if item.id in self.inv:
            self.inv[item.id] += amount
            DBC.updateItemsInv(self.inv[item.id], self.uid, item.id)
        else:
            self.inv[item.id] = amount
            DBC.insertItemsInv(self.uid, item.id, amount)
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
        #TODO on death, respawn randomly
        if self.hp <= 0:
            DBC.playerKilled(self.uid, attacker.uid)
            self.position = (random.randrange(-game.max_size, game.max_size), random.randrange(-game.max_size, game.max_size))

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
                    shop.playerPurchase(self.uid, chosenItem, amount)
                    if chosenItem in self.inv:
                        self.inv[chosenItem] += amount
                    else:
                        self.inv[chosenItem] = amount
                    self.balance -= amount*shop.for_sale[chosenItem]['price']
                    self.level += 1

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
            p = Player(i, name, (x, y))
            self.players.append(p)
            DBC.insertPlayer(p)


    def genItems(self):
        allitemsHTML = requests.get('https://minecraft-ids.grahamedgecombe.com/').text

        items = re.findall('class="name">(.*?)<.*?class="text-id">\((.*?)\)</', allitemsHTML.replace("'", ""))

        self.items = {"population": [], "weights": []}
        for i in range(len(items)):
            item = Item(i, items[i][0], items[i][1])
            self.items['population'].append(item)
            self.items['weights'].append(random.random())
            DBC.insertItem(item)

    def genFactions(self):
        factions_string = '1. Mystique - (Mystic in French) 2. Vortex 3. Dynamic 4. Wintersong 5. Villigence 6. Revenge 7. Twisted 8. Kryptic 9. Komorebi - (The Light that seeks through the trees) 10. Twizzle 11. Ethreal 12. Aurora 13. Solitude 14. Echo 15. Twighlight 16. Dawn 17. NecoCrypt 18. Keepers 19. Guardians 20. Purge 21. Velocity 22. Desire 23. Nexus 24. Dimlight 25. Wicked 26. Nefarious - (another word for wicked) 27. Nemophilists - (hunters of the woods) 28. Ukiyo - (Living in the moment; floating world) 29. Exo 30. Mythic - (or just Myth) 31. Kalopsia 32. Irusu - (another word for hiding) 33. Silence 34. Demonic 35. Defiance 36. Enlightment 37. Yoisho - (A world without meaning) 38. Brinille - (a twig) 39. Fernweh 40. Fallen 41. Darkened 42. Elysian - (beautiful) 43. Fresco 44. Amazon 45. Avalanche 46. Nova 47. Bimyou - (not bad, "meh) 48. Savage 49. Resistance 50. Evolved'
        faction_names = re.findall(r".*?\. (.*?) (- \((.*?)\) |)", factions_string)

        self.factions = list()
        chosenLeaders = []
        for i in range(NUMBER_OF_FACTIONS):
            namearr = faction_names.pop()
            f = Faction(namearr[0], random.randrange(0, 12), (random.randrange(-MAX_SIZE, MAX_SIZE), random.randrange(-MAX_SIZE, MAX_SIZE)), (namearr[2] if namearr[2] != '' else 'This is our faction!'))
            leader = None
            while leader not in chosenLeaders:
                leader = random.choice(self.players)
                chosenLeaders.append(leader)
            f.members[leader] = leader
            chosenLeaders.append(leader)
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
                for i in range(3):
                    f = random.choice(self.factions)
                    if player.level >= f.entrance_level:
                        player.faction = f
                        f.members[player] = player
                        DBC.playerJoinFaction(player, f)
                        break
            
            if random.random() < SEND_MESSAGE_CHANCE:
                other = random.choice(self.players)
                if other != player:
                    DBC.sendMessage(player, other, random.choice(self.pmessages))


    def run(self):
        # self.graphics = Graphics(self.max_size)
        self.generateStart()
        for i in range(MAX_GENERATIONS):
            self.nextState()
            # self.graphics.drawState(self.players)


if __name__ == "__main__":
    # print(chr(27) + "[2J")
    game = Game(0, 0, MAX_PLAYERS, MAX_SIZE) #change with sys.argv
    game.run()