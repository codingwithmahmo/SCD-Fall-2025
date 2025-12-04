from datetime import datetime


#PARENT CLASS
class User:
    def __init__(self,userID,name,email,password):
        self.userID = userID
        self.name = name
        self.email = email 
        self.password = password

    def login(self):
        print(f"{self.name} has logged in successfully!")
    def recoverPassword(self):
        print(f"Password recovery email sent to {self.email}")


class Attendance:
    def __init__(self, attendanceID,date,status):
        self.attendanceID = attendanceID
        self.date = date
        self.status = status

    def recordAttendance(self):
        print(f"Attendance Recorded: {self.status} on {self.date}")

class Notification: 
    def __init__(self, notificationID,message,dateIssued):
        self.notificationID = notificationID
        self.message = message
        self.dateIssued = dateIssued
    def sendNotification(self):
        print(f"Notification sent: {self.message}")
        return True
    
class Report:
    def __init__(self,reportID,typeOfReport, generatedDate):
        self.reportID = reportID
        self.type = typeOfReport
        self.generatedDate = generatedDate

    def generateReport(self):
        print(f"Generating {self.type} report....")

class Schedule:
    def __init__(self,scheduleID,courseName,timeSlot):
        self.scheduleID = scheduleID
        self.courseName = courseName
        self.timeSlot = timeSlot
    def createSchedule(self):
        print(f"Schedule created for {self.courseName} at {self.timeSlot}")
        return True
    


class Student(User):
    def __init__(self, userID,name,email,password):
        super().__init__(userID,name,email,password)
    def viewDashboard(self):
        print(f"Displaying dashboard for student: {self.name}")
    def markAttendance(self):
        print(f"Student attempting to mark attendance.....")
        return True
    def receiveAlerts(self):
        print("Checking Alerts.....")
        return ["Alert1", "Alert2"]
    
    def submitLeaveApplication(self):
        print("Leave Application submitted successfully.")


class Admin(User):
    def __init__(self,userID,name,email,password):
        super().__init__(userID,name,email,password)

    def addUser(self):
        print("New user added to system")
        return True
    
    def removeUser(self):
        print("User removed from system")

    def editPermissions(self):
        print("Permissions Updated")
        return True
    
    def exportReport(self):
        print("Exporting report file.....")
        return "File_Object"
    
    def configureSettings(self):
        print("System settings configured")
        return True
    
    def issueNotifications(self):
        print("Issuing mass notifications")
        return 1
    
class Teacher(User):
    def __init__(self,userID,name,email,password):
        super().__init__(userID,name,email,password)

    def createSchedule(self,course,time):
        newSchedule = Schedule(101,course,time)
        newSchedule.createSchedule()
        return newSchedule
    
    def markAttendance(self):
        print("Teacher marking class attendance....")
        return True
    
    def generateReport(self):
        report = Report(1, "Class Performance", datetime.now())
        report.generateReport()
        return report 
    
    def flagLowAttendance(self):
        print("Flagging students with low attendance....")
        return ["StudentA", "StudentB"]
    

#testing code from here onwards 

if __name__ == "__main__":
    #Step 1: Creating a teacher (inheritance taking place)
    myTeacher = Teacher(1,"Sir Jafir", "jafirkhan@uni.edu","pass123")
    myTeacher.login()

    #Step 2: Teacher creates a schedule (association happening here)
    myTeacher.createSchedule("Software Engineering", "10:00 AM")

    #Step 3: Creating a student
    myStudent = Student(2, "Mahmood", "mahmood@uni.edu","mahmood1234")
    myStudent.viewDashboard()
    myStudent.submitLeaveApplication()

    print("\n\n\n\n")

    teacher2 = Teacher(1,"Sir Mir Jafar","mirjafar@uni.edu","mirjafar123")
    teacher2.login()

    teacher2.createSchedule("Data Structures & Algorithms","11:20 AM")
    

    student2 = Student(3,"Asif Khan","asifkhan@uni.edu","asifkhan1234")
    student2.viewDashboard()
    student2.submitLeaveApplication()