#grass types
class grass_chums:
    def __init__(self, name, basehp, attk, emoji):
        self.name = name
        self.basehp = basehp
        self.attk = attk
        self.emoji = emoji

mosshare = grass_chums("Mosshare", 105, 45, "🌿")
barksprout = grass_chums("Barksprout", 120, 40, "🌱")
florawing = grass_chums("Florawing", 85, 55, "🌸")
thorncrest = grass_chums("Thorncrest", 95, 60, "🌾")

#fire types
class fire_chums:
    def __init__(self, name, basehp, attk, emoji):
        self.name = name
        self.basehp = basehp
        self.attk = attk
        self.emoji = emoji

blazepaw = fire_chums("Blazepaw", 90, 70, "🔥")
cineflare = fire_chums("Cineflare", 80, 80, "🔥")
pyregoat = fire_chums("Pyregoat", 100, 65, "🔥")
flintbeak = fire_chums("Flintbeak", 85, 75, "🔥")

#water types
class water_chums:
    def __init__(self, name, basehp, attk, emoji):
        self.name = name
        self.basehp = basehp
        self.attk = attk
        self.emoji = emoji

aquaquake = water_chums("Aquaquake", 95, 60, "💧")
puddleduck = water_chums("Puddleduck", 100, 55, "🦆")
finsplash = water_chums("Finplash", 85, 70, "🐟")
mistfrog = water_chums("Mistfrog", 90, 65, "🐸")

#electric types
class electric_chums:
    def __init__(self, name, basehp, attk, emoji):
        self.name = name
        self.basehp = basehp
        self.attk = attk
        self.emoji = emoji

sparkram = electric_chums("Sparkram", 80, 75, "⚡")
boltleap = electric_chums("Boltleap", 85, 70, "⚡")
Thunderpup = electric_chums("Thunderpup", 90, 65, "⚡")

#earth types
class earth_chums:
    def __init__(self, name, basehp, attk, emoji):
        self.name = name
        self.basehp = basehp
        self.attk = attk
        self.emoji = emoji

boulderpug = earth_chums("Boulderpug", 110, 50, "🪨")
ironmole = earth_chums("Ironmole", 120, 45, "🕳️")

#psychic types
class psychic_chums:
    def __init__(self, name, basehp, attk, emoji):
        self.name = name
        self.basehp = basehp
        self.attk = attk
        self.emoji = emoji

mindmelter = psychic_chums("Mindmelter", 90, 70, "🧠")
psifox = psychic_chums("Psifox", 85, 75, "🧠")

class Legendary_chums:
    def __init__(self, name, basehp, attk, emoji):
        self.name = name
        self.basehp = basehp
        self.attk = attk
        self.emoji = emoji

solaris = Legendary_chums("Solaris", 150, 90, "☀️")        
jade_dragon = Legendary_chums("Jade Dragon", 140, 95, "🐉")
grimshadow = Legendary_chums("Grimshadow", 130, 100, "👻")
aurorafang = Legendary_chums("AuroraFang",180, 90, "✨")

starter_chums = [mosshare, blazepaw, puddleduck]

class inventory:
    def __init__(self):
        self.items = {
            "Chum Ball": 10,
            "Potion": 0,
            "Super Potion": 0,
            "Revive": 0,
        }

        self.chums = []
        self.money = 100
        self.badges = 0

    def add_item(self, item):
        self.items[item] += 1

    def remove_item(self, item):
        if item in self.items:
            self.items[item] -= 1

    def add_chum(self, chum):
        self.chums.append(chum)

    def remove_chum(self, chum):
        if chum in self.chums:
            self.chums.remove(chum)

numbers = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20 ,21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
    41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60 ,61, 62, 63, 64, 65, 66, 67, 68, 69, 70,
     71, 72, 73, 74, 75, 76, 77, 78, 79 ,80 ,81 ,82 ,83 ,84 ,85 ,86 ,87 ,88 ,89 ,90 ,91 ,92 ,93 ,94 ,95 ,96 ,97 ,98 ,99 ,100
           ]

encounter = [
    mosshare, barksprout, florawing, thorncrest, blazepaw, cineflare, pyregoat, flintbeak, aquaquake, puddleduck, finsplash, mistfrog, sparkram, boltleap, boulderpug, ironmole, mindmelter, psifox, Thunderpup
]

legendary_encounter = [solaris, jade_dragon, grimshadow, aurorafang]