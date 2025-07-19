import tkinter as tk
from tkinter import messagebox
from github_api import get_repo_stats
from visualizer import plot_repo_stats

def analyze_repo():
    user_input = entry.get().strip()
    if not user_input:
        messagebox.showwarning("Input Error", "Please enter a GitHub repository (URL or owner/repo format).")
        return

    try:
        if "github.com" in user_input:
            # Handle full URL
            parts = user_input.split('/')
            if len(parts) < 5:
                raise ValueError("Invalid GitHub URL. Format: https://github.com/owner/repo")
            owner = parts[-2]
            repo = parts[-1]
        else:
            # Handle owner/repo format
            if '/' not in user_input:
                raise ValueError("Invalid format. Use: owner/repo or full GitHub URL.")
            owner, repo = user_input.split('/', 1)

        # Call API
        stats = get_repo_stats(owner, repo)
        if not stats or not isinstance(stats, dict):
            raise ValueError("Failed to fetch repository statistics. Check if repo exists or API limit exceeded.")

        contributors = stats.get("Contributors", 0)
        commits = stats.get("Commits", 0)

        plot_repo_stats(stats, repo, contributors, commits, root)

    except Exception as e:
        messagebox.showerror("Error", str(e))

# --- UI Setup ---
root = tk.Tk()
root.title("GitHub Repo Analyzer")
root.geometry("550x220")

label = tk.Label(root, text="Enter GitHub Repo (e.g., numpy/numpy or full URL):", font=("Arial", 11))
label.pack(pady=10)

entry = tk.Entry(root, width=55)
entry.pack()

analyze_btn = tk.Button(root, text="Analyze", command=analyze_repo, bg="blue", fg="white")
analyze_btn.pack(pady=20)

root.mainloop()

