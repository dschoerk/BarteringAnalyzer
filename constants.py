import textdistance
import colorsys

N = 8
HSV_tuples = [(x*1.0/N, 0.5, 0.5) for x in range(N)]
RGB_tuples = list(map(lambda x: colorsys.hsv_to_rgb(x), HSV_tuples))


items = [
    "[Level 1] Ancient Urn Piece",
    "[Level 1] Cherry Tree Seed Pouch",
    "[Level 1] Chewy Raw Gizzard",
    "[Level 1] Dried Blue Rose",
    "[Level 1] Fertile Soil",
    "[Level 1] Giant Fish Bone",
    "[Level 1] Golden Sand",
    "[Level 1] Naval Ration",
    "[Level 1] Pirates' Gunpowder",
    "[Level 1] Raft Toy",
    "[Level 1] Rakeflower Seed Pouch",
    "[Level 1] Roa Flower Seed Pouch",
    "[Level 1] Stained Seagull Figurine",
    "[Level 1] Unidentified Ancient Mural",

    "[Level 2] Balanced Stone Pagoda",
    "[Level 2] Conch Shell Ornament",
    "[Level 2] Filtered Drinking Water",
    "[Level 2] Narvo Sea Cucumber",
    "[Level 2] Pirate Gold Coin",
    "[Level 2] Urchin Spine",
    "[Level 2] Monster Tentacle",
    "[Level 2] Big Stone Slab",
    "[Level 2] Opulent Marble",
    "[Level 2] Pirate Ship Mast",
    "[Level 2] Sea Survival Kit",
    "[Level 2] Suzpreme Oyster Box",
    "[Level 2] Cron Castle Gold Coin",
    "[Level 2] Islanders' Lunchbox",

    "[Level 3] Lopters Fishnet",
    "[Level 3] Skull Symbol Carpet",
    "[Level 3] Pirates' Supply Box",
    "[Level 3] Tom Pirate Treasure Map",
    "[Level 3] Weasel Leather Coat",
    "[Level 3] Scount Binoculars",
    "[Level 3] Old Hourglass",
    "[Level 3] Ancient Orders",
    "[Level 3] Blue Candle Bundle",
    "[Level 3] Gooey Monster Blood",
    "[Level 3] Stalactite Fragment",
    "[Level 3] Skull Decorated Teacup",
    "[Level 3] Rare Herb Pile",
    "[Level 3] Round Knife",

    "[Level 4] Amethyst Fragment",
    "[Level 4] Marine Knights' Spear",
    "[Level 4] Bronze Candlestick",
    "[Level 4] Green Salt Lump",
    "[Level 4] Headless Dragon Figurine",
    "[Level 4] Opulent Thread Spool",
    "[Level 4] Panacea",
    "[Level 4] Pirate's Key",
    "[Level 4] Solidified Lava",
    "[Level 4] Stolen Pirate Dagger",
    "[Level 4] Seashell Deco",
    "[Level 4] Old Chest with Gold Coins",
    "[Level 4] Boatman's Manual",
    "[Level 4] Marine Knight's Helm",

    "[Level 5] 102 Year Old Golden Herb",
    "[Level 5] 37 Year Old Herbal Wine",
    "[Level 5] Azure Quartz",
    "[Level 5] Cox Pirate's Journal",
    "[Level 5] Elixir of Youth",
    "[Level 5] Faded Golden Dragon Figurine",
    "[Level 5] Golden Fish Scale",
    "[Level 5] Luxury Patterned Fabric",
    "[Level 5] Mysterious Rock",
    "[Level 5] Observatory Report",
    "[Level 5] Octagonal Box",
    "[Level 5] Opulent Coral Trinket",
    "[Level 5] Otters Fish Hook",
    "[Level 5] Portrait of the Ancient",
    "[Level 5] Rust Repair Tool",
    "[Level 5] Statue's Tear",
    "[Level 5] Supreme Gold Candlestick",
    "[Level 5] Taxidermied Morpho Butterfly",
    "[Level 5] Taxidermied White Caterpillar",

    "Sea Coin",
    "Great Ocean Dark Iron",
    "Frosted Black Stone",
    "Deep Sea Memory Filled Glue",
    "Island Tree Coated Plywood",
    "Bright Reef Piece",

    "Acacia Sap", 
    "Aloe", 
    "Bag of Muddy Water", 
    "Beer", 
    "Big Arrow Mushroom", 
    "Bloody Tree Knot", 
    "Cactus Rind", 
    "Cedar Plank", 
    "Cloud Mushroom", 
    "Clown's Blood", 
    "Coal", 
    "Copper Ingot", 
    "Elder Tree Plank", 
    "Elder Tree Sap", 
    "Essence of Liquor", 
    "Feather Wolf Hide", 
    "Flax", 
    "Flax Fabric", 
    "Flax Thread", 
    "Fortune Teller Mushroom", 
    "Fruit of Abundance", 
    "Fruit of Destruction", 
    "Fruit of Magic Power", 
    "Fruit of Nature", 
    "Fruit of Perfection", 
    "Grilled Bird Meat", 
    "Ground Bird Meat", 
    "Knitting Yarn", 
    "Landscape Painting of a Tree", 
    "Landscape Painting of Demi River", 
    "Landscape Painting of Foggy Serendia", 
    "Lead Ore", 
    "Log", 
    "Loopy Tree Plank", 
    "Melted Iron Shard", 
    "Monk's Branch", 
    "Noc Ore", 
    "Nutmeg", 
    "Old Tree Bark", 
    "Pile of Sunrise Herbs", 
    "Pistachio", 
    "Powder of Crevice", 
    "Powder of Darkness", 
    "Powder of Earth", 
    "Powder of Flame", 
    "Powder of Time", 
    "Processed Coal", 
    "Purified Water", 
    "Red Tree Lump", 
    "Rough Black Crystal", 
    "Rough Blue Crystal", 
    "Rough Green Crystal", 
    "Rough Mud Crystal", 
    "Rough Red Crystal", 
    "Rough Stone", 
    "Rough Violet Crystal", 
    "Silkworm Cocoon", 
    "Silver Azalea", 
    "Sinner's Blood", 
    "Soft Ferri Feather", 
    "Spirit's Leaf", 
    "Star Anise", 
    "Strawberry", 
    "Thick Meat Stew", 
    "Velia Watchtower and Cron Castle Landscape", 
    "Vinegar", 
    "Violet Crystal", 
    "Wheat", 
    "White Cedar Sap", 
    "Wild Grass", 
    "Wolf Hide", 
    "Wool"
]

