# Library Management System CLI

## Install

```bash
pip install -r requirements.txt
```

## Run

Start the interactive menu:

```bash
python library-main.py menu
```
From the menu choose between the seven options

Or run one command at a time:

```bash
python library-main.py books
python library-main.py members
python library-main.py loans
python library-main.py add-member
python library-main.py add-book
python library-main.py add-loan
python library-main.py --help
```

## Test

```bash
pytest
```
