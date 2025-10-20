# Tag Management System

A simple Python application for creating and managing tagged objects with user input.

## Overview

This repository contains a basic implementation of a tagging system that allows users to:
- Specify the number of tags to add (between 1-5)
- Interactively enter key-value pairs for each tag
- Create tagged objects with the provided metadata

## Features

- **Interactive Input**: User-friendly prompts for entering tag information
- **Input Validation**: Ensures the number of tags is within acceptable range
- **Tag Storage**: Efficient dictionary-based storage of tag key-value pairs
- **Type Hints**: Full type annotation support for better code clarity

## Usage

Run the main script:

```bash
python main.py
```

Follow the prompts to:
1. Enter the number of tags you want to add (1-5)
2. Provide a key for each tag
3. Provide a corresponding value for each key

The program will create a tagged object and display all tags.

## Example

```
Number of tags (1-5): 3
Key #0: environment
Value: production
Key #1: version
Value: 1.0.0
Key #2: owner
Value: team-alpha
{'environment': 'production', 'version': '1.0.0', 'owner': 'team-alpha'}
```

## Requirements

- Python 3.8+

## Note

This is a demonstration/educational project. Please review the code carefully before using in production environments.