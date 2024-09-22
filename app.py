import streamlit as st
import requests
from bs4 import BeautifulSoup

def scrape_doctors(city, specialization):
    # Construct the URL based on inputs
    url = f"https://www.practo.com/search/doctors?results_type=doctor&q=%5B%7B%22word%22%3A%22{specialization}%22%2C%22autocompleted%22%3Atrue%2C%22category%22%3A%22subspeciality%22%7D%2C%7B%22word%22%3A%22{city}%22%2C%22autocompleted%22%3Atrue%2C%22category%22%3A%22locality%22%7D%5D&city={city.replace(' ', '%20')}"
    
    # Send a request to the URL
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
    except requests.RequestException as e:
        st.error(f"Error fetching the webpage for city {city}: {e}")
        return None

    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract doctor details
    doctors = []
    
    for card in soup.find_all('div', class_='listing-doctor-card'):
        try:
            name = card.find('h2', class_='doctor-name').text.strip()
            spec = card.find('span').text.strip()
            experience_div = card.find('div', string=lambda text: text and 'years experience overall' in text)
            experience = experience_div.text.strip() if experience_div else "N/A"
            locality = card.find('span', {'data-qa-id': 'practice_locality'}).text.strip() if card.find('span', {'data-qa-id': 'practice_locality'}) else "N/A"
            city = card.find('span', {'data-qa-id': 'practice_city'}).text.strip() if card.find('span', {'data-qa-id': 'practice_city'}) else "N/A"
            
            doctors.append({
                'Name': name,
                'Specialization': spec,
                'Experience': experience,
                'Locality': locality,
                'City': city
            })
        except AttributeError as e:
            st.warning(f"Error extracting data from card: {e}")
            continue

    return doctors

# Streamlit app
def main():
    st.title("Doctor Details Scraper")

    # User inputs
    city = st.text_input("Enter the city:")
    specialization = st.text_input("Enter the specialization:")
    
    if st.button("Scrape"):
        if city and specialization:
            with st.spinner('Fetching data...'):
                doctor_details = scrape_doctors(city, specialization)
                if doctor_details:
                    st.write(f"Total number of doctors found in {city}: {len(doctor_details)}")
                    for doctor in doctor_details:
                        st.write(f"**Name:** {doctor['Name']}")
                        st.write(f"**Specialization:** {doctor['Specialization']}")
                        st.write(f"**Experience:** {doctor['Experience']}")
                        st.write(f"**Locality:** {doctor['Locality']}")
                        st.write(f"**City:** {doctor['City']}")
                        st.write("---")
                else:
                    st.error(f"Could not retrieve doctor details for city {city}.")
        else:
            st.warning("Please enter both city and specialization.")

if __name__ == "__main__":
    main()
