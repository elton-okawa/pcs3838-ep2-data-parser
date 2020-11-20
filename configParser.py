class Config:
    def __init__(self, name, tag, intervalSize):
        self.name = name
        self.tag = tag
        self.intervalSize = intervalSize

    def __str__(self):
        return "Name: {}, tag: {}, intervalSize: {}".format(self.name, self.tag, self.intervalSize)

def parseConfig(configFileName):
    file = open(configFileName, "r")
    config = []
    for line in file:
        parameters = line.split(", ")
        config.append(Config(parameters[0], parameters[1], int(parameters[2])))
    file.close()

    return config