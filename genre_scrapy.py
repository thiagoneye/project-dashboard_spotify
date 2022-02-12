"""
Musical genre identification by web scraping
"""

# Importações
import requests
from bs4 import BeautifulSoup

def genreScrapy(artistName, language):
    """Musical genre identification by web scraping.

    Syntax:
        genre = genreScrapy(artistName, language)

    Inputs:
        artistName - String containing the artist's name.
        language   - Search language string: 'portuguese' or 'english'.

    Outputs:
        genre - String containing the artist's genre.
    """
    # Data Manipulation
    artistName = artistName.replace(" ", "_")
    artistName = artistName.replace("&", "and")

    if (language == 'portuguese'):
        # HTML page scraping (non-nested data structure)
        wiki = "https://pt.wikipedia.org/wiki/"
        html = requests.get(wiki+artistName)

        # Create beautifulsoup document (nested data structure)
        soup = BeautifulSoup(html.content, 'html.parser')

        # Scraping
        try:
            genre = soup.find_all(class_='infobox infobox infobox_v2')[0]
            genre = genre.find_all('tr')

            for i in range(len(genre)):
                try:
                    value = genre[i].find(scope='row').get_text()[:9]
                    if value == 'Gênero(s)':
                        genre = genre[i].find_all('a')[1].get_text()
                        if (type(genre) == str):
                            get_value = True
                        else:
                            genre = soup.find_all(class_='infobox infobox infobox_v2')[0]
                            genre = genre.find_all('tr')
                            get_value = False
                except:
                    value = "It's not that"
        except:
            get_value = False

        if not get_value:
            genre = soup.find_all(class_='infobox infobox_v2')[0]
            genre = genre.find_all('tr')

            for i in range(len(genre)):
                try:
                    value = genre[i].find(scope='row').get_text()[:9]
                    if value == 'Gênero(s)':
                        genre = genre[i].find_all('a')[1].get_text()
                        if (type(genre) == str):
                            get_value = True
                        else:
                            genre = soup.find_all(class_='infobox infobox_v2')[0]
                            genre = genre.find_all('tr')
                            get_value = False
                except:
                    value = "It's not that"

    elif (language == 'english'):
        # HTML page scraping (non-nested data structure)
        wiki = "https://en.wikipedia.org/wiki/"
        html = requests.get(wiki+artistName)

        # Create beautifulsoup document (nested data structure)
        soup = BeautifulSoup(html.content, 'html.parser')

        # Scraping
        try:
            genre = soup.find_all(class_='infobox vcard plainlist')[0]
            genre = genre.find_all('tr')

            for i in range(len(genre)):
                try:
                    value = genre[i].find(scope='row').get_text()[:6]
                    if value == 'Genres':
                        genre = genre[i].find_all('a')[0].get_text()
                        if (type(genre) == str):
                            get_value = True
                        else:
                            genre = soup.find_all(class_='infobox vcard plainlist')[0]
                            genre = genre.find_all('tr')
                            get_value = False
                except:
                    value = "It's not that"
        except:
            get_value = False

        if not get_value:
            genre = soup.find_all(class_='infobox biography vcard')[0]
            genre = genre.find_all('tr')

            for i in range(len(genre)):
                try:
                    value = genre[i].find(scope='row').get_text()[:6]
                    if value == 'Genres':
                        genre = genre[i].find_all('a')[0].get_text()
                except:
                    value = "It's not that"

    if type(genre) != str:
        genre = 'Not found'

    return genre
