import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

def plot_repo_stats(stats, repo_name, contributors, commits, tk_frame=None):
    print(f"Stars: {stats['Stars']}")
    print(f"Forks: {stats['Forks']}")
    print(f"Watchers: {stats['Watchers']}")
    print(f"Open Issues: {stats['Open Issues']}")
    print(f"Contributors: {contributors}")
    print(f"Commits: {commits}")

    labels = ["Stars", "Forks", "Watchers", "Open Issues", "Contributors", "Commits"]
    values = [stats["Stars"], stats["Forks"], stats["Watchers"],
              stats["Open Issues"], contributors, commits]

    fig, ax = plt.subplots(figsize=(8, 5))
    bars = ax.bar(labels, values, color="skyblue")
    ax.set_title(f"📊 Repository Stats: {repo_name}")
    ax.set_ylabel("Count")
    ax.tick_params(axis='x', rotation=45)

    # Add value labels
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2.0, yval + 1, int(yval),
                ha='center', va='bottom', fontsize=9)

    fig.tight_layout()

    if tk_frame is not None:
        # Embed into the Tkinter GUI
        canvas = FigureCanvasTkAgg(fig, master=tk_frame)
        canvas.draw()
        canvas.get_tk_widget().pack()
    else:
        # Fall back to showing in a separate window
        plt.show()




