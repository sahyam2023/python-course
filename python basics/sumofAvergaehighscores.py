student_scores = [80, 60, 50, 65, 75, 55]
def sum_score_above_average(p_student_scores):
    sum = 0
    len = 0
    for stud in p_student_scores:
        sum= sum+ stud
        len = len + 1
    avg= sum/len
    new_score=0
    for stud in p_student_scores:
        if stud>avg:
            new_score= new_score+stud
    
        
    return new_score

print(sum_score_above_average(student_scores))


#not really done by me, knew the logic but didn't know how to write, sorry 