# Free-ish Stock API

## Description
Python web service to retrieve stock information with Python using YFiance and CherryPy. 

Just for fun and because I Googled for way too long and couldnt't find something simple without someone trying to sell something. No, I dont want to pay for your class. No, I dont want to subscribe to your YouTube channel. And NO, I dont want to buy your API license.

TODO: 
* Update to use Flask or Django instead of CherryPy
* Build frontend to do consume API


## Setup/Pre-Requisites
- [OS: Ubuntu 20.04] (https://releases.ubuntu.com/20.04/)
- [Docker] (https://docs.docker.com/engine/install/ubuntu/)
- [Python 3.8.X or Higher] (https://www.python.org/downloads/)
- [Yahoo Finance API] (https://pypi.org/project/yfinance/)
- [CherryPy Framework] (https://pypi.org/project/CherryPy/)
- [Process and System Util] (https://pypi.org/project/psutil/)


## Key Features 
Web service with mutilpe endpoints returning JSON object
* /status: retuns various system information
* /getstock: returns data for one stock ticker
* /getstocks: returns data for multiple stock tickers


## Contributor(s)
- [Hong Phan](mailto:lhvphan@gmail.com)


## Getting Started
Download code and run as is or run as container. 


## Run Locally 
Run Python code standalone
```
python3 webservice.py
```


## Run as Docker Container
Build Docker container, must be in the same directory Dockerfile is
```
docker build -t python-ws .
```

Run Docker container with port mapping
```
docker run -p 8080:8080 python-ws
```


## Usage: Test Calls
Get various system information using curl. If you know how to use PostMan or ARC, go on with your fancy pants and make it happen
```
curl -H "Content-Type: application/json" -X GET http://localhost:8080/status
```

Get information for one stock, JSON with one stock {"value" : "<ticker_symbol>"}
```
curl -d '{"value" : "fb"}' -H "Content-Type: application/json" -X POST http://localhost:8080/getstock
```

Get information for multiple stocks, JSON with multiple stocks
```
curl -d '{"FaceBook" : "fb", "Amazon" : "amzn", "Apple" : "aapl", "Netflix" : "nflx", "Microsoft" : "msft", "Google" : "goog"}' \
    -H "Content-Type: application/json" \
    -X POST http://localhost:8080/getstocks
```


## Coffee Contribution
A bunch of if's
* If you made it to the bottom of this Readme
* If this project helps you
* If you are feeling generous
* Then consider donating to my coffee fund 

Thank you and make your day great! 

[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/donate/?hosted_button_id=9GKGUVF5WVM4G)