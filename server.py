import file_manipulation
import table_manipulation
import database
from flask import Flask, redirect, url_for

# # # # # # # # # # # # # # # #
#   FLASK APP SERVER LOGIC
# # # # # # # # # # # # # # # #
app = Flask(__name__)


@app.route("/")
def output():

    file_manipulation.unzip_csv_file()
    table = file_manipulation.extract_table_from_csv()

    # PREVIEW TABLE (BEFORE CLEANING)
    print("Before: ")
    print(table)

    # CLEAN UP TABLE DATA
    table = table_manipulation.clean_table_headers(table)
    table = table_manipulation.clean_table_data(table)

    # PREVIEW TABLE (AFTER CLEANING)
    print("After: ")
    print(table)

    # SEND TABLE DATA TO DATABASE
    database.send_table_to_postgres(table)

    # REDIRECT INDEX TO RESULTS PAGE
    return redirect(url_for('results'))


@app.route("/results")
def results():
    return database.get_data_from_postgres_as_html()


if __name__ == "__main__":
    app.run(debug=True)
