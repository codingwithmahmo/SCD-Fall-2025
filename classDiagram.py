from datetime import datetime
from typing import List

# ============================================================
# BASE CLASS: USER
# ============================================================

class User:
    """Base class for all system users."""

    def __init__(self, user_id: int, name: str, email: str, password: str):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password

    def login(self, email: str, password: str) -> bool:
        return self.email == email and self.password == password

    def recover_password(self, email: str) -> bool:
        return self.email == email


# ============================================================
# SUPPORTING CLASSES
# ============================================================

class Attendance:
    """Represents a single attendance record."""

    def __init__(self, attendance_id: int, student_id: int, date: datetime, status: str):
        self.attendance_id = attendance_id
        self.student_id = student_id
        self.date = date
        self.status = status

    def record_attendance(self) -> bool:
        return True


class Notification:
    """Represents a notification message."""

    def __init__(self, notification_id: int, message: str, date_issued: datetime):
        self.notification_id = notification_id
        self.message = message
        self.date_issued = date_issued

    def send_notification(self, user: User) -> bool:
        return True


class Report:
    """Represents a generated report."""

    def __init__(self, report_id: int, report_type: str, generated_date: datetime, content: str):
        self.report_id = report_id
        self.report_type = report_type
        self.generated_date = generated_date
        self.content = content

    def save_report(self) -> bool:
        return True


class Schedule:
    """Represents a class schedule."""

    def __init__(self, schedule_id: int, course_name: str, time_slot: str):
        self.schedule_id = schedule_id
        self.course_name = course_name
        self.time_slot = time_slot

    def save_schedule(self) -> bool:
        return True

# ============================================================
# STUDENT CLASS (COMPOSITION + AGGREGATION)
# ============================================================

class Student(User):
    """Student inherits from User."""

    def __init__(self, user_id: int, name: str, email: str, password: str,
                 roll_number: str, grade: str, section: str):

        super().__init__(user_id, name, email, password)

        self.roll_number = roll_number
        self.grade = grade
        self.section = section

        # ✅ COMPOSITION (◆): Student OWNS Attendance + Report
        self.attendance_records: List[Attendance] = []   # Student ◆→ Attendance
        self.reports: List[Report] = []                  # Student ◆→ Report

        # ✅ AGGREGATION (◇): Student HOLDS Notification references
        self.notifications: List[Notification] = []      # Student ◇→ Notification

    def view_dashboard(self):
        pass

    def mark_attendance(self, present: bool) -> bool:
        # ✅ COMPOSITION (◆): Student CREATES Attendance object
        status = "Present" if present else "Absent"
        new_id = len(self.attendance_records) + 1
        attendance = Attendance(new_id, self.user_id, datetime.now(), status)

        if attendance.record_attendance():
            # ✅ COMPOSITION (◆): Student STORES Attendance object
            self.attendance_records.append(attendance)
            return True
        return False

    def receive_alerts(self) -> List[Notification]:
        # ✅ AGGREGATION (◇): Student RETURNS stored Notification references
        return self.notifications

    def submit_leave_application(self, reason: str, from_date: datetime, to_date: datetime) -> bool:
        return True

    def add_notification(self, notification: Notification):
        # ✅ AGGREGATION (◇): Student ADDS external Notification object
        self.notifications.append(notification)

    def add_report(self, report: Report):
        # ✅ COMPOSITION (◆): Student STORES Report object created by Teacher
        self.reports.append(report)

# ============================================================
# TEACHER CLASS (AGGREGATION + ASSOCIATION)
# ============================================================

