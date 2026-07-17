import re

resume = """
Name: Pranitha Reddy

Email: pranitha.reddy@gmail.com

Phone: +91 9876543210

Skills: Python, Java, SQL, Machine Learning, NLP

Experience: 3 years
"""

print("=" * 60)
print("RESUME INFORMATION EXTRACTION")
print("=" * 60)

name = re.search(r"Name:\s*(.*)", resume)
if name:
    name = name.group(1)
else:
    name = "Not Found"

emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", resume)

phones = re.findall(r"(?:\+91[\s-]?)?[6-9]\d{9}", resume)

skill_list = ["Python", "Java", "SQL", "Machine Learning", "NLP"]

skills_found = []

for skill in skill_list:
    if re.search(skill, resume, re.IGNORECASE):
        skills_found.append(skill)

experience = re.search(r"(\d+)\s+years?", resume, re.IGNORECASE)

if experience:
    years = int(experience.group(1))
else:
    years = 0

print("\nCandidate Profile Summary")
print("-" * 40)
print("Name       :", name)
print("Email      :", ", ".join(emails))
print("Phone      :", ", ".join(phones))
print("Skills     :", ", ".join(skills_found))
print("Experience :", years, "Years")

print("\nEligibility Status")
print("-" * 40)

if years >= 2 and "Python" in skills_found:
    print(name, "is ELIGIBLE for shortlisting.")
else:
    print(name, "is NOT ELIGIBLE for shortlisting.")
