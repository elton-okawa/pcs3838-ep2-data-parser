def parseData(dataFileName, configList, shouldReturnIntervalOutput):
    file = open(dataFileName, "r")
    data = []

    header = file.readline()
    next(file)
    for line in file:

        row = []
        parameters = line.split(",")

        if len(parameters) != len(configList):
            raise AttributeError("Number of config defined intervals is less than dataset's number of columns")

        for i in range(len(parameters)):
            param = int(parameters[i])
            config = configList[i]

            row.append(parseParameter(param, config, shouldReturnIntervalOutput))

        data.append(row)
    file.close()

    return (header, data)

def parseParameter(param, config, shouldReturnIntervalOutput):
    value = int(param / config.intervalSize)
    if shouldReturnIntervalOutput:
        return '{}_{}-{}'.format(config.tag, int(value * config.intervalSize), int((value + 1) * config.intervalSize))
    else:
        return str(value)