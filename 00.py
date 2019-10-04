with open("bookranking.csv", "r", errors='replace') as f:
    s = f.read()
s = s.replace("\\", "")

with open("bookranking.csv", "w", errors='replace') as f:
    f.write(s)