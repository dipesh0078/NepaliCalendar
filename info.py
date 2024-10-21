import csv
# Function to load CSV into a dictionary like the one requested
def load_bs_years_data(file_path):
    bs_years_data = {}
    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip the header row
        for row in csv_reader:
            year = int(row[0])  # The first column is the year
            months_data = [int(x) for x in row[1:]]  # The rest are the months' data
            bs_years_data[year] = months_data
    return bs_years_data

# Path to the CSV file
file_path = "C:\\Users\\Legion\\Desktop\\Project\\calendar_bs.csv"

# Load the CSV data into the desired dictionary format
bs_years_data = load_bs_years_data(file_path)


tithi_names = {
    1: "Pratipada",
    2: "Dwitiya",
    3: "Tritiya",
    4: "Chaturthi",
    5: "Panchami",
    6: "Shashthi",
    7: "Saptami",
    8: "Ashtami",
    9: "Navami",
    10: "Dashami",
    11: "Ekadashi",
    12: "Dwadashi",
    13: "Trayodashi",
    14: "Chaturdashi",
    15: "Purnima",
    16: "Pratipada",   # Krishna Paksha
    17: "Dwitiya",     # Krishna Paksha
    18: "Tritiya",     # Krishna Paksha
    19: "Chaturthi",   # Krishna Paksha
    20: "Panchami",    # Krishna Paksha
    21: "Shashthi",    # Krishna Paksha
    22: "Saptami",     # Krishna Paksha
    23: "Ashtami",     # Krishna Paksha
    24: "Navami",      # Krishna Paksha
    25: "Dashami",     # Krishna Paksha
    26: "Ekadashi",    # Krishna Paksha
    27: "Dwadashi",    # Krishna Paksha
    28: "Trayodashi",   # Krishna Paksha
    29: "Chaturdashi",  # Krishna Paksha
    30: "Amavasya"     # Krishna Paksha
}

IMPORTANT_EVENTS = {
    (1, 1): "नयाँ वर्ष",  # Nepali New Year (BS)
    (1, 11): "लोकतन्त्र दिवस",  # Loktantra Diwas
    (1, 18): "विश्व मजदुर दिवस",  # International Labor Day
    (1, 30): "श्रीपञ्चमी",  # Shree Panchami
    (3, 8): "महिला दिवस",  # International Women's Day
    (5, 15): "कुशे औंशी",  # Kushe Aunshi
    (6, 3): "संबिधान दिवस",  # Constitution Day
    (6, 8): "विश्व वातावरण दिवस",  # World Environment Day
    (6, 11): "गणेश चतुर्थी",  # Ganesh Chaturthi
    (7, 1): "विश्व पर्यटन दिवस",  # World Tourism Day
    (9, 1): "विश्व पर्यटन दिवस",  # World Tourism Day
    (9, 7): "उधौली पर्व",  # Udhauli Parva
    (9, 12): "मोहनी नख",  # Mohani Nakha (Newa)
    (9, 15): "अन्नपूर्ण यात्रा",  # Annapurna Yatra
    (9, 23): "यमरी पुन्ही",  # Yomari Punhi
    (10, 1): "माघे संक्रान्ति",  # Maghe Sankranti
    (11, 7): "प्रजातन्त्र दिवस",  # Democracy Day

}