import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import pandas as pd
# Define the base URL of the website
base_url = 'https://brainlox.com'

# List of section URLs
section_urls = [
    '/courses/category/technical',
    '/courses/category/academic',
    '/courses/category/language',
    '/courses/category/music',
    '/courses/category/lifestyle'
]

# Create empty lists to store course data
course_names = []
course_links = []
course_descriptions = []

def scrape_course_overview(url):
    # Send an HTTP GET request to the URL
    response = requests.get(url)
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find the elements containing course information
        course_elements = soup.find_all('div', class_='courses-overview')     

        # Iterate through the course elements and extract information
        for course in course_elements:        
          #Extract the course description
          course_description = course.find('p').text

          # Print the extracted information
            
          return(f'Course Description: {course_description}')
          
    else:
        return(f'Failed to fetch the webpage for {section_url}')

# Function to scrape course information
def scrape_course_info(section_url):
    url = urljoin(base_url, section_url)
    course_data_text=""
    # Send an HTTP GET request to the section URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract the section name from the URL
        section_name = section_url.split('/')[-1].capitalize()

        # Find the elements containing course information
        course_elements = soup.find_all('div', class_='courses-content')

        # Print the section name
        print(section_name)

        # Iterate through the course elements and extract information
        for course in course_elements:
            # Extract the course name
            course_name = course.find('h3').text

            # Extract the relative course link
            relative_course_link = course.find('a')['href']

            # Construct the complete course link
            complete_course_link = urljoin(base_url, relative_course_link)
            #for extracting content
            course_description = scrape_course_overview(complete_course_link)
            # Extract the course description
            #course_description = course.find('p').text
            course_data_text += f'Course Name: {course_name}\n'
            course_data_text += f'Course Link: {complete_course_link}\n'
            course_data_text += f'Course Description: {course_description}\n'
            course_data_text += '---\n'
            # Print the extracted information
            #course_names.append(course_name)
            #course_links.append(complete_course_link)
            #course_descriptions.append(course_description)
            #print(f'Course Name: {course_name}')
            #print(f'Course Link: {complete_course_link}')
            #print(f'Course Description: {course_description}')
            #print('---')
    else:
        print(f'Failed to fetch the webpage for {section_url}')

# Iterate through the section URLs and scrape course information
for section_url in section_urls:
    scrape_course_info(section_url)
# Create a DataFrame to store the data
#course_data = pd.DataFrame({
#    'Course Name': course_names,
#    'Course Link': course_links,
#    'Course Description': course_descriptions
#})
with open('course_data.txt', 'w', encoding='utf-8') as text_file:
    text_file.write(course_data_text)
# Export the DataFrame to an Excel file
#course_data.to_excel('course_data.xlsx', index=False)

