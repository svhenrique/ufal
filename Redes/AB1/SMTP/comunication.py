KEYS = [
    "email",
    "to_email",
    "subject",
    "body",
]

def comunication(*values):

    if len(values) > len(KEYS):
        raise ValueError("Too many values passed")
    if len(values) != 1 or len(values) != 4:
        raise ValueError("Only 1 or 4 values accepted")

    json = dict()
    for value in range(len(values)):
        json[KEYS[value]] = values[value]
    return json




