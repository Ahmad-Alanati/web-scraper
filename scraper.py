import requests
from  bs4 import BeautifulSoup
import json

def get_citations_needed_count(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content,'html.parser')
    citation_needed_a = soup.find_all('a', title="Wikipedia:Citation needed")

    return len(citation_needed_a)
    

def get_citations_needed_report(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content,'html.parser')
    citation_needed_sup = soup.find_all('sup', class_="noprint Inline-Template Template-Fact")
    citation_needed_p = [p.parent.text.strip() for p in citation_needed_sup]
    report = ""
    for p in citation_needed_p:
        report += p+"\n\n"
    return report

if __name__ == "__main__":
    URL = "https://en.wikipedia.org/wiki/History_of_Mexico"
    with open("test.txt",'w') as file:
        file.write("the number of citation needed"+str(get_citations_needed_count(URL))+"\n\n")
        file.write(get_citations_needed_report(URL))
    
    print(get_citations_needed_count(URL))
    print(get_citations_needed_report(URL))