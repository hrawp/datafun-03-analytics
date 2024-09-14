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

# Data for project 3
text_url="https://github.com/denisecase/datafun-03-spec/blob/main/data.txt"
json_url="https://github.com/CharanSuvarna/stocks/blob/main/stocks.json"
csv_url="https://github.com/denisecase/datafun-03-spec/blob/main/data.csv"
excel_url="https://github.com/denisecase/datafun-03-spec/blob/main/data.xls"

# Create a project path object
project_path = pathlib.Path.cwd()
folder_name = f"{project_path}"

# File names for project 3
filenametxt = "datainital.txt"
filenamejson = "datainital.json"
filenamecsv = "datainitial.csv"
filenamexls = "datainitial.xls"
filenamefinaltxt = "datafinal.txt"
filenamefinaljson = "datafinal.json"
filenamefinalcsv = "datafinal.csv"
filenamefinalxls = "datafinal.xls"

# Write Text Data to the PC

def fetch_and_write_txt_data(folder_name, filenametxt, text_url):
    response = requests.get(text_url)
    if response.status_code == 200:
        file_path = pathlib.Path(folder_name).joinpath(filenametxt) # use pathlib to join paths
        with file_path.open('w') as file:
            file.write(response.text)
        print(f"Text data saved to {file_path}")
    else:
        print(f"Failed to fetch data: {response.status_code}")

# Parse Text Data and write to a new Text file

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
        print(f"Text data saved to {file_path}")
  
  # Write Excel Data to the PC
        
def fetch_and_write_excel_data(folder_name, filenamexls, excel_url):
    response = requests.get(excel_url)
    if response.status_code == 200:
        file_path = pathlib.Path(folder_name).joinpath(filenamexls) # use pathlib to join paths
        with file_path.open('wb') as file:
            file.write(response.content)
        print(f"Excel data saved to {file_path}")
    else:
        print(f"Failed to fetch data: {response.status_code}")

# Parse Excel Data and write to a new Excel file

def parse_excel_data(folder_name, filenamexls, filenamefinalxls):
    file_pathxls = pathlib.Path(folder_name).joinpath(filenamexls)
    with file_pathxls.open('r') as file:
        content = file.read()
    soup = BeautifulSoup(content, 'html.parser')
    text = soup.get_text()
    # Remove HTML tags using regex
    # text = re.sub(r'<[^>]+>', '', content)
    # Tokenize the text into words
    words = re.findall(r'\b\w+\b', text.lower())
    # Count the frequency of each word
    word_count = Counter(words)

    file_path = pathlib.Path(folder_name).joinpath(filenamefinalxls) # use pathlib to join paths
    with file_path.open('w') as file:
        # Write the total word count
        file.write(f"The total word count is: {len(words)}\n")       
        # Write the frequency of each word
        for word, count in word_count.items():
           file.write(f"{word} - occurs {count} times.\n")  
        print(f"Excel data saved to {file_path}")

# Write .csv Data to the PC

def fetch_and_write_csv_data(folder_name, filenamecsv, csv_url):
    response = requests.get(csv_url)
    if response.status_code == 200:
        file_path = pathlib.Path(folder_name).joinpath(filenamecsv) # use pathlib to join paths
        with file_path.open('w', newline='', encoding='utf-8')as file:
            file.write(response.text)
        print(f"csv data saved to {file_path}")
    else:
        print(f"Failed to fetch data: {response.status_code}")

# Parse J.csv Data and write to a new csv file

def parse_csv_data(folder_name, filenamecsv, filenamefinalcsv):
    file_pathcsv = pathlib.Path(folder_name).joinpath(filenamecsv)
    with file_pathcsv.open('r') as file:
        content = file.read()
    soup = BeautifulSoup(content, 'html.parser')
    text = soup.get_text()
    # Remove HTML tags using regex
    # text = re.sub(r'<[^>]+>', '', content)
    # Tokenize the text into words
    words = re.findall(r'\b\w+\b', text.lower())
    # Count the frequency of each word
    word_count = Counter(words)

    file_path = pathlib.Path(folder_name).joinpath(filenamefinalcsv) # use pathlib to join paths
    with file_path.open('w') as file:
        # Write the total word count
        file.write(f"The total word count is: {len(words)}\n")       
        # Write the frequency of each word
        for word, count in word_count.items():
           file.write(f"{word} - occurs {count} times.\n")      
        print(f"csv data saved to {file_path}")


# Write JSON Data to the PC

def fetch_and_write_json_data(folder_name, filenamejson, json_url):
    response = requests.get(json_url)
    if response.status_code == 200:
        file_path = pathlib.Path(folder_name).joinpath(filenamejson) # use pathlib to join paths
        with file_path.open('w') as file:
            file.write(response.text)
        print(f"Json data saved to {file_path}")
    else:
        print(f"Failed to fetch data: {response.status_code}")

# Parse JSON Data and write to a new JSON file

def parse_json_data(folder_name, filenamejson, filenamefinaljson):
    file_pathjson = pathlib.Path(folder_name).joinpath(filenamejson)
    with file_pathjson.open('r') as file:
        content = file.read()
    soup = BeautifulSoup(content, 'html.parser')
    text = soup.get_text()
    # Remove HTML tags using regex
    # text = re.sub(r'<[^>]+>', '', content)
    # Tokenize the text into words
    words = re.findall(r'\b\w+\b', text.lower())
    # Count the frequency of each word
    word_count = Counter(words)

    file_path = pathlib.Path(folder_name).joinpath(filenamefinaljson) # use pathlib to join paths
    with file_path.open('w') as file:
        # Write the total word count
        file.write(f"The total word count is: {len(words)}\n")       
        # Write the frequency of each word
        for word, count in word_count.items():
           file.write(f"{word} - occurs {count} times.\n")
        print(f"Json data saved to {file_path}")

#####################################
# Define a main() function for this module.
#####################################

def main() -> None:
    ''' Main function to demonstrate module capabilities. '''
    

#fetch_and_write_txt_data(folder_name,filenametxt,text_url)
fetch_and_write_json_data(folder_name, filenamejson, json_url)
fetch_and_write_excel_data(folder_name, filenamexls, excel_url)
#fetch_and_write_csv_data(folder_name, filenamecsv, csv_url)
#parse_text_data(folder_name, filenametxt, filenamefinaltxt)
#parse_csv_data(folder_name, filenamecsv, filenamefinalcsv)
parse_json_data(folder_name, filenamejson, filenamefinaljson)
parse_excel_data(folder_name, filenamexls, filenamefinalxls)


#####################################
# Conditional Execution
#####################################

if __name__ == '__main__':
    main()