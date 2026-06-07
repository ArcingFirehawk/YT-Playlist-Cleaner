"""
PURPOSE: Testing reading files.
"""

import json



# Counts the values in a .json file.
def count():
    with open("Output/videoList.json") as f:
        file = json.load(f)
        f.close()

    length = len(file)

    print(length)


# Reads a text file named list.txt.
def read():
    with open("Test Files/list.txt") as f:
        list = f.read().splitlines()
        f.close()

    print(list)

    return list


# Tests what happens if list.txt is empty.
def test_empty():
    list1 = read()
    list2 = ["grain", "vegetable", "fruit", "apple"]

    print(list1)


    for i in range(len(list2)):
        if list2[i] in list1:
            print("\nbad\n")
        else:
            print(f"\n{list2[i]}\n")


def main():
    test_empty()


if __name__ == "__main__":
    main()