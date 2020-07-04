#Finding longest polyindrome in the string

def longest_palindrome(string): 
    length = len(string)
    poli = [] ##Space O(n)
    for num in range(length, 0, -1): ##O(n^2)
        for s in range(length-num+1):
            target = string[s:s+num] #Space O(n)
            #print(target)

            #print("reverse string:",string[::-1])
            if target == string[::-1]:
                poli.append(string[::-1])
    return poli


strin = "abbccbba"
string = strin.lower()
print(string)
print(longest_palindrome(string))