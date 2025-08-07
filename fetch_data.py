import requests
import pandas as pd
from datetime import datetime, timezone

url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"
response = requests.get(url).json()

data = [
    {
        "crypto": k,
        "price_usd": v["usd"],
        "timestamp": datetime.now(timezone.utc)  # ✅ version moderne
    }
    for k, v in response.items()
]

df = pd.DataFrame(data)
print(df)
