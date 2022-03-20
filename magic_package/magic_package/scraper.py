
import requests
import re

import pandas as pd
from bs4 import BeautifulSoup
import tqdm

import lxml
import cchardet

IMDB_MAIN_URL = 'https://www.imdb.com'
IMDB_TOP_LIST_URL = 'https://www.imdb.com/chart/top/'

requests_session = requests.Session()


def convert_values(x):
    """Multiplier plus offst

    Args:
        x: str. Can  be a letter or a number. If a letter then convert to a number
                If a number, then multiply by 10 + x

    Returns:
        mulitplier: int
        offset: int
    """
    values = {
        'm': 10000000,
        'M': 10000000,
        'k': 1000,
        'K': 1000,
    }
    
    if x  in values:
        return values[x], 0 
    else:
        10, int(x) 
        
def get_url_to_soup(url) -> BeautifulSoup:
    r = requests_session.get(url)
    if r.status_code != 200:
        raise Exception('bad imdb')

    soup = BeautifulSoup(r.content, 'lxml')

    return soup
    
def get_top_n_url(n=20):
    soup = get_url_to_soup(IMDB_TOP_LIST_URL)
    
    #link_css_selector = '.article .lister table.chart tbody.lister-list tr td.titleColumn a[href]'
    link_css_selector = ' td.titleColumn a[href]'
    
    list_of_a_tags = soup.select(link_css_selector)
    
    result_link = [IMDB_MAIN_URL+link['href'] for link in list_of_a_tags[:20]]
    return result_link
    # return soup
    
def get_rating(soup:BeautifulSoup):
    rating_css_selector = 'div.ipc-button__text div div div[data-testid] span'
    spans = soup.select_one(rating_css_selector)
    return float(spans.text)
    
def get_number_of_rating(soup:BeautifulSoup):
    number_of_rating_css_selector = 'div.ipc-button__text div div div:nth-child(3)'
    div = soup.select_one(number_of_rating_css_selector)
    text_value = div.text.replace('.','.')
    front_value = float(text_value[:-1])
    back_value = text_value[-1]
    multi, offset = convert_values(back_value)
    return int(front_value * multi + offset)

def get_number_of_oscar(soup:BeautifulSoup):
    award_selector = 'section[cel_widget_id="StaticFeature_Awards"] div[data-testid="awards"] ul.ipc-metadata-list li[role="presentation"] a.ipc-metadata-list-item__label'
    award_a_tag = soup.select_one(award_selector)
    if award_a_tag:
        
        win_regex = 'Won [0-9]+ Oscar[s]*'
        text =  award_a_tag.text
        res = re.findall(win_regex, text)
        if not res:
            return 0
        number_regex = '[0-9]+'
        res = re.findall(number_regex, res[0])
       
        return str(res[0])
    return 0
def get_title(soup:BeautifulSoup):
    title_selector = 'div[data-testid="hero-title-block__original-title"]'
    title_div_tags = soup.select_one(title_selector)
    if title_div_tags:

        return title_div_tags.text.replace('Original title: ', '')
    else:
        title_selector = 'h1[data-testid="hero-title-block__title"]'
        title_h1_tags = soup.select_one(title_selector)
        return title_h1_tags.text



def get_data(n=20, verbose=0)->pd.DataFrame:
    urls = get_top_n_url(n)
    res = []
    if verbose:
        iterator = tqdm.tqdm(urls)
    else:
        iterator = urls
    for url in iterator:
        try:
            soup = get_url_to_soup(url)
            rating = get_rating(soup)
            number_of_rating = get_number_of_rating(soup)
            number_of_oscar = get_number_of_oscar(soup)
            title = get_title(soup)
            res.append([title, rating, number_of_rating, number_of_oscar])
            
        except Exception as e:
            print(url, 'is skipped :(')
    return pd.DataFrame(res, columns=['title', 'rating', 'n_rating', 'n_oscar'])

# if __name__ == '__main__':
#     get_data(verbose=1)

if __name__ == '__main__':
    import tqdm

    urls = get_top_n_url()
    # urls = ['https://www.imdb.com/title/tt0111161/']
    # urls = ['https://www.imdb.com/title/tt6241872'] # award but not oscar
    # urls = ['https://www.imdb.com/title/tt2713688'] #no award
    res = []
    for url in tqdm.tqdm(urls):
        try:
            soup = get_url_to_soup(url)
            rating = get_rating(soup)
            number_of_rating = get_number_of_rating(soup)
            number_of_oscar = get_number_of_oscar(soup)
            title = get_title(soup)
            res.append([title, rating, number_of_rating, number_of_oscar])

        except Exception as e:
            print(url, 'is skipped :(')
    pd.DataFrame(res, columns=['title', 'rating', 'n_rating', 'n_oscar']).to_csv('res.csv', sep='\t', header=True, index=False)