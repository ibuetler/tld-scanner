from urllib.parse import urlparse
from threading import Thread
import http.client, sys, os, re, subprocess
import requests
import argparse


from queue import Queue

concurrent = 25
success = 0
errors = 0


def add_str_to_lines(f_name, str_to_add):
    with open(f_name, "r") as f:
        lines = f.readlines()
        for index, line in enumerate(lines):
            lines[index] = str_to_add + line.strip() + "\n"

    with open(f_name, "w") as f:
        for line in lines:
            f.write(line)

def doWork():
    while True:
        url = q.get()
        whoisresult = getStatus(url)
        if (int(len(whoisresult)) > 0):
            doSomethingWithResult(whoisresult, url)
        q.task_done()

def getStatus(ourl):
    try:
        whoisresult = subprocess.getoutput("dig ns " + ourl + " +short")
        return whoisresult
    except:
        error = 1

def doSomethingWithResult(whoisresult, domain):
    print(domain + ",\"" + whoisresult.replace('\n', ' ') + "\"")

# MAIN

parser = argparse.ArgumentParser(description='find tld of given domain')
parser.add_argument('-d', '--domain', help='domain (required)', type=str, metavar="DOMAIN", required=True)
args = parser.parse_args()


q = Queue(concurrent * 2)
f_name = "tlds-alpha-by-domain.txt"
d_name = "domains.txt"
t_uri = "https://data.iana.org/TLD/tlds-alpha-by-domain.txt"

# GET TLDS LIST
r = requests.get(t_uri)

if (r.ok):
    # GET ORIGINAL LIST 
    with open(f_name, 'wb') as f:
        f.write(r.content)

    # REMOVE LINES STARTING WITH #
    with open(d_name, 'w') as d:
        with open(f_name, 'r') as f:
            for line in f:
                if not (line.startswith('#')):
                    d.write(line)

    # ADDING OUR DOMAIN TO TLDS
    str_to_add = args.domain+'.'
    add_str_to_lines(f_name=d_name, str_to_add=str_to_add)


for i in range(concurrent):
    t = Thread(target=doWork)
    t.daemon = True
    t.start()

try:
    for url in open(d_name):  #Location of your CSV containing one domain per line
        q.put(url.strip())
    q.join()

except KeyboardInterrupt:
    sys.exit(1)
