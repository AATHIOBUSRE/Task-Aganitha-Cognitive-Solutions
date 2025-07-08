from get_papers.api import search_pubmed, fetch_pubmed_details

def test_search_pubmed_returns_ids():
    query = "covid vaccine"
    ids = search_pubmed(query, retmax=5)
    
    assert isinstance(ids, list), "IDs should be returned as a list"
    assert len(ids) > 0, "Should return at least one PubMed ID"
    assert all(isinstance(i, str) for i in ids), "Each ID should be a string"

def test_fetch_pubmed_details_returns_xml():
    # First, get a few real IDs
    ids = search_pubmed("covid vaccine", retmax=3)
    xml = fetch_pubmed_details(ids)
    
    assert isinstance(xml, str), "Returned data should be a string"
    assert "<PubmedArticle>" in xml, "XML should contain PubmedArticle tag"
