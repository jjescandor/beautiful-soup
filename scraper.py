import enum
from bs4 import BeautifulSoup
import requests

"""
Implementation Notes
Module must be named scraper.py
Create function named get_citations_needed_count
takes in a url string and returns an integer.
Create function named get_citations_needed_report
takes in a url string and returns a report string
the string should be formatted with each citation listed in the order found.
"""


def get_info(URL):
    response = requests.get(URL)
    content = BeautifulSoup(response.content, "html.parser")
    p_tags = content.find_all("p")
    paragraph = ""
    for tag in p_tags:
        if "[citation needed]" in tag.text:
            paragraph += tag.text
    return paragraph.split(".")


def get_citations_needed_count(URL):
    lst_paragprah = get_info(URL)
    return len([tag for tag in lst_paragprah if "citation needed" in tag])
    

def get_citations_needed_report(URL):
    citation_txt = "\n*** NEEDED CITATIONS ***\n"
    lst_paragprah = get_info(URL)
    num = 1
    for i, sentence in enumerate(lst_paragprah):
        if "citation" in sentence:
            txt = (lst_paragprah[i-1].replace("[citation needed]", "").strip())
            citation_txt+= f"\n{num}.) {txt}.\n"
            num += 1
    return citation_txt


if __name__ == "__main__":
    URL_ = input("\nEnter a url or press enter to see the needed citations in History of Taiwan Wikipedia article: \n").strip()
    if "en.wikipedia.org" not in URL_:
        print("\n\n*** Invalid wikipedia url ***\n\n")
    else:
        if not URL_:
            URL_ = "https://en.wikipedia.org/wiki/History_of_Taiwan"
        num_cite = get_citations_needed_count(URL_)
        if num_cite:
            print("\nNumber of Citations Needed:", num_cite)
            print(get_citations_needed_report(URL_))
        else:
            print("No citations needed")
