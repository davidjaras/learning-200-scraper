'''
Scraper Main File

Return the courses completed by the student based on their username.
'''

# python imports
import sys

# scraper imports
from functions import get_student_courses

response = {
    'message': '',
    'courses': []
}

# Main
if __name__ == "__main__":
    try:
        platzi_username = sys.argv[1].lower()
        print(f'Starting scraping for: {platzi_username}')
        search_result = get_student_courses(platzi_username, response)
        print(search_result)

    except IndexError as e:
        print(f'Error starting scraping process. Username is required')
    
