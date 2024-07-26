import os
import requests
import pandas as pd
from bs4 import BeautifulSoup

# URL of the page to scrape
url = 'https://www.ecb.europa.eu/stats/policy_and_exchange_rates/key_ecb_interest_rates/html/index.en.html'

# CSV file path
csv_file_path = 'interest_rate_history.csv'

# Function to scrape data from the website
def scrape_data():
    response = requests.get(url)
    response.raise_for_status()  # Check if the request was successful
    soup = BeautifulSoup(response.content, 'lxml')
    table = soup.find('table')
    date_year = []
    date_day_month = []
    deposit_facility = []
    fixed_rate_tenders = []
    variable_rate_tenders = []
    marginal_lending_facility = []

    for row in table.find_all('tr')[1:]:  # Skip the header row
        cells = row.find_all('td')
        if len(cells) >= 6:  # Ensure the row has at least 6 columns
            date_year.append(cells[0].get_text(strip=True))
            date_day_month.append(cells[1].get_text(strip=True))
            deposit_facility.append(cells[2].get_text(strip=True))
            fixed_rate_tenders.append(cells[3].get_text(strip=True))
            variable_rate_tenders.append(cells[4].get_text(strip=True))
            marginal_lending_facility.append(cells[5].get_text(strip=True))
        else:
            print(f"Skipping row with {len(cells)} columns: {[cell.get_text(strip=True) for cell in cells]}")

    # Combine the extracted columns into rows
    rows = list(zip(date_year, date_day_month, deposit_facility, fixed_rate_tenders, variable_rate_tenders, marginal_lending_facility))
    # Create a DataFrame
    df = pd.DataFrame(rows, columns=['Date Year', 'Date Day Month', 'Deposit Facility', 'Fixed Rate Tenders', 'Variable Rate Tenders', 'Marginal Lending Facility'])
    return df

# Check if the CSV file exists
if os.path.exists(csv_file_path):
    # Read the existing data from the CSV file
    existing_df = pd.read_csv(csv_file_path)
    # Fill gaps in 'Date Year' column with the last next valid data
    existing_df['Date Year'] = existing_df['Date Year'].ffill()
    # Determine the latest date in the existing data
    latest_date = pd.to_datetime(existing_df['Date Year'], errors='coerce').max()
    print(f"Latest date in the existing data: {latest_date}")

    # Scrape the new data
    new_df = scrape_data()
    new_df['Date Year'] = pd.to_datetime(new_df['Date Year'], errors='coerce')

    # Filter the new data to get only the rows with dates later than the latest date in the existing data
    new_data = new_df[new_df['Date Year'] > latest_date]

    # Append the new data to the existing data
    updated_df = pd.concat([existing_df, new_data], ignore_index=True)

    print(f"Number of new rows added: {len(new_data)}")
else:
    # Scrape the data and use it as the initial DataFrame
    updated_df = scrape_data()

# Fill gaps in the updated DataFrame
updated_df['Date Year'] = updated_df['Date Year'].ffill()

# Save the updated DataFrame to the CSV file
updated_df.to_csv(csv_file_path, index=False)

print(f'Data has been saved to {csv_file_path}')
