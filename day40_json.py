import json

# Python object
data = {
    "name": "Divya",
    "course": "Python",
    "skills": ["functions", "modules", "projects"]
}

# Convert Python object to JSON
json_data = json.dumps(data, indent=4)

print("JSON Data:")
print(json_data)
