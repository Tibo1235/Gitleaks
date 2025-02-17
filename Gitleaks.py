import requests
import re
import argparse
from rich.console import Console
from rich.table import Table

# Définition des patterns sensibles
SENSITIVE_PATTERNS = {
    "AWS Access Key": r"AKIA[0-9A-Z]{16}",
    "API Key": r"(?i)(api[_-]?key|token)[:=\s\"]{0,2}[0-9a-zA-Z]{16,40}",  # Escape the double quote
    "Password in URL": r"https?:\/\/[^\s:@]+:[^\s:@]+@"
}

console = Console()

def scan_repository(repo_url):
    console.print(f"[bold cyan]Scanning repository:[/bold cyan] {repo_url}")
    api_url = repo_url.replace("github.com", "api.github.com/repos") + "/git/trees/main?recursive=1"
    headers = {"Accept": "application/vnd.github.v3+json"}
    
    response = requests.get(api_url, headers=headers)
    if response.status_code != 200:
        console.print("[bold red]Error fetching repository data.[/bold red]")
        return
    
    repo_data = response.json()
    table = Table(title="Detected Secrets", show_header=True, header_style="bold magenta")
    table.add_column("File", style="cyan")
    table.add_column("Type", style="yellow")
    table.add_column("Line", style="white")
    
    for file in repo_data.get("tree", []):
        if file["type"] == "blob":
            file_url = repo_url + "/raw/main/" + file["path"]
            file_response = requests.get(file_url)
            if file_response.status_code == 200:
                content = file_response.text.split("\n")
                for i, line in enumerate(content, start=1):
                    for pattern_name, pattern in SENSITIVE_PATTERNS.items():
                        if re.search(pattern, line):
                            table.add_row(file["path"], pattern_name, str(i))
    
    console.print(table)

def main():
    parser = argparse.ArgumentParser(description="Scan a GitHub repository for sensitive data leaks.")
    parser.add_argument("repo_url", help="GitHub repository URL")
    args = parser.parse_args()
    
    scan_repository(args.repo_url)

if __name__ == "__main__":
    main()
