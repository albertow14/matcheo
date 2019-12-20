import sys
import csv
from datetime import datetime
import requests
from errors import NoFileGived, FileMustBeACSV
 
def check_if_file_gived():
    if len(sys.argv) == 1:
            print('ERROR -> please give us a csv file to match')
            raise NoFileGived

def check_extension_is_csv(file_name):    
    file_extension = file_name[-3:]
    extension = file_extension.upper()    
    if extension != 'CSV':
        print('ERROR -> THE FILE MUST BE A CSV')
        raise FileMustBeACSV

check_if_file_gived()
file_name = sys.argv[1]
fails_name = file_name[:-4] + '_fails.csv'
delimeter = sys.argv[2] # TODO check if this parameter is written in ""
check_extension_is_csv(file_name)

fails = list()
with open(file_name) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=delimeter)
    for index, row in enumerate(csv_reader):        
        result = requests.get(row[0])
        if row[1] != result.url:
            fails.append([row[0], row[1]])

if len(fails) > 0:
    with open(fails_name, 'w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=delimeter)
        for fail_row in fails:
            now = datetime.now()
            current_time = now.strftime("%D-%H:%M:%S")
            fail_row.append(current_time)
            csv_writer.writerow(fail_row)
    
        


