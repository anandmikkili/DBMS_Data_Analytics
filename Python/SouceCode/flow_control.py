student_marks = {'A':45,'B':23, 'C':56, 'D':56,'E':25, 'F':80}
for key, val in student_marks.items():
    if(val>=70):
        status = "First Division"
        print("Student {} exam status is: {}".format(key,status))
    elif((val>=50) and (val<70)):
        status = "Second Division"
        print("Student {} exam status is: {}".format(key,status))
    elif((val>=35) and (val<50)):
         status = "Third Division"
         print("Student {} exam status is: {}".format(key,status))
    else:
        status = "Failed"
        print("Student {} exam status is: {}".format(key,status))
        
