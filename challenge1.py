import requests
from datetime import date , timedelta
import json

peroid = date.today() - timedelta(days=30)

response = requests.get(f'https://api.github.com/search/repositories?q=created:%3E{peroid}&sort=stars&order=desc')
data = json.loads(response.text)
print(f"The 100 most treanding repos in {peroid} {json.dumps(data['items'] , indent=3)}")




