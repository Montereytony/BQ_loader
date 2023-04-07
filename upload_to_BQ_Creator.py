#!/usr/bin/python
#
#
# Tony's Code to Automate uploading csv files
#
# First read list of csv files, then print command to upload to bq
#

import glob

#
# Load CSV files in folder 
#
csv_files = []
for file in glob.glob("*.csv"):
    csv_files.append(file)

#
# Loop through  CSV files and create Big Query load command. The output can be piped to bash
#

for csv_filename in csv_files:
    bq_db_name = "external_data_db"
    bq_table_name = csv_filename.split(".")
    load_cmd = 'bq load --replace=true --field_delimiter="|" --autodetect  --skip_leading_rows=2 --source_format=CSV '
    load_str = load_cmd +  bq_db_name  + "." + bq_table_name[0] + " " + csv_filename
    file_variable = open(csv_filename)
    all_lines_variable = file_variable.readlines()
    new_str = all_lines_variable[1].replace("|", ":STRING,") + ":STRING"
    new_str = ''.join(new_str.split('\n'))
    new_str = load_str +  "  " + new_str
    print("echo \'Doing  " + csv_filename + "\'" )
    print(new_str)
    print(" ")

