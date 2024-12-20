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
        publications.append(f"{title} ({year}) - {authors}")
    return publications

if __name__ == "__main__":
    # Replace with your Google Scholar ID
    scholar_id = "rR9MUpkAAAAJ"
    publications = fetch_publications(scholar_id)
    with open("README.md", "w") as f:
        f.write("\n".join(publications))
