# leetcode

<a href="https://leetcode.com/u/miyakoshi-3854/">
    <img src="https://leetcard.jacoblin.cool/miyakoshi-3854" />
</a>

## Overview

Python environment for LeetCode practice.

## Setup

### 1. Install [`mise`](https://mise.jdx.dev/getting-started.html)

### 2. Run

```bash
mise run setup
```

## Usage

### 1. Solve a problem

Edit `main.py` and run:

```bash
mise run p
```

### 2. Save your answer

```bash
mise run sv
```

Enter the problem slug (e.g. `1.two-sum`) when prompted. This will:

- Save to `_result/{problem}/main.py`
- Save as `main_2.py`, `main_3.py`, etc. if the problem was solved before
- Commit automatically with git
- Reset `main.py` to the template

## Directory Structure

```
.
├── main.py                 # Working file
├── .mise.toml              # Dev tool config (mise)
├── .pre-commit-config.yaml # Pre-commit hooks
├── shell/
│   └── solve.sh            # Save script
├── _template/              # Template files
└── _result/                # Saved answers
    └── {problem}/
        └── main.py
```
