'''
Functions file that supports scraper.
'''

# python imports
import requests
import bs4

# scraper imports
from config import site_config


def get_student_courses(platzi_username, response):
    # setup params
    queries = site_config['queries']
    url = site_config['url_search'].replace('$username$', platzi_username)
    print(f'URL to scrape is: {url}')

    # request url
    try:
        response_link = requests.get(url)
        response['message'] = f'OK: {response_link.status_code}'
    except Exception as e:
        response['message'] = f'Error: {e}'
        return response
    
    if response_link.status_code != site_config['success_http_status_code']:
        response['message'] = f'Fail. Status code: {response_link.status_code}'

    return response
    
    
