#Read and Write JSON(dump,load)
import json
data = {"name": "Ahmad", "age": 21, "city": "Lahore"}

# Writing JSON data to a file
with open('data.json', 'w') as f:
    json.dump(data, f)
    
# Reading JSON data from a file
with open('data.json', 'r') as f:
    loaded_data = json.load(f)
    print(loaded_data)
    