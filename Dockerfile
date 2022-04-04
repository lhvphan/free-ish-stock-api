from python:3.10.4-bullseye

RUN pip install yfinance
RUN pip install CherryPy
RUN pip install psutil

COPY serverinfo.py .
COPY financebackend.py .
COPY webservice.py .

EXPOSE 8080
ENTRYPOINT ["python", "webservice.py"]
