from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

# Function to scrape incident titles, descriptions, and timestamps
def scrape_incidents(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all incident titles, descriptions, and timestamps
        incident_titles = soup.find_all('a', class_='whitespace-pre-wrap actual-title with-ellipsis')
        incident_descriptions = soup.find_all('span', class_='whitespace-pre-wrap')
        incident_timestamps = soup.find_all('small')

        # Check if any of the lists are empty
        if not incident_titles or not incident_descriptions or not incident_timestamps:
            return [{
                "description": "Unavailable",
                "timestamp": "Unavailable",
                "title": "Unavailable"
            }]

        # Create a list to store incidents
        incidents = []

        # Iterate over the incidents and add them to the list
        for title, description, timestamp in zip(incident_titles, incident_descriptions, incident_timestamps):
            title_text = title.text.strip() if title else "Unavailable"
            description_text = description.text.strip() if description else "Unavailable"
            timestamp_text = timestamp.text.strip().replace('\n', '') if timestamp else "Unavailable"
            incidents.append({
                "description": description_text,
                "timestamp": timestamp_text,
                "title": title_text
            })

        return incidents
    else:
        return []


# Route to serve the incidents in JSON format
@app.route('/incidents', methods=['GET'])
def get_incidents():
    # URL of the page to scrape
    url = 'https://discordstatus.com/'
    
    # Scrape incidents
    incidents = scrape_incidents(url)
    
    # Return JSON response with the description, timestamp, and title fields
    return jsonify(incidents)


if __name__ == '__main__':
    app.run(debug=True)
