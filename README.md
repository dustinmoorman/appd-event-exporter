# AppD Event Exporter

A tool to pull AppD events and store them outside of AppD.  This repo is meant to be a starting point for data extraction, and intended to be extended to fit your data storage requirements by providing an easy way to extract data with Python.

Currently, running the application after setting the account & api key, will result in a JSON payload based on your query, named `appd-data.json`.

## Usage

1. `mv accountName.txt.dist accountName.txt` and replace it with your Global Account Name
2. `mv apiKey.txt.dist apiKey.txt` and replace the contents with your Analytics API Key
3. Run `python3 run.py`
