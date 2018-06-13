def readFile(filePath):
    fileObj = open(filePath, 'r')
    text = fileObj.read()
    return text


