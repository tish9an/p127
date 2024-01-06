import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
# Initialize the webdriver
driver = webdriver.Chrome()  # You need to have Chrome WebDriver installed

# Open the URL in the web browser
url = "https://en.wikipedia.org/wiki/List_of_nearest_bright_stars"
driver.get(url)
# Get the page source and create a BeautifulSoup object
page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html.parser')

# Find the table with class 'wikitable'
table = soup.find('table', {'class': 'wikitable'})
# Initialize an empty list to store the scraped data
scraped_data = []

# Define a function to scrape the data
def scrape():
    # Find all rows in the table
    table_rows = table.find_all('tr')
    
    for row in table_rows[1:]:  # Skip the header row
        table_cols = row.find_all('td')
        temp_list = []
        print(table_cols)
        
        for col_data in table_cols:
            data = col_data.text.strip()
            temp_list.append(data)
            print(data)
        
        scraped_data.append(temp_list)

# Call the scrape function to get the data
scrape()
# Close the webdriver
driver.quit()

# Create a DataFrame with the scraped data
columns = ['Star_names', 'class', 'Magnitude_Appa
print("Data scraped and saved to star_data.csv")
rent','Magnitude_Absolute','Ascension','Not_sure','Declination','Distance']
df = pd.DataFrame(scraped_data, columns=columns)

# Save the DataFrame to a CSV file
df.to_csv('/star_data.csv', index=False)
