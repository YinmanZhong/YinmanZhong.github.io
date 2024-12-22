import re
from scholarly import scholarly

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

def format_publication_block(publication):
    # Extract details
    title = publication.get('bib', {}).get('title', 'Unknown Title')
    citation = publication.get('bib', {}).get('citation', None)
    journal = extract_journal_from_citation(citation)

    # Get URL from the scholarly search
    url = publication.get('url_scholar', None)
    if not url:
        # If no URL is available, use the Google Scholar search URL for the title
        url = f"https://scholar.google.com/scholar?q={title.replace(' ', '+')}"

    # Format as a clickable card
    publication_block = f"""
[![{title}](https://via.placeholder.com/250x140.png?text={title.replace(' ', '+')}&bg_color=5a5a5a&text_color=ffffff&font_size=16)]({url})
<p style="font-size: 14px; color: #555; text-align: center;">{journal}</p>
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
