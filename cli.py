"""
Create the CLI.
"""
# External imports
import typer
from rich.console import Console; console = Console()

# Project modules
import database
import secretsanta


app = typer.Typer(no_args_is_help=True, add_completion=False)


@app.command()
def addperson(
    name: str = typer.Argument(
        ...,
        help = "Name of the person you're adding."
    ),
    phone: int = typer.Argument(
        ...,
        help = "Phone number for assignment alerts."
    )
):
    """
    Adds a new person to the santa registry.
    """
    name = name.title()
    phone = str(phone)

    res = database.add_person(name, phone)
    if not res:
        console.print(
            f"[green]{name}[/] with phone number [green]{phone}[/] is already in the "
            "database."
        )
        return


@app.command()
def listpeople():
    """
    List all people.
    """
    people = database.read_people()
    console.print_json(data=people)


@app.command()
def resetpeople():
    """
    Resets the database of people.
    """
    database.reset_people()


@app.command()
def assign():
    """
    Assign and alert.
    """
    if len(people := database.read_people()) == 0:
        console.print("You must add people with the [blue]add[/] command.")
        return

    console.print("Running assignments with the following people.")
    console.print_json(data=people)

    with console.status("Running assignments."):
        secretsanta.assign(people)

    console.log("Assignments made.")
