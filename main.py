import requests
from bs4 import BeautifulSoup
import json

def scrape_banks_data(url):
    """
    Scrapes bank data from the given URL and saves it into a JSON file.

    Args:
    url (str): The URL of the website to scrape.

    Returns:
    None
    """
    # Send a GET request to the URL
    response = requests.get(url)

    # Parse the HTML content
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the parent div containing all tables
    parent_div = soup.find("div", class_="scroll--invite--class")

    # Find all tables within the parent div
    tables = parent_div.find_all("table")

    # Initialize a list to store bank data
    bank_data = []

    # Iterate over each table
    for table in tables:
        # Iterate over each row in the table skipping the header row
        for row in table.find_all("tr")[1:]:
            # Extract data from each column in the row
            columns = row.find_all("td")
            sort_code = columns[0].text.strip()
            bank_name = columns[1].text.strip()
            branch = columns[2].text.strip()

            # Create a dictionary for the bank data
            bank_info = {
                "sortCode": sort_code,
                "bankName": bank_name,
                "branch": branch
            }

            # Append the bank info to the list
            bank_data.append(bank_info)

    # Save the bank data to a JSON file
    with open("bank_data.json", "w") as json_file:
        json.dump(bank_data, json_file, indent=4)

    print("Bank data scraped and saved to bank_data.json.")

if __name__ == "__main__":
    url = "https://cybercrew.uk/blog/uk-banks-routing-numbers/"
    scrape_banks_data(url)
