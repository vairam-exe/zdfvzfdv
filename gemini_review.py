import os
import requests
import re
from pathlib import Path

# Constants
API_URL = ""
API_KEY = ""

def call_ai_api(diff_content):
    """Call the AI API with the Git diff content."""
    payload = {
        "messages": [
            {
                "role": "system",
                "content": "You are a senior code reviewer. Analyze the provided code diff for: code quality, security issues, best practices, and potential bugs. Provide specific feedback with line numbers and suggestions."
            },
            {
                "role": "user",
                "content": diff_content
            }
        ],
        "temperature": 0.7,
        "top_p": 0.95,
        "max_tokens": 1000
    }

    headers = {
        "Content-Type": "application/json",
        "api-key": API_KEY
    }

    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code != 200:
        raise Exception(f"API request failed: {response.status_code} - {response.text}")
    return response.json()

def parse_ai_response(response):
    """Parse the AI response to extract the review content."""
    try:
        return response["choices"][0]["message"]["content"]
    except KeyError:
        raise Exception("Invalid API response format")

def save_review(review_content):
    """Save the review content to a markdown file."""
    with open("review.md", "w") as file:
        file.write(f"## AI Code Review\n\n{review_content}")

def main():
    try:
        # Prepare to analyze each diff file
        diff_dir = Path("diffs")
        review_content = ["## Code Review"]

        for diff_file in diff_dir.glob("*.diff"):
            with open(diff_file, "r") as f:
                diff = f.read()

            # Extract filename from diff header
            filename_match = re.search(r'^diff --git a/(.+?) b/', diff, re.MULTILINE)
            filename = filename_match.group(1) if filename_match else diff_file.stem

            # Call AI API for each diff
            ai_response = call_ai_api(diff)
            review_content.append(f"### 📄 File: {filename}\n\n{parse_ai_response(ai_response)}\n\n---")

        # Save review to file
        save_review("\n".join(review_content))
        print("Review saved to review.md.")

    except Exception as e:
        print(f"Error: {e}")
        exit(1)

if __name__ == "__main__":
    main()
