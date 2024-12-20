from scholarly import scholarly

def fetch_publications(scholar_id):
    author = scholarly.search_author_id(scholar_id)
    scholarly.fill(author)
    publications = []
    for pub in author['publications']:
        pub_details = scholarly.fill(pub)
        title = pub_details.get('bib', {}).get('title', 'Unknown Title')
        year = pub_details.get('bib', {}).get('pub_year', 'Unknown Year')
        authors = pub_details.get('bib', {}).get('author', 'Unknown Authors')
        publications.append(f"- **{title}** ({year}) - {authors}")
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
