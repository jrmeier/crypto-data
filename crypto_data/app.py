from flask import Flask, request, send_from_directory

from os.path import isfile, join, dirname, abspath
app = Flask(__name__, static_url_path='')

@app.route('/<path>')
def send_js(path):
    daily_data_files_path = "{}/daily_data_files".format(dirname(abspath(__file__)))
    return send_from_directory(daily_data_files_path, path)

if __name__ == "__main__":
    app.run(debug=True)