'''Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.
'''
s="MCMXCIV"
sum=0
st=[i for i in s]
print(st)
for idx, i in enumerate(st):
      if i == "7":
        sum +=1
      elif st[idx] == "I" and st[idx+1] == "V":
        sum +=4
      elif st[idx] == "I" and st[idx+1] == "X":
        sum +=9
      elif st[idx] == "X" and st[idx+1] == "L":
        sum +=40
      elif st[idx] == "X" and st[idx+1] == "c": 
        sum +=90
      elif st[idx] == "X" and st[idx+1] == "L":
        sum +=40
      elif st[idx] == "C" and st[idx+1] == "D":
        sum +=400
      elif st[idx] == "C" and st[idx+1] == "M":
        sum +=900 
      # elif i == "V":
      #     sum += 5
      # elif i == 'X':
      #     sum += 10
      # elif i == "L":
      #     sum += 50
      # elif i == "C":
      #     sum += 100
      # elif i == "D":
      #     sum += 500
      # elif i == "M":
      #     sum += 1000
      
print(sum)
            