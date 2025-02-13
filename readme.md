# CodeWatchDog

**CodeWatchDog** is a GitHub Action that leverages AI to review your pull requests (PRs) automatically. It analyzes code changes and provides insightful comments directly on your PR, helping to improve code quality and catch potential issues early.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Setup and Configuration](#setup-and-configuration)
  - [1. Obtain the GenAI API Key](#1-obtain-the-genai-api-key)
  - [2. Generate GitHub PAT Token](#2-generate-github-pat-token)
  - [3. Set Up GitHub Secrets](#3-set-up-github-secrets)
  - [4. Initialize a Self-Hosted Server](#4-initialize-a-self-hosted-server)
- [Usage](#usage)
- [Troubleshooting](#troubleshooting)
- [Contact](#contact)
- [License](#license)

---

## Overview

CodeWatchDog integrates seamlessly into your GitHub workflow to provide automated, AI-driven PR reviews. By analyzing your code changes, it offers constructive feedback to ensure your code adheres to best practices and standards. The action requires a valid GenAI API key, a GitHub Personal Access Token (PAT), and a self-hosted server to process the reviews.

---

## Features

- **AI-Powered Analysis:** Utilizes advanced AI algorithms to review code changes.
- **Automated Feedback:** Posts detailed review comments directly on your pull requests.
- **Customizable:** Easily configurable with your own API keys and server settings.
- **Secure:** Uses GitHub Secrets to securely manage API keys and tokens.

---

## Requirements

Before you begin, ensure you have the following:

- **GenAI API Key:** Contact the GenAI Gateway team via the [GSD Form](https://gsd.dhl.com/forms/8079) to request access.
- **GitHub PAT Token:** Generate a Personal Access Token from GitHub with the necessary scopes.
- **Self-Hosted Server:** A server environment to run the AI review engine. Follow the setup instructions provided in the server documentation.

---

## Setup and Configuration

### 1. Obtain the GenAI API Key

To access the GenAI APIs:
1. **Request Access:** Fill out the [GSD Form](https://gsd.dhl.com/forms/8079) to contact the GenAI Gateway team.
2. **Receive API Key:** Once approved, you will receive your API key. This key must be stored securely.

> **Note:** The API key should be set as an environment variable named `API_KEY`.

### 2. Generate GitHub PAT Token

Generate a Personal Access Token (PAT) from GitHub to allow CodeWatchDog to interact with the GitHub API:
1. Navigate to your GitHub account settings.
2. Go to **Developer settings** > **Personal access tokens**.
3. Click on **Generate new token**.
4. Select the necessary scopes (e.g., `repo`, `workflow`, etc.).
5. Copy the generated token.

> **Tip:** Name the token clearly (e.g., `CodeWatchDog-PAT`) for easy identification.

### 3. Set Up GitHub Secrets

Store your sensitive tokens securely in your repository's secrets:
1. In your GitHub repository, go to **Settings** > **Secrets and variables** > **Actions**.
2. Click **New repository secret**.
3. Add the following secrets:
   - **`API_KEY`**: Your GenAI API key.
   - **`PAT_TOKEN`**: Your GitHub Personal Access Token.

### 4. Initialize a Self-Hosted Server

The self-hosted server is required to run the AI review engine locally. Follow these steps to set up your server:

1. **Prerequisites:**
   - Ensure you have a supported operating system (Linux, macOS, or Windows).
   - Install Docker or any other required dependencies as per the server documentation.

2. **Clone the Server Repository:**
   ```bash
   git clone https://github.com/your-organization/codewatchdog-server.git
   cd codewatchdog-server
   ```

3. **Configure the Server:**
   - Update configuration files (e.g., `.env`) with the necessary parameters including the `API_KEY` and any other required environment variables.
   - For Docker deployments, ensure your `Dockerfile` and `docker-compose.yml` are configured correctly.

4. **Start the Server:**
   - Using Docker Compose:
     ```bash
     docker-compose up -d
     ```
   - Or run the server directly if not using Docker:
     ```bash
     ./start-server.sh
     ```

5. **Verify Server Operation:**
   - Confirm that the server is running and accessible by visiting the configured endpoint (e.g., `http://localhost:8080`).

> **Important:** Ensure that your server is secure and accessible only to authorized users, as it handles sensitive API requests.

---

## Usage

Once everything is set up, CodeWatchDog will automatically run on each pull request. Here's what happens during a PR review:

1. **PR Trigger:** When a new pull request is opened or updated, the GitHub Action is triggered.
2. **Analysis:** The action sends the code changes to your self-hosted server where the AI engine processes the review.
3. **Feedback:** The AI engine generates review comments which are then posted directly on your pull request by the GitHub Action.

### Example Workflow File

Below is an example snippet of a GitHub Actions workflow (`.github/workflows/codewatchdog.yml`):

```yaml
name: CodeWatchDog PR Review

on:
  pull_request:
    types: [opened, synchronize]

jobs:
  ai-review:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Run CodeWatchDog
        uses: your-organization/codewatchdog@v1
        env:
          API_KEY: ${{ secrets.API_KEY }}
          PAT_TOKEN: ${{ secrets.PAT_TOKEN }}
          SERVER_URL: "http://your-server-address:8080"
```

> **Note:** Replace `"http://your-server-address:8080"` with the actual URL of your self-hosted server.

---

## Troubleshooting

- **Server Connectivity Issues:**  
  - Verify that your self-hosted server is running and accessible.
  - Check firewall rules and network settings.
  
- **Authentication Errors:**  
  - Ensure that `API_KEY` and `PAT_TOKEN` are correctly set in GitHub Secrets.
  - Verify the token scopes and permissions.

- **Action Failures:**  
  - Review the GitHub Actions logs for error messages.
  - Ensure that your workflow file is correctly configured.

For more detailed logs, consider enabling debug logging in your GitHub Actions workflow.

---

## Contact

For any assistance or inquiries, please contact:

**Naresh Vairam V**  
Email: [nareshvairam.v@dhl.com](mailto:nareshvairam.v@dhl.com)

---

## License

This project is licensed under the [MIT License](LICENSE).

---

Happy coding and happy reviewing with CodeWatchDog!
```
