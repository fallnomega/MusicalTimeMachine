import spotipy
import os


class Spotty:
    def __init__(self):
        self.client_id = os.environ.get('CLIENT_ID')
        self.client_secret = os.environ.get('CLIENT_SECRET')
        self.scope = 'playlist-read-private'
        self.auth_manager = spotipy.SpotifyOAuth(client_id=self.client_id, client_secret=self.client_secret,
                                                 redirect_uri='http://example.com', scope=self.scope)
        self.client = spotipy.Spotify(auth_manager=self.auth_manager)

    def get_playlists(self):
        # print(self.client.current_user())
        # self.search_track()
        return 0

    def search_track(self,band,song):
        # search_results = self.client.search(q="artist:Sisqo track:Incomplete", type="track")
        try:
            print(f"Search: {band} - {song}")
            search_results = self.client.search(q=f"artist:{band} track:{song} year:2000", type="track")
            song_uri = search_results['tracks']['items'][0]['id']
        except IndexError as error:
            print("*** No track found, skipping it ***")
            pass
        else:
            print(search_results['tracks']['items'][0]['id'])
            return search_results['tracks']['items'][0]['id']

