from asyncio.windows_events import NULL
from contextlib import nullcontext
import requests
from bs4 import BeautifulSoup
import concurrent.futures
import re
from flask import Flask, render_template
import flask.cli


app= Flask(__name__)

@app.route('/')
def index():
    ctr=0

    CarArray=[]

    file_to_read=open('output.txt', 'r')

    counter=0
    currentLink=''
    currentModel=''

    for line in file_to_read:
        if not counter % 2:
            currentModel=line.strip()
        else:
            currentLink=line.strip()
            CarArray.append([currentModel, currentLink])

        counter+=1
    
    return render_template("index.html", lista=CarArray)


if __name__=='__main__':
    app.run()




