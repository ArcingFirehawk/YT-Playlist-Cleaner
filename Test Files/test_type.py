"""
PURPOSE: Test how to get the type of an class and check it in a if statement.
"""


from Classes.Video import Video
import json

class1 = Video("hi", 654, "dave", 2345)

print(type(class1))


if type(class1) == Video:
    print("yes")
    dumped = json.dumps(class1.__dict__)
    with open("test.json", "w") as f:
        json.dump(dumped, f)
        
else:
    print("no")