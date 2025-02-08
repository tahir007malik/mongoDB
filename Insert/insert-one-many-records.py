from pymongo import MongoClient
from urllib.parse import quote_plus  # Import for URL encoding
from dotenv import load_dotenv
import os
load_dotenv()
import time

username = quote_plus(os.getenv('MongoDB_USERNAME'))  # Replace with your MongoDB username
password = quote_plus(os.getenv('MongoDB_PASSWORD'))  # Replace with your MongoDB password

uri = f"mongodb+srv://{username}:{password}@mongo-db-cluster-1.xrle0.mongodb.net/?retryWrites=true&w=majority&appName=mongo-db-cluster-1"  # Replace with your MongoDB host 

client = MongoClient(uri)
db = client["tahirtesting"]  # Connect to the database
collection = db["collectionmain"]  # Connect to the collection

result = collection.insert_one({"name": "Amanda Kyle", "age": 35, "department": "Finance", "city": "New York", "salary": 56000})
print(f"Inserted record with ID: {result.inserted_id}")

# all_records = [
#     {"name": "Amanda Kyle", "age": 35, "department": "Finance", "city": "New York", "salary": 56000},
#     {"name": "Brandon Combs", "age": 47, "department": "Finance", "city": "Boston", "salary": 78107},
#     {"name": "Chloe Adams", "age": 29, "department": "IT", "city": "San Francisco", "salary": 72000},
#     {"name": "Daniel Smith", "age": 41, "department": "Marketing", "city": "Chicago", "salary": 65500},
#     {"name": "Emily Clarke", "age": 31, "department": "HR", "city": "New York", "salary": 60500},
#     {"name": "Frank Harris", "age": 38, "department": "IT", "city": "Boston", "salary": 81000},
#     {"name": "Grace Taylor", "age": 26, "department": "R&D", "city": "San Francisco", "salary": 75000},
#     {"name": "Hannah Lee", "age": 45, "department": "Finance", "city": "Chicago", "salary": 79000},
#     {"name": "Isaac Green", "age": 37, "department": "Sales", "city": "Boston", "salary": 68000},
#     {"name": "Jessica Brown", "age": 33, "department": "Marketing", "city": "New York", "salary": 72000}
# ]
# result = collection.insert_many(all_records)
# print(f"Inserted record with ID: {result.inserted_ids}")

# Close connection 
client.close()
