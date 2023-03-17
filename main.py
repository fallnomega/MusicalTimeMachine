from bs4 import BeautifulSoup
import requests
URL = 'https://www.billboard.com/charts/hot-100/'
# url example = https://www.billboard.com/charts/hot-100/2000-08-12/

# time_period = input("Pull music from which year you want to list to; provide it in this format: YYYY-MM-DD:  ")
testing_time_period = '2000-08-12'
requestor = requests.get(url=f"{URL}{testing_time_period}/")
requestor.raise_for_status()
soup = BeautifulSoup(requestor.text, 'html.parser')
the_hits_list = soup.find_all(class_="o-chart-results-list-row")


all_one_list = []
for x in the_hits_list:
    song_name = x.h3.get_text().replace('\n', '').replace('\t', '')
    artist_name = x.h3.next_sibling.next_sibling.get_text().replace('\n', '').replace('\t', '')
    ranking = x.span.get_text().strip('\n\t\n\t')
    # print(f"{ranking}: {artist_name} - {song_name}")
    all_one_list.append({"rank": ranking, "artist": artist_name, "song":song_name})

for x in all_one_list:
    print (x)



