from datetime import datetime

#This acts as the parent class being used 
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

#THIS CLASS RECORDS THE FOLLOWING THINGS: attendanceID, date, status (present/absent)
class Attendance:
    def __init__(self, attendanceID,date,status):
        self.attendanceID = attendanceID
        self.date = date
        self.status = status

    def recordAttendance(self):
        print(f"Attendance Recorded: {self.status} on {self.date}")

#SYSTEM NOTIFICATION CLASS including notificationID, message, dateIssued
class Notification: 
    def __init__(self, notificationID,message,dateIssued):
        self.notificationID = notificationID
        self.message = message
        self.dateIssued = dateIssued
    def sendNotification(self):
        print(f"Notification sent: {self.message}")
        return True
    
#SYSTEM REPORT CLASS including reportID, typeOfReport, generatedDate
class Report:
    def __init__(self,reportID,typeOfReport, generatedDate):
        self.reportID = reportID
        self.type = typeOfReport
        self.generatedDate = generatedDate

    def generateReport(self):
        print(f"Generating {self.type} report....")

#SCHEDULE CLASS including scheduleID, courseName, timeSlot
class Schedule:
    def __init__(self,scheduleID,courseName,timeSlot):
        self.scheduleID = scheduleID
        self.courseName = courseName
        self.timeSlot = timeSlot
    def createSchedule(self):
        print(f"Schedule created for {self.courseName} at {self.timeSlot}")
        return True
    
#STUDENT CLASS INHERITING FROM USER
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

#ADMIN CLASS INHERITING FROM USER
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
    
#TEACHER CLASS INHERITING FROM USER
class Teacher(User):
    def __init__(self,userID,name,email,password):
        super().__init__(userID,name,email,password)

    def createSchedule(self,course,time):
        #Association happening here between Teacher and Schedule, object calling Schedule CLASS method
        #teacher USES A SCHEDULE
        newSchedule = Schedule(101,course,time)
        newSchedule.createSchedule()
        return newSchedule
    
    def markAttendance(self):
        print("Teacher marking class attendance....")
        return True
    
    #TEACHER GENERATING REPORT USING REPORT CLASS
    #A Teacher uses a report.
    # Here teacher is importing the report() method from the REPORT Class)
    def generateReport(self):
        report = Report(1, "Class Performance", datetime.now())
        report.generateReport()
        return report 
    
    def flagLowAttendance(self):
        print("Flagging students with low attendance....")
        return ["StudentA", "StudentB"]
    

#MAIN FUNCTION TO DEMONSTRATE THE WORKING OF THE CLASSES AND THEIR RELATIONSHIPS

if __name__ == "__main__":
    print("\n\n\n\n\n")
    print("--- 1. DIRECT Notification Test ---")
    
    # Direct testing: Creating a Notification object directly to check its functionality.
    # We use the 'Notification' class to create a new alert.
    alert_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    system_alert = Notification(
        notificationID=1001,
        message="Semester fee submission deadline is tomorrow.",
        dateIssued=alert_time
    )
    
    print(f"Notification Object created with ID: {system_alert.notificationID}")
    
    # Calling the Notification's method
    system_alert.sendNotification()
    
    print("\n--- 2. Admin Issuing Notifications Test (Association/Dependency) ---")
    
    # Step 1: Create an Admin object.
    # INHERITANCE: 'Admin' is a child of 'User'.
    myAdmin = Admin(4, "Mr. Head Administrator", "admin@uni.edu", "securepass")
    myAdmin.login() # Calls the inherited 'login' method from the 'User' parent class.
    
    # Step 2: Admin issues a mass notification.
    # ASSOCIATION (Conceptual): Admin's method uses the concept of Notification.
    # In a real system, this method would internally create and send Notification objects.
    notifications_sent = myAdmin.issueNotifications() 
    print(f"Admin action successful. Number of mass actions returned: {notifications_sent}")
    
    print("\n--- 3. Student Receiving Alerts Test ---")
    
    # Using the existing student object (or creating a new one)
    myStudent = Student(2, "Mahmood", "mahmood@uni.edu","mahmood1234") 
    
    # Simulating the student checking for alerts (which are usually notifications)
    alerts = myStudent.receiveAlerts()
    print(f"Student {myStudent.name} received alerts: {alerts}")