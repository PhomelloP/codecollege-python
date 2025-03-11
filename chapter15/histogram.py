
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.colors as mcolors

# Sample data for streaming services popularity (number of subscribers in millions)
streaming_data = {
    'Netflix': 200,
    'Amazon Prime': 200,
    'Disney+': 153.6,
    'HBO Max': 77,
    'Apple TV+': 25,
    'Paramount+': 32,
    'Showmax': 1.7,
    'Crunchyroll': 50,
    'YouTube Premium': 125
}

# Define gradient colors for each streaming service
gradients = {
    'Netflix': ('black', 'red'),
    'Amazon Prime': ('yellow', 'blue'),
    'Disney+': ('blue', 'white'),
    'HBO Max': ('purple', 'black'),
    'Apple TV+': ('grey', 'white'),
    'Paramount+': ('black', 'white'),
    'Showmax': ('green', 'blue'),
    'Crunchyroll': ('orange', 'white'),
    'YouTube Premium': ('red', 'white')
}

# Create figure and axis
fig, ax = plt.subplots(figsize=(12, 6))

# Function to create gradient color for each bar
def get_gradient_color(gradient, height):
    cmap = mcolors.LinearSegmentedColormap.from_list("", gradient)
    norm = mcolors.Normalize(vmin=0, vmax=height)
    return cmap(norm(height))

# Create bar chart with gradient colors
bars = []
for idx, (service, value) in enumerate(streaming_data.items()):
    gradient = gradients[service]
    cmap = mcolors.LinearSegmentedColormap.from_list("", gradient)
    for i in range(100):
        color = cmap(i / 100)
        ax.bar(idx, value, width=0.8, color=color, edgecolor='none', bottom=i*value/100)

# Customize the plot
ax.set_title('Streaming Services Popularity')
ax.set_xlabel('Streaming Service')
ax.set_ylabel('Subscribers (Millions)')
ax.set_xticks(np.arange(len(streaming_data)))
ax.set_xticklabels(streaming_data.keys(), rotation=45)

# Add value labels on top of each bar
for idx, (service, value) in enumerate(streaming_data.items()):
    ax.text(idx, value, f'{value}', ha='center', va='bottom')

# Adjust layout to prevent label cutoff
plt.tight_layout()

# Show the plot
plt.show()