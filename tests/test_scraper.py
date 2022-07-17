import pytest


try:
    from beautiful_soup.scraper import get_citations_needed_count, get_citations_needed_report
except:
    from scraper import get_citations_needed_count, get_citations_needed_report



def test_get_citations_needed_count_exists():
    assert get_citations_needed_count

def test_get_citations_needed_report_exists():
    assert get_citations_needed_count

# def test_bfs(graph):
#     nodes = graph.get_nodes()
#     root = nodes[0]
#     print(root.value)
#     actual = graph.breadth_first(root)
#     expected = ["Pandora", "Arendelle", "Metroville", "Monstropolis", "Narnia", "Naboo"]
#     assert actual == expected