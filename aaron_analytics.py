""" This project 3 demonstates my ability to fench, parse and write differnt file types with python.
I plan to use some market files for my sample codes to process.
I will process .txt, .csv, .xlsx, and .json files"""

# Standard library imports
import csv
from pathlib import Path
import pathlib 
import json

# External library imports (requires virtual environment)
import requests 


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


filenametxt = "data.txt"
folder_name = f"{project_path}"

filenamejson = "data.json"
filenamecsv = "data.csv"
filenameexcel = "data.xls"

def fetch_and_write_txt_data(folder_name, filenametxt, text_url):
    response = requests.get(text_url)
    if response.status_code == 200:
        file_path = pathlib.Path(folder_name).joinpath(filenametxt) # use pathlib to join paths
        with file_path.open('w') as file:
            file.write(response.text)
        print(f"Text data saved to {file_path}")
    else:
        print(f"Failed to fetch data: {response.status_code}")

#def write_txt_file(folder_name, filename):
 #   file_path = pathlib.Path(folder_name).joinpath(filename) # use pathlib to join paths
 #   with file_path.open('w') as file:
 #       file.write(response.text)
 #   print(f"Text data saved to {file_path}")   
        
def fetch_and_write_excel_data(folder_name, filenameexcel, excel_url):
    response = requests.get(excel_url)
    if response.status_code == 200:
        file_path = pathlib.Path(folder_name).joinpath(filenameexcel) # use pathlib to join paths
        with file_path.open('w') as file:
            file.write(response.text)
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
    

fetch_and_write_txt_data(folder_name,filenametxt,text_url)
fetch_and_write_json_data(folder_name, filenamejson, json_url)
fetch_and_write_excel_data(folder_name, filenameexcel, excel_url)
fetch_and_write_csv_data(folder_name, filenamecsv, csv_url)

# write_txt_file(folder_name, filename, data)
#####################################
# Conditional Execution
#####################################

if __name__ == '__main__':
    main()