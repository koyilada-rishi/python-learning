di = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}

dil = [["I",1],["V",5],["X",10],["L",50],["C",100],["D",500],["M",1000]]

# dil[0].append(9)
# print(dil[0])
1000 + 100 + 1000 + 10 + 1 + 5
# Input: s = "III"
# Output: 3
# Explanation: III = 3.

# s = "III"
# s = "LVIII"
s = "MCMXCIV"
# s = "IV"
keys_list = list(di.keys())
res = 0
# for i in range(len(s)-1):
#     if keys_list[i] == "I" and keys_list[i+1] == "V":
#         res = res + di[s[i+1]] - di[s[i]]
#     elif keys_list[i] == "X" and keys_list[i+1] == "L":
#         res = res + di[s[i+1]] - di[s[i]]
#     elif keys_list[i] == "C" and keys_list[i+1] == "D":
#         res = res + di[s[i+1]] - di[s[i]]
#     else:
#         res = res + di[s[i]]
# print(res)

for i in range(len(s)-1):
    if (s[i] == "I" and s[i+1] == "V") or (s[i] == "I" and s[i+1] == "X"):
        res = di[s[i+1]] - di[s[i]]
        i = i + 2
    elif (s[i] == "X" and s[i+1] == "L") or (s[i] == "X" and s[i+1] == "C") :
        res = res + di[s[i+1]] - di[s[i]]
        i = i + 2
    elif (s[i] == "C" and s[i+1] == "D") or (s[i] == "C" and s[i+1] == "M") :
        res = res + di[s[i+1]] - di[s[i]]
        i = i + 2
    else:
        res = res + di[s[i]]
print(res)




di = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

s = "MCMXCIV"  # Expected output: 1994
res = 0

for i in range(len(s) - 1):
    if di[s[i]] < di[s[i + 1]]:  # If the current numeral is smaller than the next one, subtract it
        res -= di[s[i]]
    else:
        res += di[s[i]]

res += di[s[-1]]  # Add the last character since it is always positive
print("Converted Value:", res)
