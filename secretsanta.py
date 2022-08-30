# External imports
import nexmo

# Local imports
import random 


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


def alert_assignment(person: str, assigned: str, phone: str):
    """
    Alerts a person who they were assigned to.
    Nexmo instantiation happens in here because there is no performance bottleneck
    whatsoever, and it makes pytests much more convenient.
    """
    sms, sender = create_sms_object()

    person = person.title()
    sms.send_message(
        {
            "from": sender,
            "to": phone,
            "text": f"{person}, you have been assigned to {assigned}."
        }
    )


def assign(people: list[dict], alert: bool = True) -> dict[str, str]:
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
            phone = person["Phone"]
        )

    return assignments
