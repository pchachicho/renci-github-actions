import requests

# URL of the raw Markdown file
url = "https://raw.githubusercontent.com/OWASP/www-project-api-security/master/index.md"

response = requests.get(url)

if response.status_code == 200:
    # Get the raw Markdown content
    new_content = response.text

    # Optional: You might want to process new_content here if needed
    # For example, extracting only a specific part of the Markdown file

    # Update the PR template with the new content
    with open('.github/pull_request_template.md', 'w') as file:
        file.write(new_content)

    print("PR template updated successfully.")
else:
    print(f"Failed to fetch content. Status code: {response.status_code}")
