import json
import csv

# Open the json file and load its data
with open('20_copy.json') as f:
    data = json.load(f)

# Change the lines where "Responses" appear into "text"
for item in data:
    if "Responses" in item:
        item["text"] = item.pop("Responses")

# Write the data to a csv file
keys = data[0].keys()
with open('train.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(data)
