from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd 

import time 

# Set the path to your webdriver executable
webdriver_path = '/path/to/chromedriver'

options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
# options.add_argument('--headless')
# Start a new Chrome browser session
driver = webdriver.Chrome(options=options)

# Open the website
url = 'http://howstat.com'
driver.get(url)

try:
    # Find all elements with class 'ScorecardBox'
    scorecard_boxes = driver.find_elements(By.CLASS_NAME, 'ScorecardSeries')

    # Choose the index of the specific ScorecardBox you want to click (e.g., index 0 for the first one)
    index_to_click = 0

    # Click on the selected ScorecardBox
    scorecard_boxes[index_to_click].click()
    
     # Wait for the table to load
    table = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'TableLined'))
    )

    # Extract data from the table
    rows = table.find_elements(By.XPATH, "//tr[position() > 1]")  # Skip the header row

    # Lists to store data
    match_numbers = []
    match_dates = []
    countries_list = []
    grounds = []
    results = []

    for row in rows:
        columns = row.find_elements(By.TAG_NAME, 'td')

        # Check if there are at least 5 columns in the row
        if len(columns) >= 5:
            match_number = columns[0].text
            match_date = columns[1].text
            countries = columns[2].text
            ground = columns[3].text
            result = columns[4].text

            # Append data to lists
            match_numbers.append(match_number)
            match_dates.append(match_date)
            countries_list.append(countries)
            grounds.append(ground)
            results.append(result)

    # Create a DataFrame from the lists
    df = pd.DataFrame({
        'Match Number': match_numbers,
        'Match Date': match_dates,
        'Countries': countries_list,
        'Ground': grounds,
        'Result': results
    })

    # Display the DataFrame
    print(df)
except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser window
    driver.quit()
