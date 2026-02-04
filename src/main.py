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
        
        if not repo_url:
            console.print("[bold red]Operation cancelled.[/bold red]")
            return

        # Clone first, let it infer the name
        target_dir = generator.clone_repository(repo_url)
        
        if target_dir and target_dir.exists():
            # Now ask for scaffolding
            project_type = interface.get_project_type(list(templates.PROJECT_TEMPLATES.keys()))
            if project_type:
                 structure = templates.PROJECT_TEMPLATES.get(project_type, [])
                 files = templates.DEFAULT_FILES.get(project_type, [])
                 # Use the folder name as the project name for README purposes
                 generator.create_structure(target_dir, structure, target_dir.name, files)

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
        files = templates.DEFAULT_FILES.get(project_type, [])
        generator.create_structure(target_dir, structure, project_name, files)

if __name__ == "__main__":
    main()
