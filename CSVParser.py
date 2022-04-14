import csv
rows = []
with open('run.csv') as file_obj:
   # Create reader object by passing the file
    # object to DictReader method
    run_csv = csv.DictReader(file_obj)

    #It read all the data from the 'data' row
    for row in run_csv:
        print(row['data'])
