import os
import subprocess
from pathlib import Path
from typing import List
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn
from src.config.templates import README_CONTENT, GITIGNORE_CONTENT

console = Console()

def create_structure(base_path: Path, directories: List[str], project_name: str):
    """
    Creates the project directory structure and basic files.
    
    Args:
        base_path (Path): The root path of the new project.
        directories (List[str]): List of relative paths to create.
        project_name (str): Name of the project for the README.
    """
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    ) as progress:
        task = progress.add_task(description=f"Creating project at {base_path}...", total=len(directories) + 3)
        
        #  base directory
        if not base_path.exists():
            base_path.mkdir(parents=True, exist_ok=True)
        progress.advance(task)

        #  subdirectories
        for dir_path in directories:
            full_path = base_path / dir_path
            full_path.mkdir(parents=True, exist_ok=True)
            (full_path / ".gitkeep").touch()
            progress.advance(task)
            
        #  README.md
        readme_path = base_path / "README.md"
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(README_CONTENT.format(project_name=project_name))
        progress.advance(task)

        #  .gitignore
        gitignore_path = base_path / ".gitignore"
        with open(gitignore_path, "w", encoding="utf-8") as f:
            f.write(GITIGNORE_CONTENT)
        progress.advance(task)

    console.print(f"[bold green]Project structure created successfully at {base_path}[/bold green]")

def clone_repository(repo_url: str, target_dir: Path):
    """
    Clones a git repository.
    
    Args:
        repo_url (str): HTTPS URL of the git repository.
        target_dir (Path): Destination directory.
    """
    console.print(f"[bold blue]Cloning {repo_url}...[/bold blue]")
    try:
        subprocess.run(["git", "clone", repo_url, str(target_dir)], check=True)
        console.print("[bold green]Repository cloned successfully![/bold green]")
    except subprocess.CalledProcessError:
        console.print("[bold red]Failed to clone repository.[/bold red]")
    except FileNotFoundError:
        console.print("[bold red]Git command not found. Is git installed?[/bold red]")
