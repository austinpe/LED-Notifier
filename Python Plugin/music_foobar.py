import urllib
import BeautifulSoup
song_id_initial = BeautifulSoup.BeautifulSoup(urllib.urlopen("http://127.0.0.1:8888/default/"))
def foobar_refresh():
        global song_id_initial
        song_id_current = BeautifulSoup.BeautifulSoup(urllib.urlopen("http://127.0.0.1:8888/default/"))
        if song_id_current.title.string != None and song_id_current.title.string != song_id_initial.title.string:
                song_id_initial = BeautifulSoup.BeautifulSoup(urllib.urlopen("http://127.0.0.1:8888/default/"))
                return song_id_current.title.string
        return None
     
        

