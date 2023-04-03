import json

def metric_units(key, v):
    if key == 'height':

    elif key == 'weight':

    else
        return v
def flatten_dict(d, parent_key='', sep='.'):
    items = []
    if isinstance(d, list):
        for i, v in enumerate(d):
            if isinstance(v, dict):
                items.extend(flatten_dict(v, f"{parent_key}{sep}{i}", sep).items())
            else:
                items.append((f"{parent_key}{sep}{i}", v))
    elif isinstance(d, dict):
        for k, v in d.items():
            new_key = f"{parent_key}{sep}{k}" if parent_key else k
            if isinstance(v, dict):
                items.extend(flatten_dict(v, new_key, sep).items())
            elif isinstance(v, list):
                items.extend(flatten_dict(v, new_key, sep).items())
            else:
                v = metric_units(new_key, v)
                items.append((new_key, v))
    return dict(items)


# Load the JSON data from a file
with open('pokedex.json') as f:
    data = json.load(f)

# Flatten the dictionary
for i, v in enumerate(data):
    flattened_data = flatten_dict(data[i])

# Print the flattened dictionary
print(flattened_data)