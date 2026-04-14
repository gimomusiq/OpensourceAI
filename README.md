# OpenSource AI Model Zoo

A comprehensive, curated, and regularly verified list of open-source AI model repositories. Includes an automated tool to check the availability of each model link, ensuring only working and up-to-date resources are listed.

## Overview
This repository provides a large, high-quality list of open-source AI model repositories, verified for availability. It includes a Python tool to check the status of each link, making it easy to keep the list current and reliable.

### Files
- `ai_model_repos.txt`: List of popular, working open-source AI model GitHub URLs (one per line)
- `check_repo_links.py`: Python script to check if each repo link is still available

## How to Use Everything

### 1. View and Update the List
- Open `ai_model_repos.txt` to see the current list of AI model repositories.
- To add more models, append their GitHub URLs to the file (one per line).

### 2. Install Requirements
- Make sure you have Python 3 installed.
- Install the required Python package:
  ```bash
  pip install requests
  ```

### 3. Check Repository Link Availability
- Run the script to check if each repository link is still working:
  ```bash
  python3 check_repo_links.py
  ```
- The script will print the status (OK/NOT AVAILABLE) for each repo link in `ai_model_repos.txt`.

### 4. Update and Maintain
- Periodically re-run the script to verify the availability of all links.
- Update `ai_model_repos.txt` as new models are released or old ones become unavailable.

---
