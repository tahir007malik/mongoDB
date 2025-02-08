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

pipeline = [
    {
        "$group": {
            "_id": "$city",  # Group by the "city" field
            "employee_count": {"$sum": 1},  # Count employees in each city
            "total_salary": {"$sum": "$salary"},
            "avg_age": {"$avg": "$age"}
        }
    },
    {
        "$sort": {"total_salary": -1}
    }
]

results = collection.aggregate(pipeline)
for x in results:
    print(x)

# Close connection 
client.close()
