from database.app import app
from parsers.provider import parse_provider_links
from parsers.purchase_plan import plan
from parsers.purchases import parse_purchase_links, parse_purchase_long
from parsers.order import parse_provider_links
urlS = []
urlL = []


parse_provider_links()
plan()
parse_purchase_links()
parse_purchase_long(urlL)
parse_provider_links()

app.run()
