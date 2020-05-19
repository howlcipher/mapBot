def clearHost(self):
    self.host = "No host set"


def clearMaps(self):
    self.m1 = "No Map Set"
    self.m2 = "No Map Set"
    self.m3 = "No Map Set"

def clearMap(self, ctx, mapNum):
    mapNum = int(mapNum)
    if (mapNum == 1):
        self.m1 = "No Map Set"
    elif (mapNum == 2):
        self.m2 = "No Map Set"
    elif (mapNum == 3):
        self.m3 = "No Map Set"
    else:
        print(f"Invalid map number: {mapNum}")
