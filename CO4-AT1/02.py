machines = {
    "M1": "Active",
    "M2": "Active",
    "M3": "Maintenance",
    "M4": "Active",
}
for m, status in machines.items():
    if status == "Active":
        print(m, "-> Producing")
    else:
        print(m, "-> Not Producing")
