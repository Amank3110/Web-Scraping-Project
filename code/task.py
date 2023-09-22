"""
INSTALLED REQUIRED MODULES
-- python -m pip install requests
-- python -m pip install bs4
"""

import requests
import html
from bs4 import BeautifulSoup
import json

class Scraping:
    def __init__(self, url):
        self.url = url
        self.job_data = {}

    def FetchData(self):
        try:
            r = requests.get(self.url)
            return r.text
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to fetch data: {e}")

    def ParseData(self, data):
        '''Parse in HTML format and loads in Json'''
        try:
            soup = BeautifulSoup(data, 'html.parser')
            script_tag = soup.find('script', id='initials')
            json_data = json.loads(script_tag.string)
            return json_data
        except (json.JSONDecodeError, AttributeError) as e:
            raise Exception(f"Failed to parse data: {e}")

    def FormatLocation(self, job):
        ''' Format in "city, country '''
        country_label = job['customField'][2]['valueLabel']
        city = job['location']['city']
        return f"{city}, {country_label}"

    def FetchJobDetails(self, job_url):
        try:
            r = requests.get(job_url)
            return r.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to fetch job details: {e}")

    def scrape_jobs(self, json_data):
        '''Scrape and format the data into required format'''
        try:
            for country, jobs in json_data['smartRecruiterResult'].items():
                for job in jobs['content']:
                    dept_name = job['department']['label']
                    job_title = job['name']
                    job_location = self.FormatLocation(job)
                    job_description = []
                    job_qualifications = []

                    # Fetch description, Qualifications from the 'ref' URL
                    job_url = job['ref']
                    job_details = self.FetchJobDetails(job_url)

                    # Update job description and qualifications if available
                    if 'jobAd' in job_details:
                        job_ad = job_details['jobAd']
                        
                        # Extract text from HTML description
                        description_soup = BeautifulSoup(job_ad['sections']['jobDescription']['text'], 'html.parser')
                        job_description.append(description_soup.get_text())
                        
                        # Extract text from HTML qualifications
                        qualifications_soup = BeautifulSoup(job_ad['sections']['qualifications']['text'], 'html.parser')
                        job_qualifications.append(qualifications_soup.get_text())

                    job_type = job['typeOfEmployment']['label']
                    posted_by = job['company']['name']

                    job_info = {
                        'title': job_title,
                        'location': job_location,
                        'description': job_description,
                        'qualification': job_qualifications,
                        'job_type': job_type,
                        'postedBy': posted_by,
                    }

                    if dept_name not in self.job_data:
                        self.job_data[dept_name] = []
                    self.job_data[dept_name].append(job_info)
        except KeyError as e:
            raise Exception(f"Failed to extract job data: {e}")

    def SaveToJson(self, filename):
        '''write Json file'''
        try:
            with open(filename, 'w', encoding='utf-8') as json_file:
                json.dump(self.job_data, json_file, ensure_ascii=False, indent=4)
            print('Data saved in', filename)
        except IOError as e:
            raise Exception(f"Failed to save data: {e}")

    def ScrapAndSave(self, filename):
        data = self.FetchData()
        json_data = self.ParseData(data)
        self.scrape_jobs(json_data)
        self.SaveToJson(filename)

if __name__ == "__main__":
    # made scraper Object of Scraping class with target URL
    scraper = Scraping("https://www.cermati.com/karir")
    try:
        scraper.ScrapAndSave('solution.json')
    except Exception as e:
        print(f"An error occurred: {e}")