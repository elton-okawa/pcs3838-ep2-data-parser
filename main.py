import sys
import configParser
import dataParser
import printUtil
import dataUtil

def main():
    if len(sys.argv) != 4:
        print("Error, expecting arguments <datasetFileName> <configFileName> <shouldReturnIntervalOutput>")

    datasetFileName = sys.argv[1]
    configFileName = sys.argv[2]
    if sys.argv[3].lower() == 'false':
        shouldReturnIntervalOutput = False
    else:
        shouldReturnIntervalOutput = True

    config = configParser.parseConfig(configFileName)
    printUtil.printObjectList(config, "Using config:")
    (header, data) = dataParser.parseData(datasetFileName, config, shouldReturnIntervalOutput)
    dataUtil.saveFile(data, "dataset.data", header)
main()