echo "# Nepali Calendar Conversion Project

This repository provides functionality for converting dates between the Nepali Calendar (Bikram Sambat, BS) and the Gregorian Calendar (Anno Domini, AD). Additionally, the project includes features for calculating Tithi (lunar phases) and related Nepali date systems.

## Features

- Convert Gregorian Calendar dates (AD) to Nepali Calendar dates (BS)
- Convert Nepali Calendar dates (BS) to Gregorian Calendar dates (AD)
- Determine the Tithi (lunar phase) for a given Nepali date
- Data-based approach using \`calendar_bs.csv\` to manage date conversion

## Project Structure

\`\`\`bash
|-- NepaliCalendar.py  # Main logic for date conversion between AD and BS
|-- info.py            # Handles loading the CSV data and providing necessary information
|-- test.py            # Contains unit tests to verify the correctness of date conversions
|-- calendar_bs.csv    # CSV file with data to handle conversion between AD and BS
\`\`\`

## Usage

1. **Convert AD to BS:**
    You can convert a date in the Gregorian calendar to its equivalent in the Nepali calendar (BS) using the \`AD_to_BS()\` function.

    \`\`\`python
    from NepaliCalendar import AD_to_BS
    bs_date = AD_to_BS(2024, 10, 21)  # Example: Convert October 21, 2024
    print(bs_date)  # Outputs corresponding BS date
    \`\`\`

2. **Convert BS to AD:**
    Similarly, the \`BS_to_AD()\` function converts a date from the Nepali calendar to the Gregorian calendar (AD).

    \`\`\`python
    from NepaliCalendar import BS_to_AD
    ad_date = BS_to_AD(2081, 7, 4)  # Example: Convert 4th Kartik 2081 BS
    print(ad_date)  # Outputs corresponding AD date
    \`\`\`

3. **Calculate Tithi:**
    To find the Tithi (lunar phase) for a particular Nepali date:

    \`\`\`python
    from NepaliCalendar import calculate_tithi
    tithi = calculate_tithi(2081, 7, 4)  # Tithi for 4th Kartik 2081 BS
    print(tithi)
    \`\`\`

## Data File

The \`calendar_bs.csv\` file contains the necessary data for converting dates between the two calendars. This file is structured in a way that supports lookups and calculations within the conversion logic.

## Testing

Unit tests are provided in the \`test.py\` file. You can run these tests to ensure that all functionalities work as expected.

\`\`\`bash
python test.py
\`\`\`

## Requirements

- Python 3.x
- Pandas (for reading CSV data)

Install the required packages using:

\`\`\`bash
pip install pandas
\`\`\`

## Contributing

Feel free to fork this repository and make contributions. Any additions to functionality or bug fixes are welcome!

## License

This project is licensed under the MIT License.
" > README.md
