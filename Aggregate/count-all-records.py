from pymongo import MongoClient
from urllib.parse import quote_plus  # Import for URL encoding
from dotenv import load_dotenv
import os
load_dotenv()


username = quote_plus(os.getenv('MongoDB_USERNAME'))  # Replace with your MongoDB username
password = quote_plus(os.getenv('MongoDB_PASSWORD'))  # Replace with your MongoDB password

uri = f"mongodb+srv://{username}:{password}@mongo-db-cluster-1.xrle0.mongodb.net/?retryWrites=true&w=majority&appName=mongo-db-cluster-1"  # Replace with your MongoDB host 

client = MongoClient(uri)
db = client["tahirtesting"]  # Connect to the database
collection = db["collectionmain"]  # Connect to the collection

# Count all records in the collection
# query = "" # If you want to count records according to some query
record_count = collection.count_documents({}) # Put query inside ({ query })
print(f"Total number of records in the collection: {record_count}")

# Close connection 
client.close()
