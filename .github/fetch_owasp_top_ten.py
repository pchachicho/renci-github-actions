import requests
import re

# URL of the raw Markdown file
url = "https://raw.githubusercontent.com/OWASP/www-project-api-security/master/index.md"

response = requests.get(url)

if response.status_code == 200:
    # Fetch the Markdown content
    owasp_data = response.text
    
    # Process the data to extract the relevant section (optional)
    # Here you could use BeautifulSoup or regex to extract the Top Ten list if needed.
    
    # Read the PR template
    with open('.github/pull_request_template.md', 'r') as file:
        pr_template = file.read()
    
    # Replace the placeholder with the fetched OWASP data
    updated_template = re.sub(
        r'\[The OWASP Top Ten list will be fetched and updated by a GitHub Action\.\]',
        owasp_data,
        pr_template
    )
    
    # Write the updated PR template
    with open('.github/pull_request_template.md', 'w') as file:
        file.write(updated_template)
    
    print("Updated PR template successfully.")
else:
    print(f"Failed to retrieve OWASP Top Ten data. Status code: {response.status_code}")
    exit(1)
