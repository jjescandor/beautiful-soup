import pytest
from scraper import get_citations_needed_count, get_citations_needed_report

def test_get_citations_needed_count_exists():
    assert get_citations_needed_count

def test_get_citations_needed_report_exists():
    assert get_citations_needed_report

def test_nanjiang_article():
    URL = "https://en.wikipedia.org/wiki/Nanjing_Massacre"
    assert get_citations_needed_count(URL) == 10


def test_taiwan_article():
    URL = "https://en.wikipedia.org/wiki/History_of_Taiwan"
    assert get_citations_needed_count(URL) == 19

def test_biotechnology_article():
    URL = "https://en.wikipedia.org/wiki/History_of_biotechnology"
    assert get_citations_needed_count(URL) == 5

def test_biotechnology_article_citation(bio_needed_citation):
    URL = "https://en.wikipedia.org/wiki/History_of_biotechnology"
    assert bio_needed_citation in get_citations_needed_report(URL)

def test_taiwan_article_citation(taiwan_needed_citation):
    URL = "https://en.wikipedia.org/wiki/History_of_Taiwan"
    assert taiwan_needed_citation in get_citations_needed_report(URL)


@pytest.fixture
def bio_needed_citation():
    return "1.)  Although now most often associated with the development of drugs, historically biotechnology has been principally associated with food, addressing such issues as malnutrition and famine."

@pytest.fixture
def taiwan_needed_citation():
    return "1.) [34] The Dutch Governor Pieter Nuyts got entangled in a dispute with the Japanese Hamada Yahei."
    