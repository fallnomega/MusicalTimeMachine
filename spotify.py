import spotipy
import os


class Spotty:
    def __init__(self):
        self.client_id = os.environ.get('CLIENT_ID')
        self.client_secret = os.environ.get('CLIENT_SECRET')
        self.scope = 'playlist-modify-private'
        self.auth_manager = spotipy.SpotifyOAuth(client_id=self.client_id, client_secret=self.client_secret,
                                                 redirect_uri='http://example.com', scope=self.scope)
        self.client = spotipy.Spotify(auth_manager=self.auth_manager)

    def create_playlists(self, timestamp):
        playlist_name = f"{timestamp} Billboard 100"
        temp = self.client.current_user()
        id = temp['id']
        new_playlist = self.client.user_playlist_create(user=id, name=playlist_name, public=False, collaborative=False,
                                                        description='Python learning task')
        return new_playlist

    def search_track(self, band, song, year):
        # print(f"Search: {band} - {song}")
        search_results = self.client.search(q=f"artist:{band} track:{song} year:{year}", type="track")
        try:
            song_uri = search_results['tracks']['items'][0]['id']
            return search_results['tracks']['items'][0]['id']
        except IndexError as error:
            print("*** No track found, skipping it ***")

    def add_track_to_playlist(self, track_uri, pl_id):
        self.client.playlist_add_items(playlist_id=pl_id, items=track_uri)
        return 0