class Teacher(User):
    """Teacher inherits from User."""

    def __init__(self, user_id: int, name: str, email: str, password: str,
                 teacher_id: str, subject: str, designation: str):

        super().__init__(user_id, name, email, password)
        self.teacher_id = teacher_id
        self.subject = subject
        self.designation = designation

        # ✅ AGGREGATION (◇): Teacher HOLDS Schedule references
        self.schedules: List[Schedule] = []  # Teacher ◇→ Schedule

    def create_schedule(self, schedule_id: int, course_name: str, time_slot: str) -> Schedule:
        # ✅ AGGREGATION (◇): Teacher CREATES Schedule object
        schedule = Schedule(schedule_id, course_name, time_slot)

        if schedule.save_schedule():
            # ✅ AGGREGATION (◇): Teacher STORES Schedule reference
            self.schedules.append(schedule)

        return schedule

    def mark_attendance(self, student: Student, present: bool) -> bool:
        # ✅ ASSOCIATION (→): Teacher interacts with Attendance but does NOT own it
        status = "Present" if present else "Absent"
        new_id = len(student.attendance_records) + 1
        attendance = Attendance(new_id, student.user_id, datetime.now(), status)

        if attendance.record_attendance():
            # ✅ COMPOSITION (◆): Attendance stored INSIDE Student (Student owns it)
            student.attendance_records.append(attendance)
            return True
        return False

    def generate_report(self, student: Student, report_type: str) -> Report:
        # ✅ ASSOCIATION (→): Teacher CREATES Report but does NOT own it
        report_id = len(student.reports) + 1
        content = f"Report for {student.name} ({student.roll_number})"

        report = Report(report_id, report_type, datetime.now(), content)
        report.save_report()

        # ✅ COMPOSITION (◆): Student OWNS the Report
        student.add_report(report)

        return report

    def flag_low_attendance(self, student: Student, threshold: float) -> bool:
        total = len(student.attendance_records)
        if total == 0:
            return False
        present_count = sum(1 for r in student.attendance_records if r.status == "Present")
        percentage = (present_count / total) * 100
        return percentage < threshold


# ============================================================
# ADMIN CLASS (AGGREGATION)
# ============================================================

class Admin(User):
    """Admin inherits from User."""

    def __init__(self, user_id: int, name: str, email: str, password: str,
                 admin_id: str, role: str):

        super().__init__(user_id, name, email, password)
        self.admin_id = admin_id
        self.role = role

        # ✅ AGGREGATION (◇): Admin HOLDS references to Users
        self.managed_users: List[User] = []  # Admin ◇→ User

    def add_user(self, user: User) -> bool:
        # ✅ AGGREGATION (◇): Admin ADDS external User object
        if any(u.user_id == user.user_id for u in self.managed_users):
            return False
        self.managed_users.append(user)
        return True

    def remove_user(self, user_id: int) -> bool:
        for user in self.managed_users:
            if user.user_id == user_id:
                self.managed_users.remove(user)
                return True
        return False

    def edit_permissions(self, user_id: int, new_role: str) -> bool:
        for user in self.managed_users:
            if isinstance(user, Admin) and user.user_id == user_id:
                user.role = new_role
                return True
        return False

    def export_report(self, report: Report) -> str:
        # ✅ ASSOCIATION (→): Admin interacts with Report but does NOT own it
        return f"/exports/report_{report.report_id}.pdf"

    def configure_settings(self, setting_name: str, value) -> bool:
        return True

    def issue_notifications(self, users: List[User], message: str) -> int:
        # ✅ ASSOCIATION (→): Admin CREATES Notification but does NOT own it
        notification = Notification(1, message, datetime.now())
        sent = 0

        for user in users:
            if notification.send_notification(user):
                sent += 1

                # ✅ AGGREGATION (◇): Student STORES Notification reference
                if isinstance(user, Student):
                    user.add_notification(notification)

        return sent

# ============================================================
# EXAMPLE USAGE
# ============================================================

if __name__ == "__main__":
    admin = Admin(1, "System Admin", "admin@school.com", "admin123", "ADM001", "System Admin")
    teacher = Teacher(2, "Ali Khan", "ali@school.com", "teach123", "T001", "SE", "Lecturer")
    student = Student(3, "Mahmood", "mahmood@student.com", "stud123", "RSE-56067", "5th Sem", "A")

    admin.add_user(teacher)
    admin.add_user(student)

    schedule = teacher.create_schedule(1, "Software Architecture", "Mon 10-12")
    print("Schedule created:", schedule.course_name, schedule.time_slot)

    teacher.mark_attendance(student, True)
    print("Attendance marked for:", student.name)

    report = teacher.generate_report(student, "Attendance")
    print("Report generated:", report.report_type)

    export_path = admin.export_report(report)
    print("Report exported to:", export_path)

    sent = admin.issue_notifications(admin.managed_users, "Midterm schedule uploaded.")
    print("Notifications sent:", sent)
