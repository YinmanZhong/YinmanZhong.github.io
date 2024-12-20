from scholarly import scholarly
import os

def fetch_publications(scholar_id):
    # Search for the Google Scholar profile
    profile = scholarly.search_author_id(scholar_id)
    scholarly.fill(profile)

    # Fetch recent publications
    publications = profile.get('publications', [])[:5]  # Top 5 recent
    return [(pub['bib']['title'], pub['bib']['pub_year']) for pub in publications]

def update_readme(publications, filepath="README.md"):
    # Format publications for Markdown
    publication_md = "\n".join(
        [f"- **{title}** ({year})" for title, year in publications]
    )
    with open(filepath, "r") as file:
        content = file.readlines()

    # Replace the placeholder section
    start_marker = "<!-- START_PUBLICATIONS -->"
    end_marker = "<!-- END_PUBLICATIONS -->"
    start_index = content.index(start_marker + "\n")
    end_index = content.index(end_marker + "\n")

    # Update publications
    content = content[:start_index + 1] + [publication_md + "\n"] + content[end_index:]
    with open(filepath, "w") as file:
        file.writelines(content)

if __name__ == "__main__":
    # Replace with your Google Scholar ID
    scholar_id = "rR9MUpkAAAAJ"
    publications = fetch_publications(scholar_id)
    update_readme(publications)
