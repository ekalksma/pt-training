fname = "data/numbers.csv"
data = ""

try:
    with open(fname, "r") as f:
        data = f.read()
except Exception as e:
    raise ValueError(f"Unable to read file {fname}") from e

data = data.split(",")
print (data[3340])