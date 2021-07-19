from modules import play
from modules import anime


def checklength(x):
    return len(x)


def checkifcontains(search, inputstring):
    if search in inputstring[0:checklength(search) + 1]:
        return True
    else:
        return False


def removecommand(command, inputstring):
    return inputstring[(checklength(command) + 1):]


def check(text):
    text = text.lower()

    if checkifcontains('play', text):
        text = removecommand('play', text)
        play.searchinyoutube(text)

    elif checkifcontains('anime', text):
        text = removecommand('anime', text)
        anime.openmal(text)
