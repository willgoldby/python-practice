from collections import namedtuple

def second_best(n, name_scores):
    Student = namedtuple('Name', 'score')
    students = []
    if n == len(name_scores):
        for student in name_scores:
            print(student)
            name = student[0]
            score = student[1]
            name = Student(name, score)
            students.append(name)
    print(students)
        
if __name__ == '__main__':
    stats = []
    num = int(input())
    print(num)
    for _ in range(num):
        name = input()
        score = float(input())
        stats.append([name, score])
    second_best(num, stats)