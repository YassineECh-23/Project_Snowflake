# 🚀 Automated Crypto Data Pipeline (ETL)

## 📌 Project Overview
This project is an automated **ETL (Extract, Transform, Load)** pipeline designed to track real-time cryptocurrency prices (Bitcoin & Ethereum).

It fetches financial data from the **CoinGecko API**, processes it using **Pandas**, and securely loads it into a **Snowflake Data Warehouse** for historical analysis and reporting.

## ⚙️ Architecture
**Source (API)** ➡️ **Transformation (Python/Pandas)** ➡️ **Storage (Snowflake DB)**

## 🛠️ Tech Stack
- **Language:** Python 3.x
- **Data Processing:** Pandas
- **Database:** Snowflake (via `snowflake-connector-python`)
- **API:** CoinGecko REST API
- **Security:** Environment variables (`python-dotenv`)

## 📊 Data Schema (Output)
The data is stored in the `CRYPTO_PRICES` table in Snowflake:

| crypto   | price_usd | timestamp           |
| :---     | :---      | :---                |
| bitcoin  | 45,230.50 | 2024-01-05 10:00:00 |
| ethereum | 3,100.20  | 2024-01-05 10:00:00 |

## 🚀 How to Run

### 1. Clone the repository
```bash
git clone https://github.com/YassineECh-23/Project_Snowflake.git
cd Project_Snowflake
2. Install dependencies
Bash

pip install -r requirements.txt
3. Configure Environment Variables
Create a .env file in the root directory and add your Snowflake credentials (do not share this file):

Extrait de code

SNOWFLAKE_USER=your_username
SNOWFLAKE_PASSWORD=your_password
SNOWFLAKE_ACCOUNT=your_account_id
SNOWFLAKE_WAREHOUSE=COMPUTE_WH
SNOWFLAKE_DATABASE=CRYPTO_DB
SNOWFLAKE_SCHEMA=RAW_DATA
4. Run the Pipeline
Bash

python insert_snowflake.py
🛡️ Security Note
This project uses a .gitignore file to ensure sensitive credentials (inside .env) are never committed to the repository.
