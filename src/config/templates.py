from typing import Dict, List

PROJECT_TEMPLATES: Dict[str, List[str]] = {
    "Data Science": [
        "data/raw", "data/processed", "notebooks", "reports/figures",
        "src/data", "src/features", "src/models", "src/visualization", "tests"
    ],
    "Machine Learning": [
        "data/raw", "data/models", "src/train", "src/eval", "configs", "metrics", "notebooks", "deployment"
    ],
    "Web (Bun)": [
        "public/assets", "src/components", "src/pages", "src/hooks", "src/utils", "src/styles", "tests"
    ],
    "FastAPI": [
        "app/api/v1", "app/core", "app/models", "app/schemas", "app/services", "app/db", "tests", "migrations"
    ],
    "Bot / Automation": [
        "src/handlers", "src/services", "config", "utils", "logs", "tests"
    ],
    "Streamlit App": [
        "pages", "assets", "utils", "tests"
    ],
    "React (Vite)": [
        "public", "src/assets", "src/components", "src/hooks", "src/contexts"
    ],
    "Local Server (Node)": [
        "src/routes", "src/controllers", "src/middleware", "public"
    ]
}

DEFAULT_FILES: Dict[str, List[str]] = {
    "Data Science": ["requirements.txt", ".env", "main.py"],
    "Machine Learning": ["requirements.txt", "training_config.yaml", "train.py"],
    "Web (Bun)": ["package.json", "tsconfig.json", "src/index.ts"],
    "FastAPI": ["requirements.txt", "app/main.py", ".env.example", "docker-compose.yml"],
    "Bot / Automation": ["requirements.txt", "main.py", "config/settings.yaml"],
    "Streamlit App": ["requirements.txt", "app.py", "README.md"],
    "React (Vite)": ["package.json", "vite.config.js", "index.html", "src/main.jsx", "src/App.jsx"],
    "Local Server (Node)": ["package.json", "server.js", "README.md", ".env"]
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
