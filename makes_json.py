import requests
import bs4
from bs4 import BeautifulSoup
from pandas import DataFrame
import pandas as pd
import json
import csv
import re

list_of_input = []
list_of_json = []
list_title = []
list_year = []
table_dictionary = []
list_form_number = []
link_form = []
list_title = []
list_year = []


def open_pages(index):
    
        url = f'https://apps.irs.gov/app/picklist/list/priorFormPublication.html?indexOfFirstRow={index}&sortColumn=sortOrder&value=&criteria=&resultsPerPage=25&isDescending=false'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        table = soup.find('table', attrs={"class": "picklist-dataTable"})
        first_page_rows = table.find_all('tr')
        # print((first_page_rows))
        first_page_rows_len = len(first_page_rows)
        # print(first_page_rows_len)
        
        for x in range(first_page_rows_len):
            form_number = first_page_rows[x].find_all('td', 'LeftCellSpacer')
            title = first_page_rows[x].find_all('td', 'MiddleCellSpacer')
            year = first_page_rows[x].find_all('td', 'EndCellSpacer')
            # print(form_number)
            for f in form_number: 
                list_form_number.append(f.text.strip().upper())
            for h in form_number: 
                link_form.append(h.a["href"] )
            for t in title: 
                list_title.append(t.text.strip())
            for y in year: 
                list_year.append(y.text.strip())

        while index <= 20150:
            index += 25
            
            if index == 20150:
                table_dictionary = [{'form': list_form_number, 'title': list_title, 'year': list_year, 'link': link_form} for list_form_number,list_title,list_year,link_form in zip(list_form_number,list_title,list_year,link_form)]
                with open('data2.json', 'w') as outfile:
                    json.dump(table_dictionary, outfile)
            else:
                return open_pages(index)

  open_pages(0)










