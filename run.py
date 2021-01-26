import json, requests

apiKeyFile = open("apiKey.txt", "r")
accountNameFile = open("accountName.txt", "r")
apiKey = apiKeyFile.read().strip()
accountName = accountNameFile.read().strip()

print("Using Account Name: ", accountName)
print("Using API Key: ", apiKey)

url = "https://analytics.api.appdynamics.com/events/query"
headerdata = {'X-Events-API-AccountName': accountName, 'X-Events-API-Key': apiKey, 'Content-Type': 'application/vnd.appd.events+json;v=2', 'Accept': 'application/vnd.appd.events+json;v=2'}
query = "SELECT * from browser_records"

response = requests.post(url, data = query, headers = headerdata)
responseJSON = json.loads(response.content.decode('utf-8'))[0]

with open('appd-data.json', 'w', encoding='utf-8') as f:
  json.dump(responseJSON, f, ensure_ascii=False, indent=4)
  print('JSON written to disk')
