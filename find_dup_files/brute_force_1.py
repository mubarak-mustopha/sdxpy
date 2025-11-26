import sys

def find_duplicates(filenames):
    matches = []
    for left in filenames:
        for right in filenames:
            if same_bytes(left, right):
                matches.append((left, right))
    return matches

def same_bytes(left_name, right_name):
    left_byte = open(left_name, "rb").read()
    right_byte = open(right_name, "rb").read()
    return left_byte == right_byte

if __name__=="__main__":
    duplicates = find_duplicates(sys.argv[1:])
    for (left, right) in duplicates:
        print(left, right)
