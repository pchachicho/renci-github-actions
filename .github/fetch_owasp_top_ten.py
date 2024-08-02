import requests

# URL of the raw Markdown file
url = "https://raw.githubusercontent.com/OWASP/www-project-api-security/master/index.md"

response = requests.get(url)

if response.status_code == 200:
    # Write the raw Markdown content to a file
    with open('owasp_top_ten.txt', 'w') as f:
        f.write(response.text)

    # Read the current PR template
    with open('.github/pull_request_template.md', 'r') as file:
        pr_template = file.read()
    
    # Read the new content from owasp_top_ten.txt
    with open('owasp_top_ten.txt', 'r') as file:
        new_content = file.read()
    
    # Update the PR template with the new content
    updated_template = pr_template.replace("[The OWASP Top Ten list will be fetched and updated by a GitHub Action.]", new_content)
    
    # Write the updated PR template back to the file
    with open('.github/pull_request_template.md', 'w') as file:
        file.write(updated_template)

    # Verify that the file has been updated
    file_path = '.github/pull_request_template.md'

    # Open the file in read mode
    with open(file_path, 'r') as file:
        # Read the file contents
        file_contents = file.read()

    # Print the file contents
    print(file_contents)

else:
    print(f"Failed to retrieve OWASP Top Ten data. Status code: {response.status_code}")
    exit(1)
