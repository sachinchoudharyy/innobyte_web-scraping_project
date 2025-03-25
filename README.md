# Doctor Details Scraper

A **Streamlit** web application that scrapes doctor details from **Practo** based on city and specialization inputs. The application fetches relevant information such as doctor names, specializations, experience, and locality details.

## Features
- User-friendly interface using **Streamlit**.
- Scrapes real-time doctor details directly from **Practo**.
- Displays essential information like:
  - **Doctor's Name**
  - **Specialization**
  - **Experience**
  - **Locality**
  - **City**
- Provides error handling for missing or incomplete data.

## Technologies Used
- **Python**
- **Streamlit**
- **Requests**
- **BeautifulSoup**

## Installation
1. **Clone the repository**
   ```bash
   git clone <repository_url>
   cd doctor-details-scraper
   ```

2. **Create a virtual environment** (optional but recommended)
   ```bash
   python -m venv env
   source env/bin/activate   # On Windows: .\env\Scripts\activate
   ```

3. **Install the required dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

## Usage
1. Enter the desired **City** and **Specialization** in the respective input fields.
2. Click the **Scrape** button.
3. The app will display the total number of doctors found and list their details.

## Example
- **City:** `Bangalore`
- **Specialization:** `Dermatologist`

**Output:**
```
Total number of doctors found in Bangalore: 15

Name: Dr. mohit
Specialization: Dermatologist
Experience: 10 years
Locality: Indiranagar
City: Bangalore

---
Name: Dr. V.C. Sharma
Specialization: Dermatologist
Experience: 5 years
Locality: Koramangala
City: Bangalore
```

## Error Handling
- If no doctors are found, the app notifies the user.
- Proper messages are displayed for connection errors or unexpected website changes.

## Future Enhancements
- Add filters for doctor ratings and fees.
- Implement pagination for improved data visualization.
- Enhance UI with better design elements.

## License
This project is licensed under the **MIT License**.

## Contributors
- SACHIN CHOUDHARY  - Developer

## Feedback
If you encounter any issues or have suggestions for improvements, feel free to raise an issue or submit a pull request.

