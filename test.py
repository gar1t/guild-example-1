import os

data = "data/foo.txt"

print("Contents of data file %s" % data)
print(open(data).read().rstrip())
