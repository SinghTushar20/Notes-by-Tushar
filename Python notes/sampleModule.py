print('Module imported successfully')
def findIndex(list, key):
    for i, value in enumerate(list):
        if value == key:
            return i
    return -1