import requests
from bs4 import BeautifulSoup


url = 'https://apps.irs.gov/app/picklist/list/priorFormPublication.html?indexOfFirstRow=100&sortColumn=sortOrder&value=form+w-2&criteria=formNumber&resultsPerPage=25&isDescending=false'

response = requests.get(url)
html = response.text

# print(html)

soup = BeautifulSoup(html, 'html.parser')
table = soup.find('table', attrs={"class": "picklist-dataTable"})
rows = table.find_all('tr')
# print(rows)

for row in rows:
    target = row.find_all('td','EndCellSpacer')
    if target:
        target = target[0]

value =  ''.join(target.strings).strip()
myobj = {'key' : int(value)}
print(myobj)


# document.querySelector("#picklistContentPane > div.picklistTable > table > tbody > tr:nth-child(2) > td.EndCellSpacer")
