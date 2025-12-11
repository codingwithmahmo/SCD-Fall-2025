from datetime import datetime

# This acts as the parent class being used 
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

# THIS CLASS RECORDS THE FOLLOWING THINGS: attendanceID, date, status (present/absent)
class Attendance:
    def __init__(self, attendanceID,date,status):
        self.attendanceID = attendanceID
        self.date = date
        self.status = status

    def recordAttendance(self):
        print(f"Attendance Recorded: {self.status} on {self.date}")

# SYSTEM NOTIFICATION CLASS including notificationID, message, dateIssued
class Notification: 
    def __init__(self, notificationID,message,dateIssued):
        self.notificationID = notificationID
        self.message = message
        self.dateIssued = dateIssued
    def sendNotification(self):
        print(f"Notification sent: {self.message}")
        return True
    
# SYSTEM REPORT CLASS including reportID, typeOfReport, generatedDate
class Report:
    def __init__(self,reportID,typeOfReport, generatedDate):
        self.reportID = reportID
        self.type = typeOfReport
        self.generatedDate = generatedDate

    def generateReport(self):
        print(f"Generating {self.type} report....")

# SCHEDULE CLASS including scheduleID, courseName, timeSlot
class Schedule:
    def __init__(self,scheduleID,courseName,timeSlot):
        self.scheduleID = scheduleID
        self.courseName = courseName
        self.timeSlot = timeSlot
    def createSchedule(self):
        print(f"Schedule created for {self.courseName} at {self.timeSlot}")
        return True
    
# STUDENT CLASS INHERITING FROM USER
class Student(User):
    def __init__(self, userID,name,email,password):
        super().__init__(userID,name,email,password)
        # 🟢 COMPOSITION IMPLEMENTATION START
        # According to the UML Diagram (black diamond), Student 'owns' Attendance records.
        # If Student is deleted, these records are logically deleted too.
        # This list attribute establishes the Composition relationship.
        self.attendance_records = [] 
        # 🟢 COMPOSITION IMPLEMENTATION END
        
    def viewDashboard(self):
        print(f"Displaying dashboard for student: {self.name}")
        # Demonstrating Composition: Student viewing its own Attendance records
        print(f"Student has {len(self.attendance_records)} attendance records.")
        
    def addAttendanceRecord(self, date, status):
        # 🟢 COMPOSITION ACTION
        # Creating a new Attendance object and storing it permanently in the Student's list.
        new_attendance = Attendance(len(self.attendance_records) + 1, date, status)
        self.attendance_records.append(new_attendance)
        new_attendance.recordAttendance()
        
    def markAttendance(self):
        print(f"Student attempting to mark attendance.....")
        return True
    def receiveAlerts(self):
        print("Checking Alerts.....")
        return ["Alert1", "Alert2"]
    
    def submitLeaveApplication(self):
        print("Leave Application submitted successfully.")

# ADMIN CLASS INHERITING FROM USER
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
        # 🟡 ASSOCIATION/DEPENDENCY: Admin uses the concept of a File object (or Report) temporarily.
        return "File_Object"
    
    def configureSettings(self):
        print("System settings configured")
        return True
    
    def issueNotifications(self):
        print("Issuing mass notifications")
        # 🟡 ASSOCIATION/DEPENDENCY: Admin uses the Notification class functionality.
        return 1
    
# TEACHER CLASS INHERITING FROM USER
class Teacher(User):
    def __init__(self,userID,name,email,password):
        super().__init__(userID,name,email,password)

    def createSchedule(self,course,time):
        # 🟡 ASSOCIATION/DEPENDENCY: Teacher uses the Schedule class temporarily within this method.
        # The Schedule object is created locally and returned/used. This is NOT Aggregation/Composition.
        newSchedule = Schedule(101,course,time)
        newSchedule.createSchedule()
        return newSchedule
    
    def markAttendance(self):
        print("Teacher marking class attendance....")
        return True
    
    def generateReport(self):
        # 🟡 ASSOCIATION/DEPENDENCY: Teacher uses the Report class temporarily within this method.
        # A Teacher uses a report object to generate output.
        report = Report(1, "Class Performance", datetime.now())
        report.generateReport()
        return report 
    
    def flagLowAttendance(self):
        print("Flagging students with low attendance....")
        return ["StudentA", "StudentB"]
    

# MAIN FUNCTION TO DEMONSTRATE THE WORKING OF THE CLASSES AND THEIR RELATIONSHIPS

if __name__ == "__main__":
    print("\n\n\n\n\n")
    
    # --- 1. Inheritance and Simple Functionality Test ---
    myStudent = Student(2, "Mahmood", "mahmood@uni.edu","mahmood1234") 
    print("--- 1. Inheritance Test ---")
    myStudent.login() # Inherited from User
    
    # --- 2. Composition Test (Student and Attendance) ---
    print("\n--- 2. Composition Test ---")
    # 🟢 Demonstrating the Composition relationship: Student creates and owns Attendance records.
    myStudent.addAttendanceRecord(datetime.now().strftime("%Y-%m-%d"), "Present")
    myStudent.addAttendanceRecord(datetime.now().strftime("%Y-%m-%d"), "Absent")
    myStudent.viewDashboard() # Now shows 2 records

    # --- 3. Association Test (Teacher and Schedule/Report) ---
    print("\n--- 3. Association Test ---")
    myTeacher = Teacher(10, "Mr. Islam Abbasi", "islam@uni.edu", "pass123")
    
    # 🟡 Teacher using Schedule (Association)
    myTeacher.createSchedule("Software Construction", "10:00 AM")
    
    # 🟡 Teacher using Report (Association)
    myTeacher.generateReport()
    
    print("\n--- 4. Admin and Dependency Test ---")
    myAdmin = Admin(4, "Mr. Head Administrator", "admin@uni.edu", "securepass")
    notifications_sent = myAdmin.issueNotifications() 
    print(f"Admin action successful. Mass notifications count: {notifications_sent}")