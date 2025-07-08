from typing import List
import requests

def search_pubmed(query: str, retmax: int = 100, debug: bool = False) -> List[str]:
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": retmax
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()
    ids = data.get("esearchresult", {}).get("idlist", [])
    if debug:
        print(f"Fetched {len(ids)} IDs.")
    return ids

def fetch_pubmed_details(ids: List[str], debug: bool = False) -> str:
    if not ids:
        return ""
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
    params = {
        "db": "pubmed",
        "id": ",".join(ids),
        "retmode": "xml"
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    if debug:
        print(f"Fetched details for {len(ids)} papers.")
    return response.text
