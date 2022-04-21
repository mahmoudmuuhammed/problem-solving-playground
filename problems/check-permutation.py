# Carcking Coding Interview Page 101 Q: 1.2

NO_OF_CHARS = 128;
def permutation(str1: str, str2: str):

    if len(str1) != len(str2):
        return False;
    
    count1 = [0] * NO_OF_CHARS;
    count2 = [0] * NO_OF_CHARS;

    for i in str1:
        count1[ord(i)] += 1;

    for i in str2:
        count2[ord(i)] += 1;

    for i in range(NO_OF_CHARS):
        if count1[i] != count2[i]:
            return False;

    return True;

str1 = input();
str2 = input();
data = permutation(str1, str2);
print(data);