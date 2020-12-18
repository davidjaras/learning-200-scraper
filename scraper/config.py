'''
Config file that contains information about Platzi WebPage selectors
'''


site_config = {
    'name': 'Platzi',
    'domain': 'https://platzi.com',
    'url_search': 'https://platzi.com/p/$username$',
    'queries': {
        'container_elements': 'script',
        'regex_filter': 'courses: \[.*\]',
        'regex_group': 0
    },
    'success_http_status_code': 200
}
