import secretsanta


people = [
    {
        "Name": "Person 1",
        "Phone": "18271928327"
    },
    {
        "Name": "Person 2",
        "Phone": "19283019283"
    },
    {
        "Name": "Person 3",
        "Phone": "19283019283"
    },
    {
        "Name": "Person 4",
        "Phone": "19283019283"
    },
    {
        "Name": "Person 5",
        "Phone": "19283019283"
    },
    {
        "Name": "Person 6",
        "Phone": "19283019283"
    },
]


def test_assignment():
    assignments = secretsanta.assign(people, alert=False)

    # Ensure all keys are unique
    assert len(assignments.keys()) == len(set(assignments.keys()))

    # Ensure all assigned are unique
    assert len(assignments.values()) == len(set(assignments.values()))
   