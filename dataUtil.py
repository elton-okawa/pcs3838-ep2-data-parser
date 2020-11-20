def saveFile(dataset, filename, header):
    filepath ="output/" + filename

    output = open(filepath, "w")
    output.write(header)

    for row in dataset:
        output.write(','.join(row) + '\n')
    output.close()