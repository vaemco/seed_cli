<div align="center">

<pre>
 ________  _______   _______   ________          ________  ___       ___     
|\   ____\|\  ___ \ |\  ___ \ |\   ___ \        |\   ____\|\  \     |\  \    
\ \  \___|\ \   __/|\ \   __/|\ \  \_|\ \       \ \  \___|\ \  \    \ \  \   
 \ \_____  \ \  \_|/_\ \  \_|/_\ \  \ \\ \       \ \  \    \ \  \    \ \  \  
  \|____|\  \ \  \_|\ \ \  \_|\ \ \  \_\\ \       \ \  \____\ \  \____\ \  \ 
    ____\_\  \ \_______\ \_______\ \_______\       \ \_______\ \_______\ \__\
   |\_________\|_______|\|_______|\|_______|        \|_______|\|_______|\|__|
   \|_________|                                                              
</pre>

# SeedCLI Architect

**Your intelligent project bootstrapper.**

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

</div>

**SeedCLI Architect** allows you to set up professional project structures in seconds. Whether Data Science, Machine Learning, Web Development or Automation - start with Best Practices.

---

## Features

- **Interactive Menus**: Navigate with arrow keys.
- **Visual Feedback**: Beautiful terminal output with progress bars and colors.
- **Smart Templates**:
  - **Data Science**: `data/raw`, `notebooks`, `src/features`
  - **Machine Learning**: `models`, `metrics`, `training_logs`
  - **Web (Bun)**: `public`, `src/components`, `src/pages`
  - **FastAPI**: `app/api`, `app/services`, `app/core`
  - **Automation**: `config`, `logs`, `utils`

---

## Prerequisites

You need **Mamba** or **Conda** to manage the environment easily.

```bash
# 1. Clone repositories
git clone https://github.com/vaemco/seed_cli.git
cd seed_cli

# 2. Create Environment (fast & clean)
mamba env create -f environment.yml

# Check if it was created
mamba env list
```

---

## Global Workflow (Recommended)

### Windows (PowerShell)

To use `seed` from **anywhere** in your terminal, add this alias to your PowerShell profile.

1.  Open your profile:

    ```powershell
    code $PROFILE
    ```

2.  Add this function:

    ```powershell
    function seed {
        # This runs the CLI inside the isolated environment automatically!
        mamba run -n seed_cli python "<YOUR-PATH-TO-REPO>\src\main.py"
    }
    ```

3.  Reload:
    ```powershell
    . $PROFILE
    ```

### macOS / Linux (Bash & Zsh)

1.  Open your config file:

    ```bash
    # For Zsh (macOS default)
    nano ~/.zshrc
    # OR for Bash
    nano ~/.bashrc
    ```

2.  Add this alias:

    ```bash
    alias seed='mamba run -n seed_cli python "/path/to/repo/src/main.py"'
    ```

    _(Replace `/path/to/repo` with the actual path)_

3.  Reload:
    ```bash
    source ~/.zshrc  # or ~/.bashrc
    ```

## Usage

Now you can just type `seed` in any folder!

```bash
cd my-new-project
seed
```

---

## Manual Usage

If you don't want an alias, you can run it manually:

```bash
mamba activate seed_cli
python src/main.py
```

---

## Project Structure

The tool promotes a modular and clean architecture:

- `src/`: Source code modules.
- `utils/`: Helper functions.
- `config/`: Configuration files.

---

## License

MIT License
