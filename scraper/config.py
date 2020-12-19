'''
Config file that contains information about Platzi WebPage selectors
'''

ok_response = 'OK: 200'

site_config = {
    'name': 'Platzi',
    'domain': 'https://platzi.com',
    'url_search': 'https://platzi.com/@$username$',
    'queries': {
        'container_elements': 'script',
        'regex_filter': 'courses: \[.*\]',
        'regex_group': 0
    },
    'success_http_status_code': 200
}
