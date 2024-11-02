import requests
from bs4 import BeautifulSoup
import time
import random

def scrape_amazon_products(url):
    products = []
    headers = {
        'User -Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    for page in range(1, 6):  # Adjust for the number of pages
        print(f"Scraping page {page}...")
        page_url = f"{url}&page={page}"
        response = requests.get(page_url, headers=headers)

        # Print the response text to inspect the HTML
        print(response.text)  # Check if the HTML is valid

        # Sleep to avoid getting blocked
        time.sleep(random.uniform(2, 5))  # Random sleep between 2 to 5 seconds

        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract product data (modify selectors based on actual HTML structure)
        for item in soup.select('.s-main-slot .s-result-item'):
            name = item.h2.text if item.h2 else 'N/A'
            price = item.find('span', class_='a-price-whole').text if item.find('span', class_='a-price-whole') else 'N/A'
            description = item.find('span', class_='a-size-base-plus').text if item.find('span', class_='a-size-base-plus') else 'N/A'

            product = {
                'Name': name,
                'Price': price,
                'Description': description
            }
            products.append(product)

    return products

if __name__ == "__main__":
    amazon_url = 'https://www.amazon.com/s?k=laptop'  # Example search URL
    product_data = scrape_amazon_products(amazon_url)
    
    # Save product data to CSV or display
    print(product_data)