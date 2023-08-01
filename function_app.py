import json
import logging
import requests
import azure.functions as func
from functions import BASE_URL, get_error_text, get_authors_by_query, get_quotes_by_authors

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)


@app.route(route="quotes/random")
def get_random_quote(req: func.HttpRequest) -> func.HttpResponse:
    response = requests.get(f'{BASE_URL}/random')
    
    if response.ok:
        quote = response.json()['content']
        return func.HttpResponse(quote, status_code=200)

    logging.error(response.text)
    return func.HttpResponse(
        json.dumps(get_error_text(response)), status_code=response.status_code,mimetype='application/json')
    

@app.route(route="quotes/author")
def get_quote_by_artist(req: func.HttpRequest) -> func.HttpResponse:
    query = req.params.get('q','les')
    authors  = get_authors_by_query(query)

    if isinstance(authors, dict):
        return func.HttpResponse(json.dumps(authors),mimetype='application/json')

    response = get_quotes_by_authors(authors)
    return func.HttpResponse(json.dumps(response), status_code=200, mimetype='application/json')
    