import os
from scholarly import scholarly

# Define the folder where the journal icons are stored
JOURNAL_ICON_FOLDER = "journal_icons"

def format_publication_block(publication, journal_name):
    """Format a publication block with the title and journal icon."""
    title = publication.get('bib', {}).get('title', 'Unknown Title')
    # Construct the local path for the journal icon
    journal_icon_path_png = os.path.join(JOURNAL_ICON_FOLDER, f"{journal_name.replace(' ', '_')}.png")
    journal_icon_path_jpg = os.path.join(JOURNAL_ICON_FOLDER, f"{journal_name.replace(' ', '_')}.jpg")

    if os.path.exists(journal_icon_path_png):
        journal_icon_path = journal_icon_path_png
    elif os.path.exists(journal_icon_path_jpg):
        journal_icon_path = journal_icon_path_jpg
    else:
        journal_icon_path = os.path.join(JOURNAL_ICON_FOLDER, "default.png")


    # Format block with local image path
    publication_block = f"""
<div style="background-color: #f0f0f0; border-radius: 8px; padding: 20px; margin-bottom: 10px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); display: flex; align-items: center;">
  <img src="{journal_icon_path}" alt="{journal_name}" style="height: 50px; margin-right: 15px;">
  <div>
    <a href="{publication.get('url_scholar', '#')}" style="text-decoration: none; color: #333; font-weight: bold; font-size: 16px;">{title}</a>
  </div>
</div>
"""
    return publication_block

def fetch_publications(scholar_id):
    """Fetch publications for a given Google Scholar ID."""
    author = scholarly.search_author_id(scholar_id)
    scholarly.fill(author)
    publications = []
    for pub in author['publications']:
        pub_details = scholarly.fill(pub)
        title = pub_details.get('bib', {}).get('title', 'Unknown Title')
        citation = pub_details.get('bib', {}).get('citation', '')
        journal_name = citation.split()[0] if citation else 'Unknown Journal'

        # Format publication block
        publication_block = format_publication_block(pub_details, journal_name)
        publications.append(publication_block)

    return "\n".join(publications)

def update_readme(publications_text):
    """Update the README file with the generated publication blocks."""
    with open("README.md", "r", encoding="utf-8") as file:
        content = file.read()
    start_marker = "<!-- START: Google Scholar Publications -->"
    end_marker = "<!-- END: Google Scholar Publications -->"
    updated_content = (
        content.split(start_marker)[0]
        + start_marker
        + "\n"
        + publications_text
        + "\n"
        + end_marker
        + content.split(end_marker)[1]
    )
    with open("README.md", "w", encoding="utf-8") as file:
        file.write(updated_content)

if __name__ == "__main__":
    scholar_id = "rR9MUpkAAAAJ"  # Replace with your actual Google Scholar ID
    publications_text = fetch_publications(scholar_id)
    print(publications_text)
    update_readme(publications_text)
