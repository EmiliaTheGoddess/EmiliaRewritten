import urllib.request
import re
import webbrowser

def searchinyoutube(inputtext):
    search_keyword = inputtext
    search_keyword = urllib.parse.quote(inputtext)
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    print("https://www.youtube.com/watch?v=" + video_ids[0])
    webbrowser.open("https://www.youtube.com/watch?v=" + video_ids[0])