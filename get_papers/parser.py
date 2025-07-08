from typing import List, Dict, Any
import xml.etree.ElementTree as ET

def parse_pubmed_xml(xml_data: str, debug: bool = False) -> List[Dict[str, Any]]:
    root = ET.fromstring(xml_data)
    articles = []

    for article in root.findall(".//PubmedArticle"):
        result = {
            "pubmed_id": "",
            "title": "",
            "publication_date": "",
            "non_academic_authors": [],
            "company_affiliations": [],
            "corresponding_email": "",
        }

        result["pubmed_id"] = article.findtext(".//PMID") or ""
        result["title"] = article.findtext(".//ArticleTitle") or ""

        pub_date = article.find(".//PubDate")
        if pub_date is not None:
            y = pub_date.findtext("Year") or ""
            m = pub_date.findtext("Month") or ""
            d = pub_date.findtext("Day") or ""
            result["publication_date"] = "-".join(filter(None, [y, m, d]))

        for author in article.findall(".//Author"):
            affil = author.findtext(".//AffiliationInfo/Affiliation")
            if affil:
                is_company = any(word in affil.lower() for word in ["inc", "pharma", "biotech", "corp", "gmbh", "co."])
                if is_company:
                    name = " ".join(filter(None, [author.findtext("ForeName"), author.findtext("LastName")]))
                    if name:
                        result["non_academic_authors"].append(name)
                        result["company_affiliations"].append(affil)

                    for token in affil.split():
                        if "@" in token:
                            result["corresponding_email"] = token.strip(",.;()")
                            break

        if debug:
            print(result)

        articles.append(result)
    return articles
