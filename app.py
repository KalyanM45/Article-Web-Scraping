import os
import requests
from bs4 import BeautifulSoup
from datetime import datetime


current_datetime = datetime.now() 

folder_name = current_datetime.strftime('%H_%M_%d_%m_%Y') # Format the current date and time for directory name

if not os.path.exists(folder_name):
    os.makedirs(folder_name, exist_ok=True) # Create a folder with the current date and time format

# Define the URL to fetch data
url = "https://content.guardianapis.com/technology/artificialintelligenceai?&api-key=01dd6b39-66d5-4ed8-8335-9dd17fe41a3f&type=article&page=1"

response=requests.get(url) # Fetch data from the URL

x=response.json() # Convert the response to JSON format

web_urls = [item['webUrl'] for item in x['response']['results']]

def save_content_to_file(url, folder, filename): # Function to save the content to a file
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
 
            with open(os.path.join(folder, filename), 'w', encoding='utf-8') as file:
                for header in soup.find_all(['h1']):
                    file.write("Tile: " + header.text + '\n'*5)
                for paragraph in soup.find_all('p'):
                    file.write(paragraph.text + '\n')
        else:
            print("Failed to retrieve the page:", url)
    except Exception as e:
        print("An error occurred:", e)
    

for index, url in enumerate(web_urls):
    filename = f'article_{index}.txt'  # Create a unique filename for each article
    save_content_to_file(url, folder_name, filename) # Save the content to a file