import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
import re

user_input = input("Enter form : ").lower()
user_input = user_input.replace(' ','+')
fixed_form = user_input[0].upper() + user_input[1:]


# print(fixed_form)

url = f"https://apps.irs.gov/app/picklist/list/priorFormPublication.html?value={fixed_form}&criteria=formNumber&submitSearch=Find"

response = requests.get(url)
html = response.text

# soup = BeautifulSoup(response.content,'lxml')
# table = soup.find_all('table')[3] 
# df = pd.read_html(str(table))
# json = df[0].to_json(orient='records')

soup = BeautifulSoup(html, 'html.parser')
table = soup.find('table', attrs={"class": "picklist-dataTable"})
rows = table.find_all('tr')
outcome = []
# print(rows)

for row in rows:
    target_column_one = row.find_all('td', 'LeftCellSpacer')
    target_column_two = row.find_all('td', 'MiddleCellSpacer')
    target_column_three = row.find_all('td', 'EndCellSpacer')
    # print(target_column[0].find('a'))
    if target_column_one:
        forms = target_column_one[0].find('a')
        
        #<a href="https://www.irs.gov/pub/irs-prior/fw2--2021.pdf">Form W-2</a>
        # print(link)
        for e in forms.find_all() : 
            e.decompose()
        form = forms.text 
        # print(type(form))

        for td in target_column_two:
            stripped_title = td.text.strip()

        for td in target_column_three:
            stripped_year = td.text.strip()
           
            outcome.append({'form_number': str(form),
                   'title': str(stripped_title),
                   'year' : int(stripped_year)
                  })






        content_url = json.dumps(outcome)

print(content_url)
 
        
        
    
    # if target_column_two:
    #     forms = target_column_two[0].find('a')
        # href = forms['href']
        # print(href)
        # print(link)
        # print(type(link))
        # https://www.irs.gov/pub/irs-prior/fw2p--1972.pdf
        
        # idx_pdf = href.index('.pdf')
        # Year = href[39:idx_pdf]
        # print(Year)
        # # if code == s :


        # # print((type(code)))
        
    
    # format_Number = row.find_all('td', 'EndCellSpacer')
    # years = [ele.text.strip() for ele in years]


    # titles = row.find_all('td', 'MiddleCellSpacer')
    # titles = [ele.text.strip() for ele in titles]

    # products = row.find_all('td', 'LeftCellSpacer')
    # products = [ele.text.strip() for ele in products]


    # data_years.append([ele for ele in years if ele])
    # data_title.append([ele for ele in titles if ele])
    # data_product.append([ele for ele in products if ele])


#LeftCellSpacer
# print(data_years)
# print(data_title)
# print(data_product)

# value =  ''.join(target.strings).strip()
# myobj = {'min_year' : int(value)}
# print(myobj)


