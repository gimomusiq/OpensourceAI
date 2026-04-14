# Contributing to OpenSource AI Model Zoo

Thank you for your interest in contributing! We welcome pull requests to add, update, or improve the list of open-source AI model repositories and project tools.

## How to Contribute

### 1. Add a New Model Repository
- Add the GitHub URL of the model to `ai_model_repos.txt` (one per line, in the appropriate section if categorized).
- Run `python3 check_repo_links.py` to ensure the link is available.
- (Optional) Run `python3 fetch_repo_metadata.py` to update metadata.

### 2. Update or Remove a Model Repository
- Edit or remove the relevant line in `ai_model_repos.txt`.
- Run the link checker to verify changes.

### 3. Improve Project Tools or Documentation
- Suggest improvements or bug fixes for the scripts or documentation.

## Pull Request Guidelines
- Fork the repository and create your branch from `main`.
- Make your changes and commit them with clear messages.
- Ensure all links in `ai_model_repos.txt` are working (use the link checker script).
- Open a pull request describing your changes and why they are needed.

## Code of Conduct
Please be respectful and constructive in all interactions. See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) for details.

## Questions or Suggestions?
Open an issue or start a discussion!
