import argparse
from get_papers.api import search_pubmed, fetch_pubmed_details
from get_papers.parser import parse_pubmed_xml
from get_papers.writer import save_to_csv

def main():
    parser = argparse.ArgumentParser(description="Fetch papers from PubMed.")
    parser.add_argument("query", type=str, help="Search query for PubMed")
    parser.add_argument("-f", "--file", type=str, help="CSV file to save results")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug output")
    args = parser.parse_args()

    ids = search_pubmed(args.query, debug=args.debug)
    xml = fetch_pubmed_details(ids, debug=args.debug)
    parsed = parse_pubmed_xml(xml, debug=args.debug)

    if args.file:
        save_to_csv(parsed, args.file)
        print(f"Results saved to {args.file}")
    else:
        for paper in parsed:
            print(paper)

if __name__ == "__main__":
    main()
