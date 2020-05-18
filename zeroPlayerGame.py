#TODO: git init

import random
import re
import requests

import matplotlib.pyplot as plt

import time

import math  

# FINE TUNING PARAMETERS
MAX_RANDOM_ADD_ITEMS = 30
MAX_MOVE_IN_DIRECTION = 15
PLAYER_DEFAULT_HEALTH = 100
INV_SIZE = 36

MAX_GENERATIONS = 100
MAX_PLAYERS = 50
MAX_SIZE = 200

MIN_DISTANCE_BETWEEN_SHOPS = MAX_SIZE / 4

# DATABASE STRINGS
INSERT_PLAYERS = "insert into players(name) values('{}');"
INSERT_ITEMS = "insert into items(item_name, item_description) values ('{}', '{}');"

PUT_ITEMS_INV = "upsert into inventory values ({}, {}, {});"

CREATE_SHOP = 'insert into shops(id, coordinates, shop_header) values ({}, {}.{}, "{}");'

PLAYER_KILLED = 'insert into kills({}, {});'

# FLAIR STRINGS
DESC_STARTERS = ["A normal", "An ordinary", "Simple", "A standard", "Your standard", "A cool looking", "An awesome", "A pretty cool", "Default", "An elementary", "Your usual", "A usual", "An everyday", "Your everyday", "An average looking", "An average", "A conventional", "Your average", "An OK", "A vanilla", "Unique", "A common", "Mainstream", "Your typical", "A typical", "A modest", "A neat", "A bland", "A serious looking", "A decent looking", "A decent", "Pretty nice", "A nice", "An undemanding", "A manageable", "An effortless", "A user-friendly", "A coherent", "An understandable", "An accessible", "Standard", "A basic", "A blunt", "Pure", "Candid", "Some honest", "Some demanding", "A piece of cake but it's actually", "You wish it'd make sound but it doesn't. Your", "Show it to your friends. Your", "Go crazy with this", "Looks better than you, a good", "But does it fly? A simple", "How will you explain this? Your cool", "A magnificient", "You can't drive it, it's a non-drivable", "A sarcastic", "Funny looking", "Has no wheels, but it's a decent", "A beautiful", "Looks better than your ex, but you're just holding one more", "How did you even get this", "A rare", "One more", "Close your eyes again, it's still just one more", "A f*cking"]

# CODE
originalprint = print
def print(string, end="\n"):
    originalprint(string, end=end)
    # time.sleep(0.01)

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
    def __init__(self, owner_id, id_shop, position, owner_name):
        self.owner_id = owner_id
        self.owner_name = owner_name
        self.id_shop = id_shop
        self.position = position
        self.shop_header = self.makeShopHeader()
        self.for_sale = []
    
    def makeShopHeader(self):
        return random.choice(DESC_STARTERS) + " shop."


class Player:
    def __init__(self, uid, name, position):
        self.hp = PLAYER_DEFAULT_HEALTH
        self.uid = uid
        self.name = name
        self.position = position
        self.balance = 100
        self.inv = {}
        self.shops = []

    def invIsFull(self):
        return len(self.inv) >= INV_SIZE

    def addToInv(self, item, amount):
        if item.id in self.inv:
            self.inv[item.id] += amount
        else:
            self.inv[item.id] = amount
        print(PUT_ITEMS_INV.format(self.uid, item.id, amount)) #TODO: Uncomment 
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
            newShop = Shop(self.uid, len(self.shops), self.position, self.name) #TODO: saber se a base de dados começa a sequencia em 1 ou 0, se for 1 é preciso mudar esta linha para baixo da outra
            print(CREATE_SHOP.format(newShop.owner_id, newShop.position[0], newShop.position[1], newShop.shop_header)) #TODO uncomment
            self.shops.append(newShop)

    def receiveHit(self, dmg, attacker, game):
        self.hp -= dmg
        #TODO on death, respawn randomly
        if self.hp <= 0:
            print(PLAYER_KILLED.format(self.uid, attacker.uid))
            self.position = (random.randrange(-game.max_size, game.max_size), random.randrange(-game.max_size, game.max_size))

    def interactWithNeighbour(self, nb, game):
        if nb != self:
            if isinstance(nb, Shop):
                if nb.owner_id != self.uid:
                    # print("{} buying from {}'s shop".format(self.name, nb.owner_name))
                    pass
            if isinstance(nb, Player) and random.random() < 0.5:
                hitDmg = random.randrange(1, 20)
                # print("{} deals {} damage to {}".format(self.name, hitDmg, nb.name))
                nb.receiveHit(hitDmg, self, game)

    def interactwithNeighbours(self, game):
        for i in range(-3, 4):
            for j in range(-3, 4):
                if i != 0 or j != 0:
                    if (self.position[0] + i, self.position[1] + j) in game.gameMap:
                        self.interactWithNeighbour(game.gameMap[(self.position[0]+i, self.position[1]+j)], game)


