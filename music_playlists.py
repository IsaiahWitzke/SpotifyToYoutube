import sys
import os
import spotipy
import spotipy.util as util

scope = 'user-library-read'

os.system("export SPOTIPY_CLIENT_ID='aae63f05cceb4e8d87386f8ade1eed52'")
os.system("export SPOTIPY_CLIENT_SECRET='67338d34cf894ddcb65e5eb0f1b41b05'")
os.system("export SPOTIPY_REDIRECT_URI='localhost'")

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print("Usage: %s username" % (sys.argv[0],))
    sys.exit()

token = util.prompt_for_user_token(username, scope)

if token:
    sp = spotipy.Spotify(auth=token)
    results = sp.current_user_saved_tracks()
    for item in results['items']:
        track = item['track']
        print(track['name'] + ' - ' + track['artists'][0]['name'])
else:
    print("Can't get token for", username)
'''
birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
spotify = spotipy.Spotify()

util.prompt_for_user_token(username,scope,client_id='your-spotify-client-id',client_secret='your-spotify-client-secret',redirect_uri='your-app-redirect-url')


results = spotify.artist_albums(birdy_uri, album_type='album')
albums = results['items']
while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'])
'''
