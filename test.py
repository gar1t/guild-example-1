import os

data = "foo.txt"

print("Contents of data file %s" % data)
print(open(os.path.join("data", data)).read().rstrip())
