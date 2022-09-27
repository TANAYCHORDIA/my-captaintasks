#basic school administration tool
import csv

def write_into_csv(info_list):
    with open ('student_info.csv','a',newline='')as csv_file:
        writer=csv.writer(csv_file)
        if csv_file.tell()==0:
            writer.writerow(['NAME','AGE','CONTACT NUMBER','EMAIL ID'])#this code will only be printed only once at the start and not be repeated
        writer.writerow(info_list)

if __name__=='__main__':
    condition = True
    student_num= 1
    while(condition):#This while loop will only be executed if the condition variable is True
        student_info=input("Enter student information for student #{} in the following format(NAME,AGE,CONTACT_NUMBER,EMAIL_ID):".format(student_num))
        student_info_list=student_info.split(' ')#This splits 1 string into sub strings
        print('\nThe entered information is - \nNAME:{} \nAGE:{} \nCONTACT_NUMBER:{} \nEMAIL_ID:{}  '.format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))
        choice_check=input('Is the entered information correct(yes/no):')#this line of code allows the user to check wether the information inputed i scorrect or not 
        if choice_check=='yes':
            write_into_csv(student_info_list)#this line of code will add the data in the spreedsheet
            condition_check=input("Do you want to enter information for another student(yes/no):")#condition_check variable asks the user wether the user wants to add information on a another student
            if condition_check=='yes':
                condition= True
                student_num= student_num + 1
            elif condition_check == 'no':
                condition = False#if the condition_check== no ,then condition variable is now false and whle loop is terminated 
        elif choice_check=='no':#if choice_check==no, that means user had entered wrong data of the student and the while loop restarts
            print('\nPlease enter correct information:')






