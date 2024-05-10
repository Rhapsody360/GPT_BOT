# Read the original file
with open('mental_health_dataset.json', 'r') as original_file:
    lines = original_file.readlines()

# Add a comma to the end of each line
modified_lines = [line.strip() + ',\n' for line in lines]

# Write the modified lines back to the file
with open('mental_health_dataset_new.json', 'w') as modified_file:
    modified_file.writelines(modified_lines)



import pandas as pd
df = pd.read_json("20.json")
print(df.head(5))

