from flask import Flask
import json
import pymongo

app = Flask(__name__)

client = pymongo.MongoClient("ds113495.mlab.com", 13495)
db = client["hack2hire"]
db.authenticate("admin", "121abhi")

@app.route("/")
def hello():
    print("after db")

    collection_ht = db['data_ht']
    with open('data_ht.json') as f:
        file_data = json.load(f)

    collection_ht.insert(file_data)
    client.close()
    return "Hack2Hire Server running!"
 
if __name__ == "__main__":
    app.run()