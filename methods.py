# ============================================================
# ✅ COMPOSITION USED IN THIS CODE — EXPLANATION
# ============================================================

# ✅ 1) Composition implement karne ke liye humne jo METHOD use kiya hai:
#    ➤ "Attribute-Based Composition" (also called Containment)
#
#    Yeh tab hota hai jab parent class ke andar:
#       - ek list ya object attribute banaya jata hai
#       - jisme child objects store hote hain
#       - aur parent unka lifecycle control karta hai
#
#    Example from code:
#       self.attendance_records = []
#       self.reports = []
#
#    Yeh dono Student ke andar create hotay hain,
#    isliye Student unka OWNER hota hai (Composition).


# ✅ 2) Composition ke alternative tareeqe:
#
#    ✅ (A) Constructor-Based Composition
#       Parent apne __init__() ke andar child object create kare.
#       Example:
#           self.profile = Profile(self.user_id)



# ✅ 3) Tumhare code mein composition EXACTLY kahan hua hai:
#
#    ✅ Student class:
#       - self.attendance_records = []   (Composition container)
#       - self.reports = []              (Composition container)
#
#       - mark_attendance() method:
#           Attendance object Student create karta hai
#           Student usay apni list mein store karta hai
#
#       - add_report() method:
#           Report object Teacher banata hai
#           Lekin Student usay OWN karta hai (composition)
#
#    Yeh dono relationships UML ke filled diamond (◆) ke bilkul mutabiq hain.





# ============================================================
# ✅ AGGREGATION USED IN THIS CODE — EXPLANATION
# ============================================================

# ✅ 1) Aggregation implement karne ke liye humne jo METHOD use kiya hai:
#    ➤ "Attribute-Based Aggregation" (also called Shared Aggregation)
#
#    Yeh tab hota hai jab parent class ke andar:
#       - ek list ya object attribute banaya jata hai
#       - jisme external (independent) objects store hote hain
#       - parent un objects ka lifecycle control nahi karta
#
#    Example from code:
#       self.notifications = []
#       self.schedules = []
#       self.managed_users = []
#
#    Yeh sab external objects hain jo parent ke bina bhi exist kar sakte hain.
#    Isliye yeh Aggregation (◇) hai, Composition nahi.


# ✅ 2) Aggregation ke alternative tareeqe:
#
#    ✅ (A) Reference-Based Aggregation
#       Parent sirf child object ka reference rakhta hai,
#       child object kahin aur create hota hai.
#
#       Example:
#           self.teacher = teacher_object
#
#       Parent lifecycle child ko affect nahi karta.


#    ✅ (B) Setter-Based Aggregation
#       Parent ek method ke through external object ko accept kare.
#
#       Example:
#           def assign_schedule(self, schedule):
#               self.schedules.append(schedule)
#
#       Child object system mein independently exist karta hai.


#    ✅ (C) Injection-Based Aggregation
#       Child object constructor ke parameter ke through parent ko diya jaye.
#
#       Example:
#           def __init__(self, schedule: Schedule):
#               self.schedule = schedule
#
#       Parent child ko create nahi karta — sirf use karta hai.


# ✅ 3) Tumhare code mein Aggregation EXACTLY kahan hua hai:
#
#    ✅ Student class:
#       - self.notifications = []          (Student ◇→ Notification)
#       - add_notification() method        (external Notification add hoti hai)
#
#    ✅ Teacher class:
#       - self.schedules = []             (Teacher ◇→ Schedule)
#       - create_schedule() method        (Schedule create hoti hai, but independent rehti hai)
#
#    ✅ Admin class:
#       - self.managed_users = []         (Admin ◇→ User)
#       - add_user() method               (external User add hota hai)
#       - issue_notifications()           (Admin sends, Student stores)
#
#    In sab cases mein:
#       - Parent object child ko OWN nahi karta
#       - Child object parent ke bina bhi exist kar sakta hai
#       - Parent sirf reference hold karta hai
#
#    Yeh UML ke hollow diamond (◇) ke bilkul mutabiq hai.
