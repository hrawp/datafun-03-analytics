""" This project 3 demonstates my ability to fench, parse and write differnt file types with python.
I plan to use some market files for my sample codes to process.
I will process .txt, .csv, .xlsx, and .json files"""

# Standard library imports

import csv
import io
from pathlib import Path
import pathlib 
import json
import re
from collections import Counter


# External library imports (requires virtual environment)
import requests 
from bs4 import BeautifulSoup

text_url="https://github.com/denisecase/datafun-03-spec/blob/main/data.txt"
json_url="https://github.com/CharanSuvarna/stocks/blob/main/stocks.json"
csv_url="https://github.com/denisecase/datafun-03-spec/blob/main/data.csv"
excel_url="https://github.com/denisecase/datafun-03-spec/blob/main/data.xls"
# Create a project path object
project_path = pathlib.Path.cwd()

# Create a project data path object
#data_path = project_path.joinpath('data')

# Create the data path if it doesn't exist, otherwise do nothing
#data_path.mkdir(exist_ok=True)

folder_name = f"{project_path}"
filenametxt = "data.txt"
filenamejson = "data.json"
filenamecsv = "data.csv"
filenameexcel = "data.xls"
filenamefinaltxt = "data2.txt"
filenamefinaljson = "data2.json"
filenamefianlcsv = "data2.csv"
filenamefinalexcel = "data2.xls"

def fetch_and_write_txt_data(folder_name, filenametxt, text_url):
    response = requests.get(text_url)
    if response.status_code == 200:
        file_path = pathlib.Path(folder_name).joinpath(filenametxt) # use pathlib to join paths
        with file_path.open('w') as file:
            file.write(response.text)
        print(f"Text data saved to {file_path}")
    else:
        print(f"Failed to fetch data: {response.status_code}")

def parse_text_data(folder_name, filenametxt, filenamefinaltxt):
    file_pathtxt = pathlib.Path(folder_name).joinpath(filenametxt)
    with file_pathtxt.open('r') as file:
        content = file.read()
    soup = BeautifulSoup(content, 'html.parser')
    text = soup.get_text()
    # Remove HTML tags using regex
    # text = re.sub(r'<[^>]+>', '', content)
    # Tokenize the text into words
    words = re.findall(r'\b\w+\b', text.lower())
    # Count the frequency of each word
    word_count = Counter(words)

    file_path = pathlib.Path(folder_name).joinpath(filenamefinaltxt) # use pathlib to join paths
    with file_path.open('w') as file:
        # Write the total word count
        file.write(f"The total word count is: {len(words)}\n")       
        # Write the frequency of each word
        for word, count in word_count.items():
            file.write(f"{word} - occurs {count} times.\n")     

  
        
def fetch_and_write_excel_data(folder_name, filenameexcel, excel_url):
    response = requests.get(excel_url)
    if response.status_code == 200:
        file_path = pathlib.Path(folder_name).joinpath(filenameexcel) # use pathlib to join paths
        with file_path.open('wb') as file:
            file.write(response.content)
        print(f"Excel data saved to {file_path}")
    else:
        print(f"Failed to fetch data: {response.status_code}")

def fetch_and_write_csv_data(folder_name, filenamecsv, csv_url):
    response = requests.get(csv_url)
    if response.status_code == 200:
        file_path = pathlib.Path(folder_name).joinpath(filenamecsv) # use pathlib to join paths
        with file_path.open('w') as file:
            file.write(response.text)
        print(f"csv data saved to {file_path}")
    else:
        print(f"Failed to fetch data: {response.status_code}")

def fetch_and_write_json_data(folder_name, filenamejson, json_url):
    response = requests.get(json_url)
    if response.status_code == 200:
        file_path = pathlib.Path(folder_name).joinpath(filenamejson) # use pathlib to join paths
        with file_path.open('w') as file:
            file.write(response.text)
        print(f"Json data saved to {file_path}")
    else:
        print(f"Failed to fetch data: {response.status_code}")

#####################################
# Define a main() function for this module.
#####################################

def main() -> None:
    ''' Main function to demonstrate module capabilities. '''
    
#file_pathcsv = pathlib.Path(folder_name).joinpath(filenamecsv)
#with open(file_pathcsv, mode='r', newline='') as file: 
  #  csv_data = file.read()
# Use io.StringIO to convert the string data into a file-like object
  #  csv_file = io.StringIO(csv_data)

# Create a CSV reader object
  #  csv_reader = csv.reader(csv_file)

# Read and print each row
#    for row in csv_reader:
 #       print(row)


#fetch_and_write_txt_data(folder_name,filenametxt,text_url)
#fetch_and_write_json_data(folder_name, filenamejson, json_url)
#fetch_and_write_excel_data(folder_name, filenameexcel, excel_url)
#fetch_and_write_csv_data(folder_name, filenamecsv, csv_url)
parse_text_data(folder_name, filenametxt, filenamefinaltxt)

# write_txt_file(folder_name, filename, data)
#####################################
# Conditional Execution
#####################################

if __name__ == '__main__':
    main()