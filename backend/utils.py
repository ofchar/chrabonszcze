import random
import string


def getRandomString(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(length))
