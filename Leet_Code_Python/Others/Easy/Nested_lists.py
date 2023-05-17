'''
Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

Example

The ordered list of scores is , so the second lowest score is . There are two students with that score: . Ordered alphabetically, the names are printed as:

Constraints

There will always be one or more students having the second lowest grade.
Output Format

Print the name(s) of any student(s) having the second lowest grade in. If there are multiple students, order their names alphabetically and print each one on a new line.

Sample Input 0

5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
Sample Output 0

Berry
Harry
Explanation 0

There are  students in this class whose names and grades are assembled to build the following list:

python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

The lowest grade of  belongs to Tina. The second lowest grade of  belongs to both Harry and Berry, so we order their names alphabetically and print each name on a new line


'''
lst=[["Harry",37.21],["Berry",37.21],["Tina",37.2],["Akriti",41],["Harsh",39]]

if __name__ == '__main__':
    nestedlist = []
    allscores = []
    secondstudents = []

    for _ in range(int(input())):
            name = input()
            score = float(input())
            nestedlist.append([name,score])
            allscores.append(score)

    secondgrade = sorted(set(allscores))[1]

    for i in range(len(nestedlist)):
            if nestedlist[i][1] == secondgrade:
                    secondstudents.append(nestedlist[i])

    secondstudents.sort()

    for i in range(len(secondstudents)):
            print(secondstudents[i][0])
        
