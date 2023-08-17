'''
599. Minimum Index Sum of Two Lists

Given two arrays of strings list1 and list2, find the common strings with the least index sum.

A common string is a string that appeared in both list1 and list2.

A common string with the least index sum is a common string such that if it appeared at list1[i] and list2[j] then i + j should be the minimum value among all the other common strings.

Return all the common strings with the least index sum. Return the answer in any order.

 

Example 1:

Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
Output: ["Shogun"]
Explanation: The only common string is "Shogun".
Example 2:

Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC","Shogun","Burger King"]
Output: ["Shogun"]
Explanation: The common string with the least index sum is "Shogun" with index sum = (0 + 1) = 1.
Example 3:

Input: list1 = ["happy","sad","good"], list2 = ["sad","happy","good"]
Output: ["sad","happy"]
Explanation: There are three common strings:
"happy" with index sum = (0 + 1) = 1.
"sad" with index sum = (1 + 0) = 1.
"good" with index sum = (2 + 2) = 4.
The strings with the least index sum are "sad" and "happy".

'''
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d={}
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    d[list1[i]] = i+j
        lst=[]
        for i,j in d.items():
            if j == min(d.values()):
                lst.append(i)
        return lst

#less time

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dic1 = {}
        for i, s in enumerate(list1):
            if s not in dic1:
                dic1[s] = i
            
        dic2 = {}
        for i,s in enumerate(list2):
            if s not in dic2:
                dic2[s] = i
        m = float('inf')
        ans = []
        for k,v in dic1.items():
            if k in dic2:
                p1 = v
                p2 = dic2[k]
                if m == p1 + p2:
                    ans.append(k)
                elif m > p1 + p2:
                    m = p1 + p2
                    ans = [k]
        return ans

#less memory

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        
        hashmap = dict()

        if len(list1) < len(list2):
            smallest = list1
            biggest = list2
        else:
            smallest = list2
            biggest = list1

        for i in range(len(smallest)):

            if smallest[i] in biggest:

                try:
                    hashmap[i + biggest.index(smallest[i])].append(smallest[i])

                except KeyError:
                    hashmap[i + biggest.index(smallest[i])] = [smallest[i]]

        return hashmap[min(hashmap.keys())]
    
