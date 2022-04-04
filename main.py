# Local imports
import random 
import _keys

# Non-local imports
import nexmo

# Instantiate Nexmo client
nexmo_client = nexmo.Client(
    key = _keys.nexmo_api_key,
    secret = _keys.nexmo_api_secret
)
sms = nexmo.Sms(client = nexmo_client)

def alert_assignment(person: str, assigned: str):
    """Alerts a person who they were assigned to."""
    person = person.title()
    sms.send_message(
        {
            "from": _keys.nexmo_sender,
            "to": _keys.people[person],
            "text": f"{person}, you have been assigned to {assigned}."
        }
    )

def main():
    """Main execution function."""
    already_assigned = []
    for person in _keys.people:
        # Local list of people
        people = list(_keys.people.keys())

        # Assign person to another person
        people.remove(person)
        assigned = random.choice(people)
        # Duplicity check
        while assigned in already_assigned:
            assigned = random.choice(people)
        # Store the assignment for future iterations
        already_assigned.append(assigned)

        # Alert the person who they were assigned to
        alert_assignment(
            person = person,
            assigned = assigned
        )

if __name__ == "__main__":
    main()