islands = [
    ("Teyamal Island", 572, 404),
    ("Rameda Island", 614, 89),
    ("Theonil  Island", 710, 229),
    ("Modric Island", 772, 288),
    ("Baeza Island", 873, 335),
    ("Ginburrey Island", 831, 110),
    ("Randis Island", 1072, 247),
    ("Serca Island", 1066, 332),
    ("Daton Island", 861, -117),
    ("Netnume Island", 951, -44),
    ("Oben Island", 1038, -90),
    ("Dunde Island", 1080, 6),
    ("Eberdeen Island", 1154, -29),
    ("Albresser Island", 1261, 29),
    ("Barater Island", 1277, 122),
    ("Teste Island", 912, -427),
    ("Almai Island", 1031, -556),
    ("Padix Island", 1193, -407),
    ("Kuit Island", 1195, -744),
    ("Arita Island", 1581, -571),
    ("Staren Island", 1549, -97),
    ("Louruve Island", 1674, -191),
    ("Lisz Island", 1601, -305),
    ("Marka Island", 1780, -238),
    ("Narvo Island", 1776, -408),
    ("Tashu Island", 1996, -886),
    ("Lema Island", 2226, -766),
    ("Orffs Island", 2233, -530),
    ("Tulu Island", 2120, -515),
    ("Invernen Island", 1992, -436),
    ("Balvege Island", 2097, -303),
    ("Marlene Island", 2202, -302),
    ("Angie Island", 1963, -204),
    ("Eveto Island", 2126, -142),
    ("Duch Island", 2091, -97),
    ("Luivano Island", 2272, -3),
    ("Ephde Rune Island", 2453, 54),
    ("Mariveno Island", 2336, -157),
    ("Paratama Island", 2581, -97),
    ("Weita Island", 2563, -271),
    ("Baremi Island", 2452, -389),
    ("Ajir Island", 2692, -508),
    ("Al-Naha Island", 2557, -671),
    ("Racid Island", 2672, -807),
    ("Kanvera Island", 2718, -215),
    ("Arakil Island", 2770, -151),
    ("Ostra Island", 2928, -104),
    ("Taramura Island", 2885, -39),
    ("Beiruwa Island", 2727, 54),
    ("Iliya Island", 2984, -391),
    ("Tinberra Island", 3200, -1234),
    ("Lerao Island", 3376, -1201),
    ("Portanen Island", 3456, -1003),
    ("Shasha Island", 3368, -823),
    ("Rosevan Island", 3523, -828),
    ("Delinghart Island", 3156, -70),
    ("Pilava Island", 3332, -40),
    ("Sokota Island", 3592, 148),
    ("Riyed Island", 3820, -4),
    ("Boa Island", 3911, -679),
    ("Orisha Island", 3907, -508),
    ("Tigris Island", -274, 0),
    ("Shirna Island", 4001, -288),
    ("Esfah Island", 3920, -207),
    ("Halmad Island", 4404, -542),
    ("Kashuma Island", 4511, -680),
    ("Derko Island", 5409, -832),
    ("Hakoven Island", 6856, -1298),

    ("Shipwrecked Cargoship", -300, -1744),
    ("Incomplete Ship", -300, -1744),
    ("Latinia's Combat Raft", -300, -1744),
    ("Old Moon Guild Carrack", -300, -1744),
]

