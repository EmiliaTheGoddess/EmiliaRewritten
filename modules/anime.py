import webbrowser

def openmal(searchstring):
    webbrowser.open("https://myanimelist.net/search/all?q={}&cat=all".format(searchstring))