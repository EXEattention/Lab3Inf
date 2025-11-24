 # Author = Kiyashko Alexander Maksimovich
 # Group = P3118
 # Date = 10.11.2025
import re
import requests
def idsearch():
    arr = []
    url = 'https://isu.itmo.ru'
    response = requests.get(url)
    html = response.text

    pattern = r'\bid\s*=\s*["\']?([^"\'\s>]+)["\']?'

    ids = re.findall(pattern, html, re.IGNORECASE)

    for id_value in set(ids): 
        print(id_value)
        arr.append(id_value)
    return arr
idsearch()