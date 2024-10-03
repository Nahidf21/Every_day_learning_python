import pandas as pd
import glob
import xml.etree.ElementTree as ET
from datetime import datetime
import json
import os
print(f"Current working directory: {os.getcwd()}")

log_file = "log_file.txt"
target_file = 'transform_data.csv'

def extract_from_csv(file_to_process):
    dataframe = pd.read_csv(file_to_process)
    return dataframe

def extract_from_json(file_to_process):
    dataframe = pd.DataFrame()  # Initialize an empty dataframe
    with open(file_to_process, 'r') as f:
        for line in f:
            json_obj = json.loads(line)  # Parse each line as a JSON object
            dataframe = pd.concat([dataframe, pd.DataFrame([json_obj])], ignore_index=True)
    return dataframe


def extract_from_xml(file_to_process):
    dataframe = pd.DataFrame(columns=['name', 'height', 'weight'])
    tree = ET.parse(file_to_process)
    root = tree.getroot()

    for person in root:
        name = person.find("name").text
        height = person.find("height").text
        weight = person.find("weight").text
        dataframe = pd.concat([dataframe, pd.DataFrame([{"name": name, "height": height, "weight": weight}])], ignore_index=True)
    return dataframe

def extract():
    extract_data = pd.DataFrame(columns=['name', 'height', 'weight'])

    for csvfile in glob.glob(r"C:\Users\nahid\Desktop\Python_World\ETL Coursera 2024\source\*.csv"):
        extract_data = pd.concat([extract_data, extract_from_csv(csvfile)], ignore_index=True)

    for jsonfile in glob.glob(r"C:\Users\nahid\Desktop\Python_World\ETL Coursera 2024\source\*.json"):
        extract_data = pd.concat([extract_data, extract_from_json(jsonfile)], ignore_index=True)
    
    for xmlfile in glob.glob(r"C:\Users\nahid\Desktop\Python_World\ETL Coursera 2024\source\*.xml"):
        extract_data = pd.concat([extract_data, extract_from_xml(xmlfile)], ignore_index=True)

    return extract_data

def transform(data):
    data['height'] = round(data['height'].astype(float) * 0.0254, 2)
    data['weight'] = round(data['weight'].astype(float) * 0.45359237, 2)

    return data

def load_data(target_file, transform_data):
    transform_data.to_csv(target_file, index=False)

def log_progress(message):
    timestamp_format = '%Y-%m-%d-%H:%M:%S'
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)
    with open(log_file, 'a') as f:
        f.write(f"{timestamp} , {message}\n")

# Log the initialization of the ETL process 
log_progress("ETL Job Started")

# Log the beginning of the Extraction process 
log_progress("Extract phase Started")
extracted_data = extract()

# Log the completion of the Extraction process 
log_progress("Extract phase Ended")

# Log the beginning of the Transformation process 
log_progress("Transform phase Started")
transformed_data = transform(extracted_data)
print("Transformed Data")
print(transformed_data)

# Log the completion of the Transformation process 
log_progress("Transform phase Ended")

# Log the beginning of the Loading process 
log_progress("Load phase Started")
load_data(target_file, transformed_data)

# Log the completion of the Loading process 
log_progress("Load phase Ended")

# Log the completion of the ETL process 
log_progress("ETL Job Ended")




