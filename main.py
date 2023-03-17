from bs4 import BeautifulSoup
import requests
import spotify

URL = 'https://www.billboard.com/charts/hot-100/'

# time_period = input("Pull music from which year you want to list to; provide it in this format: YYYY-MM-DD:  ")
time_period = '2000-08-12'
requestor = requests.get(url=f"{URL}{time_period}/")
requestor.raise_for_status()
soup = BeautifulSoup(requestor.text, 'html.parser')
the_hits_list = soup.find_all(class_="o-chart-results-list-row")

all_one_list = []
for x in the_hits_list:
    song_name = x.h3.get_text().replace('\n', '').replace('\t', '')
    artist_name = x.h3.next_sibling.next_sibling.get_text().replace('\n', '').replace('\t', '')
    ranking = x.span.get_text().strip('\n\t\n\t')
    all_one_list.append({"rank": ranking, "artist": artist_name, "song": song_name})

spot_client = spotify.Spotty()

spotify_uris = []
for x in all_one_list:
    spotify_uris.append(spot_client.search_track(x['artist'],x['song']))
# spot_client.search_track('Sisqo','Incomplete')
print(spotify_uris)



# spot_client.get_playlists()
