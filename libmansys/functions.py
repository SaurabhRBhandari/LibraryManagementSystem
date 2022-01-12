
from .models import Student
def if_new_user(request):
    '''Adds the current user to student list if not present'''
    student_list=Student.objects.all()#Get existing students
    student_id_list=[]#Stores the unique IDs of every student
    
    for student in student_list:
        student_id_list.append(student.user_ID)
        
    current_user_id=request.user.id#get the ID of current user
    
    if current_user_id not in student_id_list:#If the current user is not in database
        s=Student(user_ID=current_user_id)#Create a new user
        s.save()#Add it to the database