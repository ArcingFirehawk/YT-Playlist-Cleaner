"""
PURPOSE: Counts the values in a .json file.
"""

import json



with open("Output/videoList.json") as f:
    file = json.load(f)
    f.close()

length = len(file)

print(length)