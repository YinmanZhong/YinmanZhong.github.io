from scholarly import scholarly

def format_publication_block(publication):
    # Extract details
    title = publication.get('bib', {}).get('title', 'Unknown Title')
    year = publication.get('bib', {}).get('pub_year', 'Unknown Year')
    authors = publication.get('bib', {}).get('author', 'Unknown Authors')

    # Get URL from the scholarly search
    url = publication.get('url_scholar', None)
    if not url:
        # If no URL is available, use the DOI or construct a URL from the title or other fields
        url = f"https://scholar.google.com/scholar?q={title.replace(' ', '+')}"

    print(f"Publication URL: {url}")

    # Format as a block with HTML and Markdown link
    publication_block = f"""
<div style="background-color: #f0f0f0; border-radius: 8px; padding: 20px; margin-bottom: 10px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);">
  <a href="{url}" style="text-decoration: none; color: #333; font-weight: bold; font-size: 16px;">{title}</a>
  <p style="font-size: 14px; color: #555;">{authors} ({year})</p>
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
    scholar_id = "rR9MUpkAAAAJ"
    publications_text = fetch_publications(scholar_id)
    print(publications_text)
    update_readme(publications_text)
