import requests
from bs4 import BeautifulSoup

url = "https://owasp.org/www-project-top-ten/"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    # Adjust the selector based on the actual HTML structure of the page
    owasp_items = soup.select('a[href*="www-project-top-ten/"]')

    with open('owasp_top_ten.txt', 'w') as f:
        for item in owasp_items:
            title = item.text.strip()
            f.write(f"{title}\n")
else:
    print("Failed to retrieve OWASP Top 10 data")

