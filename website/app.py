

### here starting page is home.html not index.html

import time
import requests
import json
from flask import Flask, jsonify,render_template,request

app = Flask(__name__)

api_key = "d095ca647af955e6df735431b2bb9f39374fa8e3e7e5c86e0892b6ff6042702c"

@app.route('/')
def index():
    return render_template('home.html')

########################################################################################################################
@app.route('/File Analysis', methods=['POST'])
def upload():
    url = "https://www.virustotal.com/api/v3/files"
    file = request.files['file']

    headers = {
        "x-apikey": api_key,
    }

    files = {'file': (file.filename, file.read())}

    response = requests.post(url, headers=headers, files=files)
    x = response.json()
    id = x["data"]["links"]["self"]

    response = requests.get(id, headers=headers)
    result = response.json()
    return render_template('fileresults.html', data=result["data"])

##############################################################################################################


@app.route('/Url Analysis', methods=['POST'])
def upload_url():
    url = request.form['url']

    url_scan_endpoint = "https://www.virustotal.com/api/v3/urls"

    headers = {
        'x-apikey': api_key,
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json'
    }

    data = {'url': url}

    response = requests.post(url_scan_endpoint, headers=headers, data=data)

    result = response.json()
    id=result["data"]["links"]["self"]
    response = requests.get(id, headers=headers)
    result=response.json()
    print(response.text)
    return render_template('index.html', data=result['data'])

##############################################################################################################

@app.route('/Ip Analysis', methods=['POST'])
def search():
    base_url = "https://www.virustotal.com/api/v3/ip_addresses/"
    search = request.form['search']
    
    # Construct the dynamic URL based on user input
    url = f"{base_url}{search}"

    headers = {
        'x-apikey': api_key,
        'accept': 'application/json'
    }

    response = requests.get(url, headers=headers)
    result = response.json()
    print(response.text)
    return render_template('searchresult.html', data=result['data'])

##############################################################################################################


if __name__ == "__main__":
    app.run(debug=True)
    #app.run(host='0.0.0.0', port=8000, debug=True) for docker