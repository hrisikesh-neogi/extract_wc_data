from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

class Scrape:
    def __init__(self):

        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--headless')
        # Start a new Chrome browser session
        self.driver = webdriver.Chrome(options=options)

    def scrape(self):
        try:
            # Open the website
            url = 'http://howstat.com'
            self.driver.get(url)
            # Find all elements with class 'ScorecardBox'
            scorecard_boxes = self.driver.find_elements(By.CLASS_NAME, 'ScorecardSeries')

            # Choose the index of the specific ScorecardBox you want to click (e.g., index 0 for the first one)
            index_to_click = 0

            # Click on the selected ScorecardBox
            scorecard_boxes[index_to_click].click()
            
            # Wait for the table to load
            table = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'TableLined'))
            )

            # Extract data from the table
            rows = table.find_elements(By.XPATH, "//tr[position() > 1]")  # Skip the header row

            # Lists to store data
            dates = []
            team_1 = []
            team_2 = []
            winners = []
            margins = []
            grounds = []

            for row in rows:
                columns = row.find_elements(By.TAG_NAME, 'td')

                # Check if there are at least 5 columns in the row
                if len(columns) >= 5:
                    date = columns[1].text
                    countries = columns[2].text.split(' v ')
                    team_1.append(countries[0])
                    team_2.append(countries[1])
                    winner_margin = columns[4].text.split(' won by ')
                    winner = winner_margin[0]
                    margin = winner_margin[1]
                    ground = columns[3].text

                    # Append data to lists
                    dates.append(date)
                    winners.append(winner)
                    margins.append(margin)
                    grounds.append(ground)

            # Create a DataFrame from the lists
            df = pd.DataFrame({
                'Date': dates,
                'Team_1': team_1,
                'Team_2': team_2,
                'Winner': winners,
                'Margin': margins,
                'Ground': grounds
            })
            return df
        
        except Exception as e:
            print(f"An error occurred: {e}")
        