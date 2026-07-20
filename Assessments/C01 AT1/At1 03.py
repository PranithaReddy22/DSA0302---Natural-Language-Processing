import re

print("=" * 60)
print("STUDENT REGISTRATION VALIDATION SYSTEM")
print("=" * 60)

# Sample Student Details
register_no = "23AIML101"
email = "student@saveetha.com"
course_code = "CS301"
semester = "Semester 5"
mobile = "9876543210"

# Validation Flags
reg_valid = False
email_valid = False
course_valid = False
sem_valid = False
mobile_valid = False

# 1. Validate Register Number
if re.fullmatch(r"\d{2}[A-Z]{4}\d{3}", register_no):
    print("Register Number : Valid")
    reg_valid = True
else:
    print("Register Number : Invalid")

# 2. Validate Institutional Email
if re.fullmatch(r"[a-zA-Z0-9._%+-]+@saveetha\.com", email):
    print("Email           : Valid")
    email_valid = True
else:
    print("Email           : Invalid")

# 3. Validate Course Code
if re.fullmatch(r"[A-Z]{2}\d{3}", course_code):
    print("Course Code     : Valid")
    course_valid = True
else:
    print("Course Code     : Invalid")

# 4. Validate Semester
if re.fullmatch(r"Semester\s[1-8]", semester):
    print("Semester        : Valid")
    sem_valid = True
else:
    print("Semester        : Invalid")

# 5. Validate Mobile Number
if re.fullmatch(r"[6-9]\d{9}", mobile):
    print("Mobile Number   : Valid")
    mobile_valid = True
else:
    print("Mobile Number   : Invalid")

# Final Registration Report
print("\n" + "=" * 60)
print("REGISTRATION STATUS REPORT")
print("=" * 60)

if reg_valid and email_valid and course_valid and sem_valid and mobile_valid:
    print("Registration Successful")
else:
    print("Registration Failed")
