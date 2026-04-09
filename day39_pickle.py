import pickle

# Data to store
data = {"name": "Divya", "course": "Python"}

# Writing to file
with open("data.pkl", "wb") as file:
    pickle.dump(data, file)

print("Data saved successfully!")

# Reading from file
with open("data.pkl", "rb") as file:
    loaded_data = pickle.load(file)

print("Loaded Data:", loaded_data)
