import requests

url = "https://analytics.api.appdynamics.com/events/query"
headers = {}
query = "SELECT * from browser_records"

data = requests.post(url, query, headers)

print(data)
