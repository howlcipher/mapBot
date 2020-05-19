import random

from maps import availableMaps


# map class
class Maps:
    def __init__(self, m1: str, m2: str, m3: str, ct: str):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.ct = ct


# RANDOM MAPS
# random number 1 - x
def randomNumber(x):
    return random.randint(1, x)


def randomMapCount():
    return random.randint(3, 5)

# random number
def randomMaps(mapTotal):
    mapNums = {"map1": randomNumber(mapTotal),
               "map2": randomNumber(mapTotal),
               "map3": randomNumber(mapTotal)}
    return mapNums


# setting the map
def setMapRandom(mapcount=None):
    if (mapcount is not None):
        # set map
        mapcount = int(mapcount)
        if (mapcount == 3):
            mn = randomMaps(len(availableMaps.vsmapsdb3) - 1)
            return availableMaps.vsmapsdb3[mn["map1"]][0] + ": " + availableMaps.vsmapsdb3[mn["map1"]][
                1] + " MAP COUNT:" + availableMaps.vsmapsdb3[mn["map1"]][2]
        elif (mapcount == 4):
            mn = randomMaps(len(availableMaps.vsmapsdb4) - 1)
            return availableMaps.vsmapsdb4[mn["map1"]][0] + ": " + availableMaps.vsmapsdb4[mn["map1"]][
                1] + " MAP COUNT:" + availableMaps.vsmapsdb4[mn["map1"]][2]
        elif (mapcount == 5):
            mn = randomMaps(len(availableMaps.vsmapsdb5) - 1)
            return availableMaps.vsmapsdb5[mn["map1"]][0] + ": " + availableMaps.vsmapsdb5[mn["map1"]][
                1] + " MAP COUNT:" + availableMaps.vsmapsdb5[mn["map1"]][2]
        else:
            mn = randomMaps(len(availableMaps.vsmapsdb) - 1)
            return availableMaps.vsmapsdb[mn["map1"]][0] + ": " + availableMaps.vsmapsdb[mn["map1"]][
                1] + " MAP COUNT:" + availableMaps.vsmapsdb[mn["map1"]][2]
    else:
        mn = randomMaps(len(availableMaps.vsmapsdb) - 1)
        return availableMaps.vsmapsdb[mn["map1"]][0] + ": " + availableMaps.vsmapsdb[mn["map1"]][1] + " MAP COUNT:" + \
               availableMaps.vsmapsdb[mn["map1"]][2]


def randomMapFilter(self, mapcount1=None, mapcount2=None, mapcount3=None):
    m1 = mapcount1
    m2 = mapcount2
    m3 = mapcount3

    if (mapcount1 is not None):
        m1 = int(mapcount1)
        self.m1 = setMapRandom(m1)
    if (mapcount2 is not None):
        m2 = int(mapcount2)
        self.m2 = setMapRandom(m2)
    if (mapcount3 is not None):
        m3 = int(mapcount3)
        self.m3 = setMapRandom(m3)

    self.m1 = setMapRandom(m1)
    self.m2 = setMapRandom(m2)
    self.m3 = setMapRandom(m3)


# sets specific map - select the map and then the ID of the map
def setMap(self, mapNum, mapID):
    # set map
    if (int(mapNum) == 1):
        self.m1 = availableMaps.vsmapsdb[int(mapID) - 1][0] + ": " + availableMaps.vsmapsdb[int(mapID) - 1][
            1] + " MAP COUNT:" + availableMaps.vsmapsdb[int(mapID) - 1][2]
    if (int(mapNum) == 2):
        self.m2 = availableMaps.vsmapsdb[int(mapID) - 1][0] + ": " + availableMaps.vsmapsdb[int(mapID) - 1][
            1] + " MAP COUNT:" + availableMaps.vsmapsdb[int(mapID) - 1][2]
    if (int(mapNum) == 3):
        self.m3 = availableMaps.vsmapsdb[int(mapID) - 1][0] + ": " + availableMaps.vsmapsdb[int(mapID) - 1][
            1] + " MAP COUNT:" + availableMaps.vsmapsdb[int(mapID) - 1][2]
