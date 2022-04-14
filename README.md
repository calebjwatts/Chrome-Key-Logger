# Chrome Keylogger
By Caleb Watts for the completion of COMP6841.

## Table of Contents
  - [About](#about)
    - [This Project](#this-project)
    - [Keyloggers](#keyloggers)
      - [What are they?](#what-are-they)
      - [How have they been used?](#how-have-they-been-used)
      - [What can you do about them?](#what-can-you-do-about-them)
  - [Reflection](#reflection)
    - [Challenges](#challenges)
      - [Useful data](#useful-data)
      - [Designing Server/Frontend for log](#designing-serverfrontend-for-log)
    - [What I learned](#what-i-learned)
    - [Room for expansion](#room-for-expansion)
  - [References](#references)
  - [Requirements](#requirements)
  - [Installation](#installation)
  - [Use](#use)
## About
### This Project
This project is in two parts, the extension which collects the key strokes and the server which recieves and logs them. The extension is a chrome extension that functions by inserting javascript into the loaded page that reacts on keypresses. On a keypress the extension sends a request to a background js script which makes a POST request to the server.

The server recieves the POST request and will then either:
1. Create a new record for a new webpage; or
2. Append the keystroke to an existing record for a known webpage.

The records are saved on the server in a JSON file. This information can then be accessed remotely via the `/dump` endpoint or directly by reading the `log.json` file on the server.

### Keyloggers
Keyloggers are among the oldest classes of spyware. They vary from incredibly simple and limited in scope to very complex programs that have access to strokes across the whole machine.

#### What are they?
Keyloggers are programs that capture and record a user's keystrokes. They are a form of *spyware*, a class of malware that as the name describes - spies on users. They can capture significant amounts of private information including usernames, emails, passwords, and financial information; essentially they can capture anything you type. [^1]

They can vary in scope from being limited to a single application to across a whole machine.

#### How have they been used?
Keyloggers are used in many scenarios, some legitimate, others less than legal. 

An interesting example of legitimate use is given by Grammerly. Grammerly is a spellchecker/grammer checker that actively captures user inputs and provides the user with tips to improve their writing.[^1]

On the otherhand, they are often used to spy on people and businesses. One such business was Anthem. Anthem is a medical insurance provider in the United States and in 2015 was the victim of a data breach. [^2] As a result names, emails, medical information, social security numbers, amongst other information, of up to 80 million customers was stolen, leading to lawsuits costing the company US$115 million. [^3]

#### What can you do about them?
The best strategy is to avoid being infected in the first place and so normal startegies for avoiding malware and being safe apply here. 
* Don't download software without first checking that it is safe. 
* Don't insert random USBs into your machine.
* Don't click on emails and attachments from unknown or untrusted senders.
* Lock your machine if you leave it unattended (or better yet don't leave your machine unattended)

Essentially you can often avoid keyloggers, like most other forms of malware by practiving safe IT practices.

But as Richard says,
> A determined enough attacker will find a way...

## Reflection
### Challenges
#### Useful data
A challenge that keyloggers have is that they capture huge amounts of data. Every single key someone types is captured. This means that trying to find useful data is like trying to find a needle in a haystack. 

In this project I intitalliy tried to limit data captured by checking the URL for the string `"login"`, thinking that I would be able to limit the data to credentials in that way. However what I found was that a substantial number of popular sites, instead of having a login page they instead just have a widget on the site to handle the process. This meant that in those cases I was losing the opportunity to catch credentials.

In the end I decided that it would be better to simply capture all keystrokes. It was simpler than attempting to filter by URL or by other means. If I had more free time this would be an aspect I would like to further develop.


#### Designing Server/Frontend for log
This part of the project is something I had to learn. I have in the past developed simple static websites however they have often used other technologies that abstracted some of the lower level webdevelopment away (namely Jekyll). Here I had to develop a basic level of proficiency in making a simple page using Flask/Bootstrap.

The reason I decided to use this was that by the time I decided I wanted a 'pretty' keylog dump page, I had already developed the server that was recieving the keystrokes. Instead of rewriting the server I decided to look for a Flask based solution. This led me to initially using raw HTML and then Bootstrap.

Learning this was a bit of a challenge however I was able to develop a simple webpage that fits the purpose. It is something however I would like to further expand on.


### What I learned
In this project I learned a few things, namely about keyloggers, building a chrome extension, and building a webpage using Flask/bootstrap.


### Room for expansion
In completing this project I have identified a few areas that could be expanded upon in future iterations.
* Filtering - this would allow an attacker to more easily find useful data, such as financial information and user credentials.


## References
[^1] - [What is a Keylogger? How attackers can monitor everything you type](https://www.csoonline.com/article/3326304/what-is-a-keylogger-how-attackers-can-monitor-everything-you-type.html)

[^2] - [11 of the Largest Data Breaches of All Time (Updated)](https://www.opswat.com/blog/11-largest-data-breaches-all-time-updated)

[^3] - [Anthem Hacking Points to Security Vulnerability of Health Care Industry](https://www.nytimes.com/2015/02/06/business/experts-suspect-lax-security-left-anthem-vulnerable-to-hackers.html)

## Requirements
- Chrome Browser
- Python 3.9.12
    - Flask
    - Flask CORS
    - Flask Bootstrap


## Installation
1. Install prerequisite software
    1. [Chrome Browser](https://www.google.com.au/chrome/)
    2. [Python](https://wiki.python.org/moin/BeginnersGuide/Download)
    3. Python packages: 
```
pip3 install -r requirements.txt
```

2. Clone repository to local machine:
```
git clone git@github.com:hackermonke/Chrome-Key-Logger.git 
```
3. Enable developer mode in chrome.

4. Load unpacked extension from `./Chrome-Key-Logger/src`


The server will now run and the extension is now loaded into the browser.


## Use
Once installed run:
```cd ./Keylogger/server; python3 -m server```
This will start the server.

The server will passively recieve keystrokes from the extension.

To access the log you can open `log.json` in `./Chrome-Key-Logger/server` or by going to http://127.0.0.1:5000/dump which will display the log on a static webpage.