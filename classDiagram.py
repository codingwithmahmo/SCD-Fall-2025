from datetime import datetime

# --- CORE DATA CLASSES ---

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
        # Using string date format for consistency with original code's __main__ block
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
    
# --- USER ROLE CLASSES (INHERITANCE) ---

#implements "is a" relationship as "student is a user"
class Student(User):
    def __init__(self, userID,name,email,password):
        super().__init__(userID,name,email,password)
        # 🟢 Composition: Student 'owns' Attendance records (black diamond)
        self.attendance_records = [] 
        # Association: Student 'receives' Notifications
        self.alerts = []
        
    def viewDashboard(self):
        print(f"Displaying dashboard for student: {self.name}")
        print(f"Student has {len(self.attendance_records)} attendance records.")
        
    def addAttendanceRecord(self, date, status):
        # Composition between Student & Attendance
        # if student is deleted this shall be deleted as well along with it's data
        new_attendance = Attendance(len(self.attendance_records) + 1, date, status)
        self.attendance_records.append(new_attendance)
        new_attendance.recordAttendance()
        
    def markAttendance(self):
        print(f"Student attempting to mark attendance.....")
        return True
    
    def receiveAlerts(self):
        print("Checking Alerts.....")
        return self.alerts
    
    def submitLeaveApplication(self):
        print("Leave Application submitted successfully.")

    # Helper method for demonstration
    def addAlert(self, notification_obj):
        self.alerts.append(notification_obj)


class Admin(User):
    def __init__(self,userID,name,email,password):
        super().__init__(userID,name,email,password)
        self.managed_users = [] 

    def addUser(self, user_obj):
        # Update the managed_users list when adding a user
        self.managed_users.append(user_obj)
        print(f"New user {user_obj.name} added to system and is now managed by Admin.")
        return True
    
    def removeUser(self, user_obj):
        if user_obj in self.managed_users:
            self.managed_users.remove(user_obj)
            print(f"User {user_obj.name} removed from system and Admin's management list.")
        else:
             print(f"User {user_obj.name} not found in management list.")


    def editPermissions(self):
        print("Permissions Updated")
        return True
    
    def exportReport(self, report_obj):
        # 🟡 FIX: Dependency/Association - Admin uses a Report object
        print(f"Exporting report file for {report_obj.type}...")
        return "File_Object"
    
    def configureSettings(self):
        print("System settings configured")
        return True
    
    def issueNotifications(self, message):
        # 🟡 FIX: Dependency/Association - Admin uses/creates a Notification object
        new_notification = Notification(1, message, datetime.now().strftime("%Y-%m-%d"))
        new_notification.sendNotification()
        return new_notification
    
class Teacher(User):
    def __init__(self,userID,name,email,password):
        super().__init__(userID,name,email,password)
        # Aggregation Implementation - Teacher 'has' 0 to * Students (white diamond)
        self.students_taught = [] 
        self.schedule = None

    # Helper method to add students to the teacher's list
    def addStudent(self, student_obj):
        self.students_taught.append(student_obj)
        print(f"Student {student_obj.name} added to Teacher's class list.")

    def createSchedule(self,course,time):
        # 🟡 FIX: Store the created Schedule object (Association/records)
        newSchedule = Schedule(101,course,time)
        newSchedule.createSchedule()
        self.schedule = newSchedule 
        return newSchedule
    
    def markAttendance(self):
        print("Teacher marking class attendance....")
        return True
    
    def generateReport(self, type_of_report="Class Performance"):
        # 🟡 FIX: Dependency/Association - Teacher uses/creates a Report object
        report = Report(1, type_of_report, datetime.now().strftime("%Y-%m-%d"))
        report.generateReport()
        return report 
    
    def flagLowAttendance(self):
        # 🟡 FIX: Use the actual list of Student objects managed by the teacher
        low_attendees = [s.name for s in self.students_taught if len(s.attendance_records) < 2]
        print(f"Flagging students with low attendance: {low_attendees}")
        # Return a list of student objects or names matching the action
        return low_attendees
    

# MAIN FUNCTION TO DEMONSTRATE THE WORKING OF THE CLASSES AND THEIR RELATIONSHIPS

if __name__ == "__main__":
    print("\n" + "="*50)
    print("           UML Class Diagram Implementation Test")
    print("="*50 + "\n")
    
    # --- SETUP USERS ---
    myStudent1 = Student(2, "Mahmood", "mahmood@uni.edu","mahmood1234") 
    myStudent2 = Student(3, "Alia", "alia@uni.edu","alia567")
    myTeacher = Teacher(10, "Mr. Islam Abbasi", "islam@uni.edu", "pass123")
    myAdmin = Admin(4, "Mr. Head Administrator", "admin@uni.edu", "securepass")
    
    
    # --- 1. Inheritance and Composition Test ---
    print("--- 1. Inheritance and Composition (Student) ---")
    myStudent1.login() # Inherited from User
    
    # 🟢 Composition: Student owns Attendance records
    myStudent1.addAttendanceRecord(datetime.now().strftime("%Y-%m-%d"), "Present")
    myStudent1.addAttendanceRecord(datetime.now().strftime("%Y-%m-%d"), "Absent")
    myStudent1.viewDashboard() 
    
    # --- 2. Aggregation (Admin manages Users) Test ---
    print("\n--- 2. Aggregation (Admin manages Users) ---")
    
    # 🟡 FIX: Admin adds various Users to their managed list
    myAdmin.addUser(myTeacher)
    myAdmin.addUser(myStudent1)
    
    print(f"Admin is now managing {len(myAdmin.managed_users)} users.")
    myAdmin.removeUser(myStudent1)
    print(f"Admin is now managing {len(myAdmin.managed_users)} users after removal.")
    
    # --- 3. Aggregation (Teacher has Students) Test ---
    print("\n--- 3. Aggregation (Teacher has Students) ---")
    
    # 🟡 FIX: Teacher adds students to their class list
    myTeacher.addStudent(myStudent1)
    myTeacher.addStudent(myStudent2)

    # 🟡 Teacher generating a Report (Dependency)
    generated_report = myTeacher.generateReport("Term End Class Report")
    
    # 🟡 Teacher flagging low attendance (uses the Aggregated Student list)
    myStudent2.addAttendanceRecord(datetime.now().strftime("%Y-%m-%d"), "Present") # Alia has only 1 record
    low_attendees = myTeacher.flagLowAttendance() # Alia should be flagged as < 2
    
    # --- 4. Associations/Dependencies Test ---
    print("\n--- 4. Associations/Dependencies ---")
    
    # 🟡 Teacher creating and recording a Schedule (Association/records)
    mySchedule = myTeacher.createSchedule("Software Construction", "10:00 AM")
    
    # 🟡 Admin exporting a Report (Dependency)
    myAdmin.exportReport(generated_report)