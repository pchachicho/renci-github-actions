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


      # - name: Update PR template
    #   run: |
    #     owasp_top_ten=$(cat owasp_top_ten.txt | awk '{print "- " $0}' | paste -sd '\n' -)
    #     echo "OWASP Top Ten:"
    #     echo "$owasp_top_ten"
    #     echo "Debug: escaping special characters"
    #     printf '%s' "$owasp_top_ten" | sed 's/[&/\]/\\&/g'  
    #     sed -i "s|\[The OWASP Top Ten list will be fetched and updated by a GitHub Action.\]|$owasp_top_ten|" .github/pull_request_template.md
    #     echo "Updated PR Template:"