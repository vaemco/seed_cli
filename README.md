# SeedCLI Architect

```
 ________  _______   _______   ________          ________  ___       ___
|\   ____\|\  ___ \ |\  ___ \ |\   ___ \        |\   ____\|\  \     |\  \
\ \  \___|\ \   __/|\ \   __/|\ \  \_|\ \       \ \  \___|\ \  \    \ \  \
 \ \_____  \ \  \_|/_\ \  \_|/_\ \  \ \\ \       \ \  \    \ \  \    \ \  \
  \|____|\  \ \  \_|\ \ \  \_|\ \ \  \_\\ \       \ \  \____\ \  \____\ \  \
    ____\_\  \ \_______\ \_______\ \_______\       \ \_______\ \_______\ \__\
   |\_________\|_______|\|_______|\|_______|        \|_______|\|_______|\|__|
   \|_________|

```

**SeedCLI Architect** is a powerful command-line interface tool designed to automate the creation of standardized project structures. It helps developers kickstart their projects with best practices in mind, whether it's for Data Science, Machine Learning, Web Development, or Automation.

## Features

- **Interactive Selection**: Uses arrow keys to select project types.
- **Visual Feedback**: Beautiful terminal output with progress bars and colors.
- **Standardized Templates**:
  - **Data Science**: Optimized for data processing and notebooks.
  - **Machine Learning**: Structure for models, training logs, and metrics.
  - **Web**: Optimized for modern stacks (e.g., Bun).
  - **FastAPI**: Clean architecture with separation of concerns.
  - **Bot/Automation**: Ready-to-go structure for scripts and logging.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/vaemco/seed_cli.git
   cd seed_cli
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the CLI tool:

```bash
python src/main.py
```

Follow the on-screen instructions to select your project type and configure your new project.

## Project Structure

The tool promotes a modular and clean architecture:

- `src/`: Source code modules.
- `utils/`: Helper functions.
- `config/`: Configuration files.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.
