import questionary
from rich.console import Console
from rich.panel import Panel

console = Console()

from rich.align import Align
from rich.text import Text

WELCOME_ASCII = r"""
 ________  _______   _______   ________          ________  ___       ___     
|\   ____\|\  ___ \ |\  ___ \ |\   ___ \        |\   ____\|\  \     |\  \    
\ \  \___|\ \   __/|\ \   __/|\ \  \_|\ \       \ \  \___|\ \  \    \ \  \   
 \ \_____  \ \  \_|/_\ \  \_|/_\ \  \ \\ \       \ \  \    \ \  \    \ \  \  
  \|____|\  \ \  \_|\ \ \  \_|\ \ \  \_\\ \       \ \  \____\ \  \____\ \  \ 
    ____\_\  \ \_______\ \_______\ \_______\       \ \_______\ \_______\ \__\
   |\_________\|_______|\|_______|\|_______|        \|_______|\|_______|\|__|
   \|_________|                                                              
"""

def display_welcome():
    """Displays the welcome banner with centered rainbow ASCII art."""
    lines = WELCOME_ASCII.strip().split("\n")
    colors = ["red", "orange1", "yellow", "green", "blue", "magenta", "violet"]
    
    rainbow_text = Text()
    for i, line in enumerate(lines):
        color = colors[i % len(colors)]
        rainbow_text.append(line + "\n", style=f"bold {color}")
    
    console.print(Panel(Align.center(rainbow_text), border_style="green", title="SeedCLI Architect", subtitle="Your intelligent project bootstrapper"))
    console.print("\n")

def get_action_choice() -> str:
    """Asks the user what they want to do."""
    return questionary.select(
        "What would you like to do?",
        choices=[
            "Create New Project",
            "Clone Repository",
            "Exit"
        ]
    ).ask()

def get_project_type(options: list) -> str:
    """Asks the user for the project template type."""
    return questionary.select(
        "Select the project type:",
        choices=options
    ).ask()

def get_project_name() -> str:
    """Asks for the project name."""
    return questionary.text("Enter project project name (folder will be created):").ask()

def get_repo_url() -> str:
    """Asks for the repository URL."""
    return questionary.text("Enter the GitHub repository URL:").ask()

def ask_to_continue() -> bool:
    """Asks validation to continue if directory is not empty."""
    return questionary.confirm("Do you want to continue?").ask()
