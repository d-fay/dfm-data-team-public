import petl as etl
import psycopg2
import psycopg2.extras

# # # # # # # # # # # # # # # # # # # # # # # #
#   DATABASE CONNECTION & RELATED METHODS
# # # # # # # # # # # # # # # # # # # # # # # #

# CONNECT TO POSTGRES DATABASE
connection = psycopg2.connect('dbname=postgres')


def send_table_to_postgres(table):

    # SEND ETL DATA TO TABLE IN DATABASE --> WARNING: drop=True will erase existing data in specified table
    etl.todb(table, connection, 'digi_data', create=True, drop=True, dialect='postgresql')


def get_data_from_postgres_as_html():

    dictionary_cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

    table_string = "<table  style=\"border: 1px solid black; border-collapse: collapse;\">"

    dictionary_cursor.execute("SELECT * FROM digi_data")
    db_table_data = dictionary_cursor.fetchall()

    for row in db_table_data:
        table_string += "<tr style=\"border: 1px solid black;\">"
        for item in row:
            table_string += "<td style=\"border: 1px solid black;\">" + \
                            str(item) + "</td><td>" + \
                            "</td>"
        table_string += "</tr>"
    table_string += "</table>"

    return table_string
