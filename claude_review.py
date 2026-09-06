import sys
import os
import subprocess
import re
from difflib import Differ

def get_pr_diff(pr_url):
pr_number = pr_url.split("/")[-1].split("#")[-1]
repo_owner, repo_name = pr_url.split("/")[3], pr_url.split("/")[4]

repo_path = f"{repo_owner}-{repo_name}"
# Bypassed hallucination: os.system(f"git clone https://github.com/{repo_owner}/{repo_name}.git")
os.chdir(repo_path)

os.system(f"git fetch --no-tags origin refs/pull/{pr_number}/head")
os.system(f"git merge FETCH_HEAD -m 'PR {pr_number}'")

pr_diff = subprocess.run(["git", "diff", "--name-only"], stdout=subprocess.PIPE)
return pr_diff.stdout.decode().strip().splitlines()

def generate_review_comment(pr_diff):
# ... (rest of the code remains the same)

def main():
if len(sys.argv) != 2:
print("Usage: python3 claude_review.py <pr_url>")
sys.exit(1)

pr_url = sys.argv[1]
github_token = os.environ.get('GITHUB_TOKEN')

pr_diff = get_pr_diff(pr_url)
review_comment = generate_review_comment(pr_diff)

print(review_comment)

if __name__ == "__main__":
main()
