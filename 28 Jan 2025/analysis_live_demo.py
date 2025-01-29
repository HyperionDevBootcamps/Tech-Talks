'''
Scenario: generate summary reports for .csv files in a folder
'''

import os
import pandas as pd

# Folder containing datasets
folder_path = r'C:\Users\Sanana Mwanawina\Desktop\Commercial\Tech Talks\Automation with Python\files-to-organise'

# Iterate over all files
for filename in os.listdir(folder_path):

    # if statement to check for .csv files only
    if filename.endswith('.csv'):

        # Construct file path
        file_path = os.path.join(folder_path, filename)

        # Read in csv file
        df = pd.read_csv(file_path)

        # Generate summary report
        summary = df.describe()

        # Name for report file
        report_filename = f'{os.path.splitext(filename)[0]}_report.csv'
        report_path = os.path.join(folder_path, report_filename)

        # Save summary to report file
        summary.to_csv(report_path)

        # Print statement to confirm report has been made for file x
        print(f"Report generated for {filename} and saved as {report_filename}.")