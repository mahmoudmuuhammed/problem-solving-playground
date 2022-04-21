# Carcking Coding Interview Page 101 Q: 1.1

def isUnique(str: str):
    dict = {};
    for letter in str:
        if letter in dict:
            return True;

        dict[letter] = letter;
    return False;


str = input().strip();

print(isUnique(str));