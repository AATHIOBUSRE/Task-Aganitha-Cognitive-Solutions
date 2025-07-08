from typing import List, Dict
import xml.etree.ElementTree as ET

def extract_paper_data(xml_data: str, debug: bool = False) -> List[Dict]:
    root = ET.fromstring(xml_data)
    results = []

    for article in root.findall(".//PubmedArticle"):
        try:
            pmid = article.findtext(".//PMID")
            title = article.findtext(".//ArticleTitle")
            pub_date = article.findtext(".//PubDate/Year") or "Unknown"
            authors = article.findall(".//Author")
            non_academic_authors = []
            company_affiliations = []
            corresponding_email = None

            for author in authors:
                affil = author.findtext(".//AffiliationInfo/Affiliation")
                if affil:
                    affil_lower = affil.lower()
                    if not any(kw in affil_lower for kw in ["university", "college", "institute", "hospital", "school"]):
                        non_academic_authors.append(author.findtext("LastName") or "Unknown")
                    if any(kw in affil_lower for kw in ["pharma", "biotech", "therapeutics", "inc", "ltd", "gmbh"]):
                        company_affiliations.append(affil)
                if "email" in (affil_lower if affil else "") and not corresponding_email:
                    corresponding_email = affil.split()[-1]  # crude heuristic

            results.append({
                "PubmedID": pmid,
                "Title": title,
                "Publication Date": pub_date,
                "Non-academic Author(s)": "; ".join(non_academic_authors),
                "Company Affiliation(s)": "; ".join(company_affiliations),
                "Corresponding Author Email": corresponding_email or "N/A"
            })
        except Exception as e:
            if debug:
                print(f"Error parsing article: {e}")
    return results
