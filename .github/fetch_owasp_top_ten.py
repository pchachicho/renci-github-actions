import requests

# URL of the raw Markdown file
url = "https://raw.githubusercontent.com/OWASP/www-project-api-security/master/index.md"

response = requests.get(url)

if response.status_code == 200:
    # Write the raw Markdown content to a file
    with open('owasp_top_ten.txt', 'w') as f:
        f.write(response.text)

    with open('.github/pull_request_template.md', 'r') as file:
        pr_template = file.read()
        updated_template = pr_template
     # Write the updated PR template
    with open('.github/pull_request_template.md', 'w') as file:
        file.write(updated_template)

    # Optional: Print the first few lines of the Markdown file to verify
    print("Fetched OWASP Top Ten data:")
    print("\n".join(response.text.splitlines()[:10]))  # Print first 10 lines for review

else:
    print(f"Failed to retrieve OWASP Top Ten data. Status code: {response.status_code}")
    exit(1)
