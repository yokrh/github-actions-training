import sys
import os

print("hello github action")
print(sys.version)
print(os.getcwd())

# path = "../../../doc/sandbox/a.yml"
path = "doc/sandbox/a.yml"

with open(path) as f:
  s = f.read()
  print(s)
