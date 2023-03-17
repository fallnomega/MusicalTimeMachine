from bs4 import BeautifulSoup
import requests

URL = 'https://www.billboard.com/charts/hot-100/'
# time_period = input("Pull music from which year you want to list to; provide it in this format: YYYY-MM-DD:  ")
testing_time_period = '2000-08-12'

# url example = https://www.billboard.com/charts/hot-100/2000-08-12/

requestor = requests.get(url=f"{URL}{testing_time_period}/")
requestor.raise_for_status()
soup = BeautifulSoup(requestor.text, 'html.parser')
# print(soup.prettify())

artist_html = soup.find_all(name="div", class_='o-chart-results-list-row-container')
# artists = [band.getText().strip('\n\t\n\t') for band in artist_html]
# print(artist_html)
for x in artist_html:
    print(x)
ranking = soup.find_all(name="li", class_='o-chart-results-list__item // lrv-u-background-color-black '
                                            'lrv-u-color-white u-width-100 u-width-55@mobile-max '
                                            'u-width-55@tablet-only lrv-u-height-100p lrv-u-flex '
                                            'lrv-u-flex-direction-column@mobile-max lrv-u-flex-shrink-0 '
                                            'lrv-u-align-items-center lrv-u-justify-content-center lrv-u-border-b-1 '
                                            'u-border-b-0@mobile-max lrv-u-border-color-grey')
rank_cleanup = [rank.getText().strip('\n\t\n\t') for rank in ranking]
print(rank_cleanup)

all_one_list = {}
# for x in range(len(artists)-1):
#     all_one_list.update({'rank':rank})



# for x in artists:
#     x = x.strip("\n\t\n\t")
#     print(x)
# stripped = [s.strip('\n\t\n\t') for s in artists]
# print(stripped)

