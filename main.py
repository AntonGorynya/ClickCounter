import requests
import argparse
from urllib.parse import urlparse
from os import environ
from dotenv import load_dotenv


CLICK_URL = 'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary'
SHORTEN_URL = 'https://api-ssl.bitly.com/v4/shorten'
RETRIEVE_URL = 'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}'


def shorten_url(long_url, token):
    response = requests.post(
        SHORTEN_URL,
        json={'long_url': long_url},
        headers={'Authorization': token}
    )
    response.raise_for_status()
    return response.json()['link']


def count_clicks(short_url, token):
    parsed_url = urlparse(short_url)
    short_url = '{netloc}{path}'.format(
        netloc=parsed_url.netloc,
        path=parsed_url.path
    )
    response = requests.get(
        CLICK_URL.format(bitlink=short_url),
        headers={'Authorization': token}
    )
    response.raise_for_status()
    return response.json()['total_clicks']


def is_bitlink(url, token):
    parsed_url = urlparse(url)
    url = '{netloc}{path}'.format(
        netloc=parsed_url.netloc,
        path=parsed_url.path
    )
    response = requests.get(
        RETRIEVE_URL.format(bitlink=url),
        headers={'Authorization': token}
    )
    response.raise_for_status()
    return response.ok


def create_parser():
    parser = argparse.ArgumentParser(description='Bitly URL shortener')
    parser.add_argument('url', help='your URL')
    return parser


if __name__ == "__main__":
    parser = create_parser()
    args = parser.parse_args()
    url = args.url
    load_dotenv()
    token = environ['TOKEN_BITLY']
    if is_bitlink(url, token):
        print(count_clicks(url, token))
    else:
        print('Битлинк: ', shorten_url(url, token))
