import requests
import plotly.express as px

# Make an API call and check the response.
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"
headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")


# Process overall results
response_dict = r.json()
print(f"Complete results: {not response_dict['incomplete_results']}")

 # Process repository information.
repo_dicts = response_dict['items']
repo_links, stars, hover_texts = [], [], []
for repo_dict in repo_dicts:
    # Turn repo names into active links.
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)

    stars.append(repo_dict['stargazers_count'])

    # Build hover texts.
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    hover_text = f"{owner}<br />{description}"
    hover_texts.append(hover_text)

# Make visualization.
title = "Most-Starred Python Projects on GitHub"
labels = {'x': 'Repository', 'y': 'Stars'}
fig = px.bar(x=repo_links, y=stars, title=title, labels=labels,
        hover_name=hover_texts)

fig.update_layout(title_font_size=28, xaxis_title_font_size=20,
        yaxis_title_font_size=20)

fig.update_traces(marker_color='SteelBlue', marker_opacity=0.6)

fig.show()



#API Request:

"""You're making a call to the GitHub API to retrieve repository data for Python projects with over 10,000 stars.

The response is parsed using r.json().

Data Processing:

You extract relevant data like repository names, URLs, star counts, and additional details (owner and description).

Data Visualization:

A bar chart is created with plotly.express (px.bar).

Each bar represents a repository, and you include hover text for additional information about the owner and description.

Styling and Customization:

The chart has been customized with font sizes, colors, and opacity to make it visually appealing.
We can each explain a few sections"""