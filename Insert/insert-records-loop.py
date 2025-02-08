from pymongo import MongoClient
from urllib.parse import quote_plus  # Import for URL encoding
from dotenv import load_dotenv
import os
load_dotenv()
from faker import Faker
import random
import time

username = quote_plus(os.getenv('MongoDB_USERNAME'))  # Replace with your MongoDB username
password = quote_plus(os.getenv('MongoDB_PASSWORD'))  # Replace with your MongoDB password

uri = f"mongodb+srv://{username}:{password}@mongo-db-cluster-1.xrle0.mongodb.net/?retryWrites=true&w=majority&appName=mongo-db-cluster-1"  # Replace with your MongoDB host 

client = MongoClient(uri)
db = client["tahirtesting"]  # Connect to the database
collection = db["collectionmain"]  # Connect to the collection

fake = Faker() # Initialize Faker for dummy data
departments = ["HR", "IT", "Finance", "Marketing", "Sales", "Operations", "R&D"]
cities = ["New York", "Los Angeles", "Chicago", "San Francisco", "Seattle", "Austin", "Boston", "Denver", "San Diego", "Phoenix"]

while True:
    employee = {
        "name": fake.name(),
        "age": random.randint(22, 60),
        "department": random.choice(departments),
        "city": random.choice(cities),
        "salary": random.randint(50000, 100000),
    }
    insert_result = collection.insert_one(employee)
    print(f"Inserted record with ID: {insert_result.inserted_id}")
    time.sleep(.1)
    employee.clear()
    
# Close connection 
client.close()
