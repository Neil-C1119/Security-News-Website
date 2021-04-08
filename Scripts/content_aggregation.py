#Python content aggregation for website
import mysql.connector, requests
from bs4 import BeautifulSoup

Naked = 'https://nakedsecurity.sophos.com/'
Naked_page = requests.get(Naked)

SecWeek = 'https://www.securityweek.com/'
SecWeek_page = requests.get(SecWeek)

Dark = 'https://www.darkreading.com/'
Naked_page = requests.get(Dark)

THN = 'https://thehackernews.com/'
Naked_page = requests.get(THN)

Bleeping = 'https://www.bleepingcomputer.com/'
Naked_page = requests.get(Bleeping)

#
# mydb = mysql.connector.connect(
#     host=""
#     user=""
#     password=""
# )
