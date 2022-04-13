# Chrome Keylogger
By Caleb Watts for the completion of COMP6841.

## About
This project is in two parts, the extension which collects the key strokes and the server which recieves and logs them. The extension is a chrome extension that functions by inserting javascript into the loaded page that reacts on keypresses. On a keypress the extension sends a request to a background js script which makes a POST request to the server.

The server recieves the POST request and then filters it out depndant on whether the substring 'login' is in the URL. If the substring is found it will then check the log to see if the source webpage is listed. If it is the key is appended to the existing keypresses else a new entry is made.

## Challenges
The most challenging part of developing a keylogger is determining a smart way to filter useful information (login credentials) from ordinary keystrokes. I resorted to checking the URL however this misses situations where a login is handled by a widget on an ordinary page.

## Reflection
### Keyloggers

## Requirements
- Chrome Browser
- Python 3
    - Flask
    - Flask CORS

## Installation
1. Enable developer mode in chrome.
2. Load unpacked extension from `./Keylogger/src`

## Use
Once installed run:
```cd ./Keylogger/server; python3 -m server```
This will start the server.

The server will passively recieve keystrokes from the extension.

To access the log you can open `log.json` in `./Keylogger/server` or by going to http://127.0.0.1:5000/dump which will dump the logfile to the page.