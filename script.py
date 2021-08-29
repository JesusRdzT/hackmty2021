from googlesearch import search

query="Matemáticas"

for i in search (query, tld='com', lang='en', tbs='0', safe='off', num=2, start=0, stop=2, domains=None, pause=2.0, tpe='', country='', extra_params=None, user_agent=None):
    print(i)