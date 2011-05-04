# Grooveshark Now Player Plugin for LED Notifier
# v1.0
# By Austin Philipp-Edmonds and Paulo Da Silva

#!/usr/bin/env python
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import json, thread

current_song = ''
current_artist = ''
has_notification = False

#Checks for change in song
def grooveshark_refresh():
    global has_notification
    if has_notification:
        has_notification = False
        return "%s by %s" % (current_song, current_artist)
    return None
    

class CustomHandler(BaseHTTPRequestHandler):

    def log_message(self, format, *args):
        return

    def update_song(self, song, artist):
        global current_song
        global current_artist
        global has_notification
        
        if song != current_song and artist != current_artist:
            current_song = song
            current_artist = artist
            has_notification = True
            #print "%s by %s" % (current_song, current_artist)

    def do_POST(self):
        try:
            if self.path.endswith("updateInfo"):
                infoLen = self.headers['Content-Length']
                info = self.rfile.read(int(infoLen))

                jsonObject = json.loads(info)
                
                if jsonObject['song']:
                    songName = jsonObject['song']['songName']
                    artistName = jsonObject['song']['artistName']
                    self.update_song(songName, artistName)

                self.send_response(200)
                self.end_headers()
                self.wfile.write(self)
        except IOError:
            self.send_error(405,'Method Not Allowed')

#Starts local server to allow JSON
def start_server():
    try:
            server = HTTPServer(('',2020),CustomHandler)
            print 'Server started'
            server.serve_forever()
    except KeyboardInterrupt:
            server.socket.close()
            print 'Server terminated'

thread.start_new_thread(start_server,())
