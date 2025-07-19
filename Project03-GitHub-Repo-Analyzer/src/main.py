from github_api import get_repo_stats
from visualizer import plot_repo_stats

def main():
    print("🔍 GitHub Repository Analyzer 🔍")
    owner = input("Enter GitHub username or organization: ")
    repo = input("Enter repository name: ")

    # Fetch and plot repo stats (like stars, forks, etc.)
    stats = get_repo_stats(owner, repo)
    if stats:
        print("\n📊 Repository Stats:")
        for key, value in stats.items():
            print(f"{key}: {value}")
        
        contributors = stats.get("Contributors", 0)
        commits = stats.get("Commits", 0)
        plot_repo_stats(stats, repo, contributors, commits)
    else:
        print("❌ Failed to fetch repository statistics.")

if __name__ == "__main__":
    main()



