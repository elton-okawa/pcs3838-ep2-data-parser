import os

OUTPUT_DIR = "output"

def saveFile(dataset, filename, header):
    if not os.path.exists(OUTPUT_DIR):
        os.mkdir(OUTPUT_DIR)

    filepath = OUTPUT_DIR + '/' + filename

    output = open(filepath, "w")
    output.write(header)

    for row in dataset:
        output.write(','.join(row) + '\n')
    output.close()