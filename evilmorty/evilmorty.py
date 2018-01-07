import requests
from bs4 import BeautifulSoup as bs

urls = ['http://rickandmorty.wikia.com/wiki/Pilot/Transcript',
 'http://rickandmorty.wikia.com/wiki/Rickmancing_the_Stone/Transcript',
 'http://rickandmorty.wikia.com/wiki/Rick_Potion_9/Transcript',
 'http://rickandmorty.wikia.com/wiki/Morty%27s_Mind_Blowers/Transcript',
 'http://rickandmorty.wikia.com/wiki/The_Real_Animated_Adventures_of_Doc_and_Mharti/Transcript',
 'http://rickandmorty.wikia.com/wiki/Meeseeks_and_Destroy/Transcript',
 'http://rickandmorty.wikia.com/wiki/The_Ricks_Must_Be_Crazy/Transcript',
 'http://rickandmorty.wikia.com/wiki/Big_Trouble_in_Little_Sanchez/Transcript',
 'http://rickandmorty.wikia.com/wiki/M._Night_Shaym-Aliens!/Transcript',
 'http://rickandmorty.wikia.com/wiki/Rixty_Minutes/Transcript',
 'http://rickandmorty.wikia.com/wiki/Raising_Gazorpazorp/Transcript',
 'http://rickandmorty.wikia.com/wiki/Something_Ricked_This_Way_Comes/Transcript',
 'http://rickandmorty.wikia.com/wiki/The_ABC%27s_of_Beth/Transcript',
 'http://rickandmorty.wikia.com/wiki/The_Whirly_Dirly_Conspiracy/Transcript',
 'http://rickandmorty.wikia.com/wiki/Rest_and_Ricklaxation/Transcript',
 'http://rickandmorty.wikia.com/wiki/Interdimensional_Cable_2:_Tempting_Fate/Transcript',
 'http://rickandmorty.wikia.com/wiki/A_Rickle_in_Time/Transcript',
 'http://rickandmorty.wikia.com/wiki/Alien:_Covenant_Rick_and_Morty/Transcript',
 'http://rickandmorty.wikia.com/wiki/Ricksy_Business/Transcript',
 'http://rickandmorty.wikia.com/wiki/Pickle_Rick/Transcript',
 'http://rickandmorty.wikia.com/wiki/Anatomy_Park_(episode)/Transcript',
 'http://rickandmorty.wikia.com/wiki/The_Rickshank_Rickdemption/Transcript',
 'http://rickandmorty.wikia.com/wiki/The_Ricklantis_Mixup/Transcript',
 'http://rickandmorty.wikia.com/wiki/Look_Who%27s_Purging_Now/Transcript',
 'http://rickandmorty.wikia.com/wiki/Total_Rickall/Transcript',
 'http://rickandmorty.wikia.com/wiki/Get_Schwifty/Transcript',
 'http://rickandmorty.wikia.com/wiki/Lawnmower_Dog/Transcript',
 'http://rickandmorty.wikia.com/wiki/Auto_Erotic_Assimilation/Transcript',
 'http://rickandmorty.wikia.com/wiki/The_Wedding_Squanchers/Transcript',
 'http://rickandmorty.wikia.com/wiki/Close_Rick-counters_of_the_Rick_Kind/Transcript',
 'http://rickandmorty.wikia.com/wiki/The_Rickchurian_Mortydate/Transcript',
 'http://rickandmorty.wikia.com/wiki/Mortynight_Run/Transcript',
 'http://rickandmorty.wikia.com/wiki/Vindicators_3:_The_Return_of_Worldender/Transcript']

# given a url:
def get_transcript(url):
    r = requests.get(url)
    content = r.content
    soup = bs(content, 'html.parser')
    transcript = soup.find('div', {'class':'poem'})
    return transcript