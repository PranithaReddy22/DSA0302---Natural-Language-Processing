queries = {
    "Q1": ("Activate Roaming", "Activate Roaming"),
    "Q2": ("Deactivate Caller Tune", "Activate Caller Tune"),
    "Q3": ("Query Data Balance", "Query Data Balance"),
    "Q4": ("Activate 5G Service", "Activate 5G Service")
}
for q, (actual, predicted) in queries.items():
    if actual == predicted:
        print(q, "Correct")
    else:
        print(q, "Incorrect:", actual, "!=", predicted)