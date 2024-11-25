import requests
from bs4 import BeautifulSoup
import validators

# Step 1: User Inputs URL and Parameters
def get_user_input():
    url = "https://www.facebook.com"
    if not validators.url(url):
        print("Invalid URL. Please try again.")
        return None
    return url

# Step 2: Validate URL
def validate_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("URL validated successfully!")
            return response
        else:
            print(f"Failed to access the URL. HTTP Status Code: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

# Step 3: Scrape Content
def scrape_content(response):
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract the title
    title = soup.title.string if soup.title else "No title found"
    
    # Extract the meta description
    description_tag = soup.find('meta', attrs={'name': 'description'})
    description = description_tag['content'] if description_tag else "No description found"
    
    print("Scraped Content:")
    print(f"Title: {title}")
    print(f"Description: {description}")

def main():
    url = get_user_input()
    if url:
        response = validate_url(url)
        if response:
            scrape_content(response)

if __name__ == "__main__":
    main()
