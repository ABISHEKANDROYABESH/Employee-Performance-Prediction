import pickle

# Just store a simple object instead of a custom class
model = {"message": "This is a dummy model", "predict": "High Performance"}

with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("model.pkl created successfully!")
