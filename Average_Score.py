from turtledemo.chaos import jumpto

grades = [[5,3,3,5,4],[2,2,2,3],[4,5,5,2],[4,4,3],[5,5,5,4,5]]
students = {"Johnny","Bilbo","Steve","Khendrik","Aaron"}
journal={}

#Средний балл
average_score = [sum(((grades[0]))) / len((grades[0])),
                 sum(((grades[1]))) / len((grades[1])),
                 sum(((grades[2]))) / len((grades[2])),
                 sum(((grades[3]))) / len((grades[3])),
                 sum(((grades[4]))) / len((grades[4]))]

student_sort = list(students)
student_sort.sort()
journal = dict([(student_sort[0],average_score[0]),
                (student_sort[1],average_score[1]),
                (student_sort[2],average_score[2]),
                (student_sort[3],average_score[3]),
                (student_sort[4],average_score[4])])
print(journal)