import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.animation import FuncAnimation


def levenshtein_visualize(s1: str, s2: str):
    m, n = len(s1), len(s2)

    # Initialize distance matrix
    distance_matrix = np.zeros((m + 1, n + 1), dtype=int)

    # Fill in base cases
    for i in range(m + 1):
        distance_matrix[i][0] = i
    for j in range(n + 1):
        distance_matrix[0][j] = j

    # Initialize the plot
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(distance_matrix, annot=True, fmt="d",
                cbar=False, ax=ax, cmap="YlGnBu")

    # Function to update the heatmap at each step
    def update(frame):
        i, j = frame
        if i == 0 or j == 0:
            return  # Base cases already initialized

        # Compute cost
        if s1[i - 1] == s2[j - 1]:
            cost = 0
        else:
            cost = 1

        # Calculate the minimum cost among insertion, deletion, or substitution
        distance_matrix[i][j] = min(
            distance_matrix[i - 1][j] + 1,      # Deletion
            distance_matrix[i][j - 1] + 1,      # Insertion
            distance_matrix[i - 1][j - 1] + cost  # Substitution
        )

        # Clear the previous heatmap
        ax.clear()
        # Re-draw the heatmap with updated values
        sns.heatmap(distance_matrix, annot=True, fmt="d",
                    cbar=False, ax=ax, cmap="YlGnBu")
        ax.set_title(f'Calculating Levenshtein Distance: Step ({i}, {j})')
        ax.set_xlabel('String 2: ' + s2)
        ax.set_ylabel('String 1: ' + s1)

    # Create an animation
    frames = [(i, j) for i in range(m + 1) for j in range(n + 1)]
    ani = FuncAnimation(fig, update, frames=frames, repeat=False)

    plt.show()


# Example usage:
s1 = "computador"
s2 = "ventilador"
levenshtein_visualize(s1, s2)