def findClosest(txt, collection, collection_transformer=None, max_chars = None):
    best_score = 99999
    for item in collection:

        if collection_transformer is not None:
            item = collection_transformer(item)

        #print(item)

        item_comp = item
        if max_chars is not None:
            item_comp = item[:max_chars]

        d = textdistance.levenshtein(txt, item_comp)

        if d < best_score:
            best_score = d
            best_item = item
    
    return best_item, best_score

def findClosestItem(txt, max_chars = None):
    return findClosest(txt, items, max_chars = max_chars)

def findClosestIsland(txt, max_chars = None, collection_transformer = lambda x: x[0]):
    return findClosest(txt, islands, collection_transformer = collection_transformer, max_chars = max_chars)

def transformIslandCoordinatesToScreen(x,y):
    x = x + 300
    y = y + 1400
    x = x * 0.3
    y = y * 0.3
    return (int(x),int(y))

def getIslandCoordinates(islandName):
    for i in islands:
        if i[0] == islandName:
            return (i[1], i[2])

def drawMap(paths):
    import cv2
    import numpy as np

    img = np.zeros((600, 1600, 3))

    for path in paths:
        def getCoords(island):
            (x,y) = getIslandCoordinates(island)
            (x,y) = transformIslandCoordinatesToScreen(x,y)
            return (x,y)

        (sx,sy) = getCoords(path.a)
        (ex,ey) = getCoords(path.b)

        img = cv2.line(img, (sx,sy), (ex,ey), RGB_tuples[path.col], 2) 

    for island in islands:
        (x,y) = transformIslandCoordinatesToScreen(island[1], island[2])
        img = cv2.putText(img, island[0], (int(x),int(y)), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (255,255,255), 1, cv2.LINE_AA) 

    cv2.imshow("", img)
    cv2.waitKey()

