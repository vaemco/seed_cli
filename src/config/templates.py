from typing import Dict, List

PROJECT_TEMPLATES: Dict[str, List[str]] = {
    "Data Science": [
        "data/raw",
        "data/processed",
        "notebooks",
        "reports/figures",
        "src/data",
        "src/features",
        "src/models",
        "src/visualization",
    ],
    "Machine Learning": [
        "data",
        "models",
        "src",
        "metrics",
        "notebooks",
    ],
    "Web (Bun)": [
        "public",
        "src/components",
        "src/pages",
        "src/utils",
        "tests",
    ],
    "FastAPI": [
        "app/api/endpoints",
        "app/api/middleware",
        "app/core",
        "app/models",
        "app/schemas",
        "app/services",
        "tests",
    ],
    "Bot / Automation": [
        "src",
        "config",
        "utils",
        "logs",
    ]
}

README_CONTENT = """# {project_name}

## Description
*Write a short summary of the project here. What does it do? Who is it for?*

## Installation

```bash
# Clone the repository
git clone <your-repo-url>

# Install dependencies
pip install -r requirements.txt
# or
npm install
```

## Usage

```bash
# Run the application
python src/main.py
# or
npm start
```

## Project Structure

A brief overview of the project's organization.

## License
[Choose a license]
"""

GITIGNORE_CONTENT = """# General
.DS_Store
.env
.vscode/
.idea/

# Python
__pycache__/
*.py[cod]
*$py.class
venv/
env/
.venv/
dist/
build/
*.egg-info/
*.log

# Node / Web
node_modules/
dist/
.parcel-cache/
npm-debug.log
yarn-error.log
"""
