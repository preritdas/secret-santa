# External imports
import nexmo

# Local imports
import random 

# Project
import messaging


def create_sms_object() -> tuple[nexmo.Sms, str]:
    """
    Returns a tuple of Sms object and sender.
    """
    import _keys 

    nexmo_client = nexmo.Client(
        key = _keys.nexmo_api_key,
        secret = _keys.nexmo_api_secret
    )
    return nexmo.Sms(client = nexmo_client), _keys.nexmo_sender


def alert_assignment(person: str, assigned: str, email: str) -> None:
    """
    Alerts a person who they were assigned to.
    Nexmo instantiation happens in here because there is no performance bottleneck
    whatsoever, and it makes pytests much more convenient.
    """
    person = person.title()

    return messaging.send_email(
        email, 
        person, 
        "Your Secret Santa Assignment", 
        f"{person}, you have been assigned to {assigned}."
    )


def old_assign(people: list[dict], alert: bool = True) -> dict[str, str]:
    """Main execution function."""
    already_assigned = []
    assignments = {}
    for person in people:
        local_people = [person["Name"] for person in people]

        # Assign person to another person
        local_people.remove(person["Name"])
        assigned = random.choice(local_people)

        # Duplicate check
        while assigned in already_assigned:
            assigned = random.choice(local_people)

        # Store the assignment for return
        assignments[person["Name"]] = assigned

        # Store the assignment for future iterations
        already_assigned.append(assigned)

        # Alert the person who they were assigned to
        if not alert: continue
        alert_assignment(
            person = person["Name"],
            assigned = assigned,
            email = person["Email"]
        )

    return assignments


def assign(people: list[dict], alert: bool = True) -> dict[str, str]:
    """Re-implemented."""
    assignments = random.sample(people, len(people))

    return_sequence = {
        person["Name"]: assigned["Name"] for person, assigned in zip(people, assignments)
    }

    if not alert:
        return return_sequence

    for person, assigned in zip(people, assignments):
        alert_assignment(
            person = person["Name"],
            assigned = assigned["Name"],
            email = person["Email"]
        )

    return return_sequence
