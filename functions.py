import requests

BASE_URL = 'https://api.quotable.io'


def get_error_text(response: requests.Response):
    error =  'Error happened on server'
    
    try:
        error = response.json()['statusMessage']
    except Exception:
        pass
        
    return {'status': 'error','detail': error}


def get_authors_by_query(query):
    index = 1
    total = 1
    authors = []
    author_string = ''
    
    while True:
        if index > total:
            break

        resp = requests.get(f'https://api.quotable.io/authors?page={index}&limit=150')
        if not resp.ok:
            return get_error_text(resp)
        
        results = resp.json()['results']
        authors.extend([item['name'] for item in results if query in item['name']])

        index  += 1
        total  = resp.json()['totalPages']

    for author in authors:
        author_string += f'|{author}'

    return author_string[1:]


def get_quotes_by_authors(author_string):
    index = 1
    total = 1
    quotes = []
    
    while True:
        if index > total:
            break

        resp = requests.get(f'https://api.quotable.io/quotes?author={author_string[1:]}&limit=100')
        if not resp.ok:
            return get_error_text(resp)
        
        results = resp.json()['results']
        quotes.extend([{'author':item['author'],'content':item['content']} for item in results])

        index  += 1
        total  = resp.json()['totalPages']

    return quotes