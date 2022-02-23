import pwinput
import os
# from CourseAdder import runCourseAdder
from TranscriptAnalyser import TranscriptAnalyser
from User import User

transcriptAnalyser = TranscriptAnalyser()
user = User()

user.username = input("Enter your Poly username : ")
user.password = pwinput.pwinput(prompt="Enter your Poly password : ")
user.dob = input("Enter your date of birth (YYYYMMDD or YYMMDD) : ")
user.email = input("Enter your email : ")

#isMenuCompleted = False

# while(not isMenuCompleted):
os.system('CLS')
# print("Select one of the following option :")
# selectedOption = input(
#     "1) Transcript Analysis - Notify you when a new grade is added to your transcript.\n2) Schedule Modifier - Adds a course to your schedule as soon as a spot becomes available. An email is then sent to you.\n")
# if(selectedOption == '1'):
# os.system('CLS')

print("Transcript Analysis - Program that notifies you when a new grade is added to your transcript.\n")
coursesRaw = input(
    "Enter the courses for grades (separated by comma) : ").upper().replace(" ", "")
transcriptAnalyser.courses = coursesRaw.split(',')
transcriptAnalyser.runTranscriptAnalyser(user)

# elif(selectedOption == '2'):
#     os.system('CLS')
#     print("Schedule Modifier - Adds a course to your schedule as soon as a spot becomes available. An email is then sent to you.\n")
#     courseNumber = input("Enter the course name : ")
#     thGroup = input("Enter the theoretical group number : ")
#     labGroup = input("Enter the lab group number : ")
#     runCourseAdder(username, password, dob, email,
#                    courseNumber, thGroup, labGroup)
# else:
#   print("Invalid option")
