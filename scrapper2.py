import requests
from bs4 import BeautifulSoup
import json

def scrape_sort_code_data(url):
    """
    Scrapes sort code data from the given URL and saves it into a JSON file.

    Args:
    url (str): The URL of the website to scrape.

    Returns:
    None
    """
    # Send a GET request to the URL
    response = requests.get(url)

    # Parse the HTML content
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the section with the title "10. Sort Code Samples"
    section_title = soup.find("h4", string="10. Sort Code Samples")

    if section_title:
        # Find the table containing the sort code data
        table = section_title.find_next("table")

        # Initialize a list to store sort code data
        sort_code_data = []

        if table:
            # Iterate over each row in the table skipping the header row
            for row in table.find_all("tr")[1:]:
                # Extract data from each column in the row
                columns = row.find_all("td")
                sort_code = columns[0].text.strip()
                bank = columns[1].text.strip()
                city = columns[2].text.strip()
                zip_code = columns[3].text.strip()
                phone = columns[4].text.strip()

                # Create a dictionary for the sort code data
                sort_code_info = {
                    "sortCode": sort_code,
                    "bank": bank,
                    "city": city,
                    "zip": zip_code,
                    "phone": phone
                }

                # Append the sort code info to the list
                sort_code_data.append(sort_code_info)

            # Save the sort code data to a JSON file
            with open("sort_code_data.json", "w") as json_file:
                json.dump(sort_code_data, json_file, indent=4)

            print("Sort code data scraped and saved to sort_code_data.json.")
        else:
            print("No sort code table found in the section.")
    else:
        print("Section '10. Sort Code Samples' not found on the page.")

if __name__ == "__main__":
    url = "https://www.iban.com/country/united-kingdom"
    scrape_sort_code_data(url)
