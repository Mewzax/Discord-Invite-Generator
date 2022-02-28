def saveCodes(code, file):
    with open(file, 'a') as f:
        f.write(code + '\n')
        f.close()

def generateCode():
    code = 'mantle'
    return code