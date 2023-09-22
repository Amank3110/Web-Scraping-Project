# Job Portal Scraper

## Overview

This project is a web scraper built in Python to collect job postings from the Cermati job portal. The scraper dynamically explores different departments, extracts job details, and stores the data in a structured JSON format.

## Features

- **Dynamic Exploration:** The scraper dynamically explores multiple departments on Cermati.com to collect job postings.

- **Parallelized Scraping:** To improve speed, the scraper is designed to parallelize the scraping process.

- **Flexible and Adaptable:** The code is built to adapt to changes in the number of departments, jobs, or job types on the website.

- **Data Structuring:** Job details are structured in a JSON file by department, making it easy to analyze and use the data.

## Requirements

- Python 3.x
- Required Python modules (install using `python -m pip install requests bs4`)

## Usage

1. Clone this repository to your local machine:


2. Navigate to the project directory:


3. Run the scraper script `solution.py`


The script will start scraping job postings and store the data in a JSON file named `solution.json`.

## JSON Data Format

The data collected by the scraper is structured as follows:

```json
{
"<Department Name>": [
 {
   "title": "<Job Title>",
   "location": "<Job Location>",
   "description": ["<Job Description>", "<Job Description>", ...],
   "qualification": ["<Qualification>", "<Qualification>", ...],
   "job_type": "<Job Type>",
   "postedBy": "<Posted By>"
 },
 // More job entries...
],
// More departments...
}
```

## Note
The code is designed to handle potential changes in the structure of the website. However, manual adjustments may be required if there are significant changes.


## Contact

For any inquiries or collaborations, feel free to reach out to me at amankumar80451@gmail.com or connect with me on LinkedIn at [LinkedIn Profile](https://www.linkedin.com/in/aman-kumar-3bab59201/).
