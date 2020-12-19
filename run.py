from database.app import app
from parsers.provider import parse_provider_links

parse_provider_links()

app.run()
