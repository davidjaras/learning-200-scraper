'''
Flask app.
Scraper API.
'''

# python imports
import flask

# scraper imports
from scraper import scrape_student_profile


app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/api/<username>', methods=['GET'])
def home(username):
    return scrape_student_profile(username)


app.run()
