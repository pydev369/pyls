# pyls
A Python utility that mimics the `ls` command for a JSON-defined directory structure.

## Features

- List directory contents with optional detailed view (`-l`)
- Include hidden files (`-A`)
- Reverse order while sorting (`-r`)
- Sort by time modified (`-t`)
- Filter by file or directory (`--filter`)
- Navigate within the directory structure
- Show human-readable sizes (`-h`)
- Provide a helpful message (`--help`)


## Installation

### Requirements

- Python 3.7+
- `pip`

### Steps

1. Clone the repository:

    ```bash
    git clone https://github.com/pydev369/pyls.git
    cd pyls
    ```

2. Install the package:

    ```bash
    pip install .
    ```

## Usage

    ```bash
    pyls [options] [path]
    ```

## Project Structure

pyls/
│
├── pyls.py          # Main script file
├── structure.json   # JSON file representing directory structure
├── tests/
│   └── test_pyls.py # Test file
└── pyproject.toml   # Project metadata
