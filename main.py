import sys
import configParser
import dataParser
import printUtil
import dataUtil

CONFIG_FILE_FORMAT = '{}-{}'
DATASET_FILE_FORMAT = '{}-{}.{}'

def main():
    if len(sys.argv) != 5:
        raise Exception("Error, expecting arguments <datasetFileName> <configFileName> <configVersion> <shouldReturnIntervalOutput>")

    datasetFileName = sys.argv[1]
    configFileName = sys.argv[2]
    configVersion = int(sys.argv[3])
    if sys.argv[4].lower() == 'false':
        shouldReturnIntervalOutput = False
    else:
        shouldReturnIntervalOutput = True

    config = configParser.parseConfig(CONFIG_FILE_FORMAT.format(configFileName, configVersion))
    printUtil.printObjectList(config, "Using config:")
    (header, data) = dataParser.parseData(datasetFileName, config, shouldReturnIntervalOutput)
    dataUtil.saveFile(data, DATASET_FILE_FORMAT.format('dataset', configVersion, 'data'))
main()