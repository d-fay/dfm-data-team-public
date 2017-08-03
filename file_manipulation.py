import os
import gzip
import shutil
import codecs
import csv
import petl as etl

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#   REQUIRES PYTHON 2 - Developed using python 2.7.13
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

file_name = 'example_report'


def unzip_csv_file():

    fullpath = os.path.join(os.path.dirname(__file__), file_name)
    file_in = gzip.open(fullpath + '.csv.gz', 'r')
    file_contents = csv.reader(file_in)

    file_out_csv = codecs.open(fullpath + '.csv', 'w')
    writer = csv.writer(file_out_csv)

    # REMOVE COMMAS AND '%' SYMBOLS FROM WITHIN CSV VALUES
    for line in file_contents:
        line = [value.replace(',', '') for value in line]
        line = [value.replace('%', '') for value in line]
        writer.writerow(line)

    file_in.close()
    file_out_csv.close()

    with open(fullpath + '.csv', 'rb') as f_in, gzip.open(fullpath + '_clean.csv.gz', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)


def extract_table_from_csv():
    # EXTRACT TABLE FROM FILE
    table = etl.fromcsv(file_name + '.csv')
    return table