class Game:
    def __init__(self, rules, max_iterations, max_players, max_size):
        self.rules = rules
        self.max_iterations = max_iterations
        self.max_players = max_players
        self.max_size = max_size

    def genPlayers(self):
        names = set()
        names.update(map(lambda e: e.replace("_", "").replace('-', ""), requests.get("http://names.drycodes.com/{}?nameOptions=starwarsFirstNames&combine=2&case=lower".format(self.max_players)).json()))
        names.update(map(lambda e: e.replace("_", "").replace('-', ""), requests.get("http://names.drycodes.com/{}?nameOptions=starwarsLastNames&combine=2".format(self.max_players)).json()))
        names.update(map(lambda e: e.replace("_", ""), requests.get("http://names.drycodes.com/{}?nameOptions=girl_names&combine=1&case=lower".format(self.max_players)).json()))
        names.update(map(lambda e: e.replace("_", ""), requests.get("http://names.drycodes.com/{}?nameOptions=boy_names&combine=1&case=lower".format(self.max_players)).json()))
        names.update(map(lambda e: e.replace("_", "").replace('.', ""), requests.get("http://names.drycodes.com/{}?nameOptions=presidents&combine=1".format(self.max_players)).json()))
        names.update(map(lambda e: e.replace("_", ""), requests.get("http://names.drycodes.com/{}?nameOptions=cities&combine=1&case=lower".format(self.max_players)).json()))
        self.players = list()
        for i in range(self.max_players):
            x = random.randrange(-self.max_size, self.max_size)
            y = random.randrange(-self.max_size, self.max_size)
            name = names.pop()
            p = Player(i, name, (x, y))
            self.players.append(p)
            print(INSERT_PLAYERS.format(p.name)) #TODO uncomment


    def genItems(self):
        allitemsHTML = requests.get('https://minecraft-ids.grahamedgecombe.com/').text

        items = re.findall('class="name">(.*?)<.*?class="text-id">\((.*?)\)</', allitemsHTML)

        self.items = {"population": [], "weights": []}
        for i in range(len(items)):
            item = Item(i, items[i][0], items[i][1])
            self.items['population'].append(item)
            self.items['weights'].append(random.random())
            print(INSERT_ITEMS.format(item.name, item.desc)) #TODO uncomment

    def generateStart(self):
        self.genPlayers()
        self.genItems()

    def printPlayerInventories(self):
        for p in self.players:
            for iid, amount in p.inv.items():
                print("{} has {} of {}.".format(p.name, amount, self.items["population"][iid].name))

    def nextState(self):
        self.gameMap = dict()
        for player in self.players:
            self.gameMap[player.position] = player
            for shop in player.shops:
                self.gameMap[shop.position] = shop
                
        chosenItems = random.choices(population=self.items["population"], weights=self.items["weights"], k=len(self.players))
        for i, player in enumerate(self.players):
            if random.random() <= 0.5 and not player.invIsFull(): #TODO limit inv size?
                #TODO make items have different chances of being obtained. Dirt is more likely than gold
                player.addToInv(chosenItems[i], random.randrange(1, MAX_RANDOM_ADD_ITEMS))
            player.moveSomewhere(self)
            player.thinkOfCreatingShop(self)
            player.interactwithNeighbours(self)

    def run(self):
        self.graphics = Graphics(self.max_size)
        self.generateStart()
        for i in range(MAX_GENERATIONS): #change with sys.argv
            self.nextState()
            self.graphics.drawState(self.players)
#            input()


if __name__ == "__main__":
    print(chr(27) + "[2J")
    game = Game(0, 0, MAX_PLAYERS, MAX_SIZE) #change with sys.argv
    game.run()
