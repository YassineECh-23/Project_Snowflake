import snowflake.connector
import pandas as pd
import requests
from datetime import datetime, timezone
import logging

# Enable debug logging
# logging.basicConfig(level=logging.DEBUG)

# 1. Fetch crypto data
url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"
response = requests.get(url).json()

data = [
    {
        "crypto": k,
        "price_usd": v["usd"],
        "timestamp": datetime.now(timezone.utc)
    }
    for k, v in response.items()
]

df = pd.DataFrame(data)
print(df)

# 2. Connect to Snowflake
try:
    conn = snowflake.connector.connect(
        user='YASSINE',
        password='uRvCW8BZkzvM2n4',
        account='zvdggde-jq68575',  # lowercase, no .snowflakecomputing.com
        warehouse='ETL_WH',
        database='REALTIME_PROJECT',
        schema='RAW_DATA',
    )

    cursor = conn.cursor()
    cursor.execute("USE SCHEMA RAW_DATA")  # Ensure schema is set

    # 3. Create table if not exists and insert data
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS CRYPTO_PRICES (
            crypto VARCHAR,
            price_usd FLOAT,
            timestamp TIMESTAMP_TZ
        )
    """)
    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO CRYPTO_PRICES (crypto, price_usd, timestamp)
            VALUES (%s, %s, %s)
        """, (row.crypto, row.price_usd, row.timestamp.isoformat()))

    # 4. Close connection
    cursor.close()
    conn.close()
    print("Data inserted successfully into Snowflake!")
except Exception as e:
    logging.error(f"An error occurred: {e}")
    print(f"Error: {e}")