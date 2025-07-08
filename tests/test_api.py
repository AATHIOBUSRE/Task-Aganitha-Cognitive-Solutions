from get_papers.api import search_pubmed, fetch_pubmed_details
from get_papers.parser import parse_pubmed_xml

def test_search_pubmed():
    ids = search_pubmed("cancer", retmax=2)
    assert isinstance(ids, list)
    assert all(isinstance(i, str) for i in ids)

def test_fetch_and_parse():
    ids = search_pubmed("covid", retmax=1)
    xml = fetch_pubmed_details(ids)
    data = parse_pubmed_xml(xml)
    assert isinstance(data, list)
    assert isinstance(data[0], dict)
    expected_keys = {"pubmed_id", "title", "publication_date", "non_academic_authors", "company_affiliations", "corresponding_email"}
    assert expected_keys.issubset(data[0].keys())
