import sys
import http.client
import urllib.parse
from html.parser import HTMLParser

from httpClient import HttpClient
from parser import ListCounterParser

def main():
    if len(sys.argv) != 2:
        print("No url provided")
        sys.exit(1)

    url = sys.argv[1]
    # url = """https://en.wikipedia.org/wiki/Wikipedia:Wiki_Game""" //Test

    parsed_url = urllib.parse.urlparse(url)

    httpClient = HttpClient(parsed_url.netloc)
    html_content = httpClient.fetch(parsed_url.path)
    
    parser = ListCounterParser()
    parser.feed(html_content)
    print(f"Largest unordered list child count: {len(parser.highest_ul_list)}")

if __name__ == "__main__":
    main()
