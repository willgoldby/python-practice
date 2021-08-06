# Given the names and grades for each student in a class of N students, store them in a 
# nested list and print the name(s) of any student(s) having the second lowest grade.
def second_lowest(n, student_list):
    names_scores = {} 
    if n == len(student_list):
        for student in student_list:
            names_scores[student[0]] = student[1]
        names_scores = dict(sorted(names_scores.items(), key=lambda score: score[1]))
        scores = set()
        for k, v in names_scores.items():
            scores.add(v)
        sorted_scores = sorted(list(scores))
        second_lowest = sorted_scores[1]
        students_with_second_score = []
        for student, score in names_scores.items():
            if score == second_lowest:
                students_with_second_score.append(student)
        students_with_second_score.sort()
        for name in students_with_second_score:
            print(name)



if __name__ == '__main__':
    num = int(input())
    scores =[]
    for _ in range(num):
        name = input()
        score = float(input())
        scores.append([name, score])
    
    second_lowest(num, scores)