'''
Scraper Main File

Return the courses completed by the student based on their username.
'''

# python imports
import sys

# scraper imports
from functions import get_student_courses
from config import ok_response


def scrape_student_profile(username):
    response = {
        'message': '',
        'courses': []
    }

    search_result = get_student_courses(username, response)

    if not search_result['courses'] and search_result['message'] == ok_response:
        response['message'] = 'Profile is private or has not approved courses'

    return(response)

   
