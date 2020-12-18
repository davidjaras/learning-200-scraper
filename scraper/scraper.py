'''
Scraper Main File

Return the courses completed by the student based on their username.
'''

# python imports
import sys

# scraper imports
from functions import get_student_courses
from config import ok_response

response = {
    'message': '',
    'courses': []
}


# Main
if __name__ == "__main__":
    try:
        platzi_username = sys.argv[1].lower()
    except IndexError as e:
        response['message'] = 'Error starting scraping. Username is required'
    
    search_result = get_student_courses(platzi_username, response)

    if not search_result['courses'] and search_result['message'] == ok_response:
        response['message'] = 'Profile is private or has not approved courses'
    
    print(response)
    
