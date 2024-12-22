import re
from scholarly import scholarly

# Map journal names to their respective icons (add more as needed)
JOURNAL_ICON_MAP = {
    "Environmental Science & Technology": "https://pubs.acs.org/cms/10.1021/esthag.2024.58.issue-50/asset/193d3a45-b919-d3a4-6b91-3d3a456b9193/esthag.2024.58.issue-50.largecover.jpg",
    "Journal of Hydrology": "https://ars.els-cdn.com/content/image/X00221694.jpg",
    "Science": "https://www.science.org/pb-assets/images/styleguide/logo-1672180580750.svg",
    "AGU Fall Meeting Abstracts 2022": "https://www.arm.gov/uploads/AGU-400x400-1.png"
    # Add more mappings here
}

def extract_journal_from_citation(citation):
    """
    Extracts the journal name from the citation string.
    Assumes the journal name is the first part of the citation string before the first number or volume indicator.
    """
    if not citation:
        return "Unknown Journal"
    
    # Match everything before the first number (assumes journal names do not contain numbers)
    match = re.match(r"^[^\d]+", citation)
    if match:
        return match.group(0).strip()
    return "Unknown Journal"

def get_journal_icon(journal_name):
    """
    Returns the icon URL for the journal name. If not found, returns a default icon.
    """
    return JOURNAL_ICON_MAP.get(journal_name, "https://example.com/icons/default.png")

def format_publication_block(publication):
    # Extract details
    title = publication.get('bib', {}).get('title', 'Unknown Title')
    citation = publication.get('bib', {}).get('citation', None)
    journal = extract_journal_from_citation(citation)
    journal_icon = get_journal_icon(journal)

    # Get URL from the scholarly search
    url = publication.get('url_scholar', None)
    if not url:
        # If no URL is available, use the Google Scholar search URL for the title
        url = f"https://scholar.google.com/scholar?q={title.replace(' ', '+')}"

    # Format as a clickable card with an icon
    publication_block = f"""
<div style="display: flex; align-items: center; margin-bottom: 15px;">
  <img src="{journal_icon}" alt="{journal}" style="width: 30px; height: 30px; margin-right: 10px; border-radius: 50%;"/>
  <a href="{url}" style="text-decoration: none; color: #333; font-weight: bold; font-size: 16px;">{title}</a>
</div>
"""
    return publication_block

def fetch_publications(scholar_id):
    author = scholarly.search_author_id(scholar_id)
    scholarly.fill(author)
    publications = []
    for pub in author['publications']:
        pub_details = scholarly.fill(pub)
        publication_block = format_publication_block(pub_details)
        publications.append(publication_block)
    return "\n".join(publications)

def update_readme(publications_text):
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
