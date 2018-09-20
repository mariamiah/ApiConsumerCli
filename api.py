import click
import requests

@click.command()
def cli():
    source_request = requests.get("https://newsapi.org/v2/sources?apiKey=a117f0a67f6146999368f24be6ab37f3")
    source_request_dict = source_request.json()
    sources = source_request_dict['sources']
    for source in sources:
        click.echo(source['name'])


