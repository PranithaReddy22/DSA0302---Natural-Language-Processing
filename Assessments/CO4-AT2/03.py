import re

text = """The doctor who reviewed the patient last week
recommends starting medication and scheduling a follow-up
visit in Chennai."""

doctor = re.search(r"The (doctor)", text).group(1)

action = re.findall(r"(recommends|starting|scheduling)", text)

location = re.search(r"in (\w+)", text).group(1)

print("Subject:", doctor)
print("Actions:", action)
print("Location:", location)