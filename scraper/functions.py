'''
Functions file that supports scraper.
'''

# python imports
import requests
import bs4
import re
import json

# scraper imports
from config import site_config


def get_student_courses(platzi_username, response):
    # setup params
    queries = site_config['queries']
    url = site_config['url_search'].replace('$username$', platzi_username)

    # request url
    try:
        response_link = requests.get(url)
        response['message'] = f'OK: {response_link.status_code}'
    except Exception as e:
        response['message'] = f'Error: {e}'
        return response

    if response_link.status_code != site_config['success_http_status_code']:
        response['message'] = f'Fail. Status code: {response_link.status_code}'

    ''' Get courses. '''
    soup = bs4.BeautifulSoup(response_link.text, 'html.parser')
    elements = soup.select(queries['container_elements'])

    # find html element with dourses data
    for element in elements:
        # use regex to get string with courses
        str_courses = re.search(queries['regex_filter'], str(element))
        if str_courses is not None:
            # string processing to return courses in json format
            courses = str_courses.group(queries['regex_group'])
            courses = courses.replace('courses: ', '')
            response['courses'] = json.loads(courses)

    return response
