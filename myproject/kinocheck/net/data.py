import os
import time
import traceback

import flickrapi
from urllib.request import urlretrieve

import sys
from retry import retry


@retry()
def get_photos(url, filepath):
    urlretrieve(url, filepath)
    time.sleep(0.2)


if __name__ == '__main__':
    flickr_api_key = '55aa52b6e6975c41d742d48ec10b9629'
    secret_key = 'caa92ac82fdb81d2'

    flicker = flickrapi.FlickrAPI(flickr_api_key, secret_key, format='parsed-json')
    keywords = ["Poison mushrooms","Edible mushrooms"]
    for keyword in keywords:
        response = flicker.photos.search(
            text=keyword,
            per_page=1000,
            media='photos',
            sort='relevance',
            safe_search=1,
            extras='url_c,license'
        )
        photos = response['photos']
        if not os.path.exists('data/' + keyword):
            os.mkdir('data/' + keyword)
        for photo in photos['photo']:
            try:
                url = photo['url_c']
                filepath = 'data/' + keyword + '/' + photo['id'] + '.jpg'
                get_photos(url, filepath)
            except Exception as e:
                traceback.print_exc()
