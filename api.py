import click
import requests

@click.command()
def cli():
    source_request = requests.get("https://newsapi.org/v2/sources?apiKey=a117f0a67f6146999368f24be6ab37f3")
    source_request_dict = source_request.json()
    sources = source_request_dict['sources']
    source_names = [source['name'] for source in sources]
    top_four_sources = source_names[:4]
    click.echo(top_four_sources)

    source = input("Enter source: ")
    get_news_source(top_four_sources, source)
    

def get_news_source(top_four_sources, source):
    if source not in top_four_sources:
        print("Chosen source not in list provided")
    if source == 'ABC News':
        headlines_request = requests.get("https://newsapi.org/v2/top-headlines?sources=abc-news&apiKey=a117f0a67f6146999368f24be6ab37f3")
        headlines_dict = headlines_request.json()
        articles = headlines_dict['articles']
        for article in articles:
            click.echo(click.style('TITLE: ' + article['title']))
            click.echo(click.wrap_text(article['description'],100))
            click.echo(click.style('URL: ' + article['url']))
            click.echo('\n')
            click.echo('*' * 100)

    if source == 'ABC News (AU)':
        headlines_request = requests.get("https://newsapi.org/v2/top-headlines?sources=abc-news-au&apiKey=a117f0a67f6146999368f24be6ab37f3")
        headlines_dict = headlines_request.json()
        articles = headlines_dict['articles']
        for article in articles:
            click.echo(click.style('TITLE: ' + article['title']))
            click.echo(click.wrap_text(article['description'],100))
            click.echo(click.style('URL: ' + article['url']))
            click.echo('\n')
            click.echo('*' * 100)

    if source == 'Aftenposten':
        headlines_request = requests.get("https://newsapi.org/v2/top-headlines?sources=aftenposten&apiKey=a117f0a67f6146999368f24be6ab37f3")
        headlines_dict = headlines_request.json()
        articles = headlines_dict['articles']
        for article in articles:
            click.echo(click.style('TITLE: ' + article['title']))
            click.echo(click.wrap_text(article['description'],100))
            click.echo(click.style('URL: ' + article['url']))
            click.echo('\n')
            click.echo('*' * 100)

    if source == 'Al Jazeera English':
        headlines_request = requests.get("https://newsapi.org/v2/top-headlines?sources=al-jazeera-english&apiKey=a117f0a67f6146999368f24be6ab37f3")
        headlines_dict = headlines_request.json()
        articles = headlines_dict['articles']
        for article in articles:
            click.echo(click.style('TITLE: ' + article['title']))
            click.echo(click.wrap_text(article['description'],100))
            click.echo(click.style('URL: ' + article['url']))
            click.echo('\n')
            click.echo('*' * 100)
