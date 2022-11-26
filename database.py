"""
Interact with the people.json database.
"""
import json
import os


current_dir = os.path.dirname(os.path.realpath(__file__))
db_dir = os.path.join(current_dir, "people.json")

def read_people() -> list[dict]:
    """
    Reads the database and returns a dict.
    """
    with open(db_dir, "r", encoding="utf-8") as db:
        return json.load(db)


def _write_people(db: list[dict]) -> None:
    """
    Writes raw content back to the people.json database.
    """
    with open(db_dir, "w", encoding="utf-8") as f:
        f.write(json.dumps(db, indent=4))


def reset_people() -> None:
    """
    Removes all people from the database.
    """
    with open(db_dir, "w", encoding="utf-8") as f:
        f.write("[]")


def add_person(name: str, email: str) -> bool:
    """
    Returns True if successful, false if a person with that name and email 
    already exists in the people.json database.
    """
    db = read_people()

    assert isinstance(name, str) and isinstance(email, str)
    insert = {"Name": name, "Email": email}

    # Check for duplication
    for person in db:
        if person == insert: return False

    # Write results
    db.append(insert)
    _write_people(db)
    return True
