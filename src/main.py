import sys
from pathlib import Path
from rich.console import Console

#  find src
sys.path.append(str(Path(__file__).parent.parent))

from src.utils import interface, generator
from src.config import templates

console = Console()

def main():
    """
    Entry point for the SeedCLI Architect.
    """
    interface.display_welcome()

    action = interface.get_action_choice()

    if action == "Exit":
        console.print("[bold yellow]Goodbye![/bold yellow]")
        sys.exit(0)

    elif action == "Clone Repository":
        repo_url = interface.get_repo_url()
        project_name = interface.get_project_name()
        
        if not repo_url or not project_name:
            console.print("[bold red]Operation cancelled.[/bold red]")
            return

        target_dir = Path.cwd() / project_name
        generator.clone_repository(repo_url, target_dir)

    elif action == "Create New Project":
        project_type = interface.get_project_type(list(templates.PROJECT_TEMPLATES.keys()))
        project_name = interface.get_project_name()

        if not project_type or not project_name:
             console.print("[bold red]Operation cancelled.[/bold red]")
             return

        target_dir = Path.cwd() / project_name
        
        # check if directory already exists
        if target_dir.exists() and any(target_dir.iterdir()):
             console.print(f"[bold yellow]Warning: Directory {target_dir} already exists and is not empty.[/bold yellow]")
             if not interface.ask_to_continue():
                 console.print("[bold red]Aborted.[/bold red]")
                 return

        structure = templates.PROJECT_TEMPLATES.get(project_type, [])
        generator.create_structure(target_dir, structure, project_name)

if __name__ == "__main__":
    main()
