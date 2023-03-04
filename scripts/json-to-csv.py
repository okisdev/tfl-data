import os
import csv
import json


json_dir = 'json/tube/station'
csv_dir = 'csv/tube/station'


for filename in os.listdir(json_dir):
    if filename.endswith('.json'):
        json_path = os.path.join(json_dir, filename)

        with open(json_path, 'r') as json_file:
            data = json.load(json_file)

        csv_filename = f'{os.path.splitext(filename)[0]}.csv'
        csv_path = os.path.join(csv_dir, csv_filename)

        with open(csv_path, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(data.keys())
            writer.writerow(data.values())
