import argparse
from get_papers.api import search_pubmed, fetch_pubmed_details
from get_papers.parser import extract_paper_data
from get_papers.exporter import export_results

def main():
    parser = argparse.ArgumentParser(description="Fetch PubMed papers with pharma/biotech affiliations.")
    parser.add_argument("query", type=str, help="PubMed search query")
    parser.add_argument("-f", "--file", type=str, help="Filename to save CSV results")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug output")
    args = parser.parse_args()

    ids = search_pubmed(args.query, debug=args.debug)
    xml = fetch_pubmed_details(ids, debug=args.debug)
    parsed = extract_paper_data(xml, debug=args.debug)
    export_results(parsed, filename=args.file)

if __name__ == "__main__":
    main()
