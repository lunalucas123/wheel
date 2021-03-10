import requests
import bs4
from bs4 import BeautifulSoup
from pandas import DataFrame
import pandas as pd
import json
import csv
# index = 25 
user_input = input("Enter form : ").lower()
user_input = user_input.replace(' ','+')
fixed_form = user_input[0].upper() + user_input[1:]

with open('IRS.csv', mode='w') as csv_file:
   fieldnames = ['form_number', 'title', 'year']
   writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
   writer.writeheader()

list_form_number = []
list_title = []
list_year = []
page_max_sliced = ''


def open_pages(index):
    
    url = f'https://apps.irs.gov/app/picklist/list/priorFormPublication.html?indexOfFirstRow={index}&sortColumn=sortOrder&value={fixed_form}&criteria=formNumber&resultsPerPage=25&isDescending=false'
    
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
   
    results_table = soup.find('table', attrs={"class": "searchFieldsTable"})
    results_page = results_table.find_all('tr')
    # results_number = results_page.find('tr', attrs={"class": "ShowByColumn"} )
    for r in range(len(results_page)):
        result_number = results_page[r].find_all('th', 'ShowByColumn')

        for e in result_number: 
            page_max_num = e.text.strip()
            page_max_sliced = page_max_num[-12:-5].strip()
            page_max_sliced = page_max_sliced.replace(',', '')
            page_max_sliced = int(page_max_sliced)        
    # print(page_max_sliced)

    table = soup.find('table', attrs={"class": "picklist-dataTable"})
    first_page_rows = table.find_all('tr')
    first_page_rows_len = len(first_page_rows)
    # print(first_page_rows)
    

    for x in range(first_page_rows_len):
        form_number = first_page_rows[x].find_all('td', 'LeftCellSpacer')
        title = first_page_rows[x].find_all('td', 'MiddleCellSpacer')
        year = first_page_rows[x].find_all('td', 'EndCellSpacer')


        for e in form_number: 
            list_form_number.append(e.text.strip())
        for e in title: 
            list_title.append(e.text.strip())
        for e in year: 
            list_year.append(e.text.strip())
        
    
    # print(list_form_number,list_title, list_year)
    
    data = { 'Form_number': list_form_number,'Title':list_title, 'year':list_year}
    df = DataFrame(data, columns = ['Form_number','Title','year'])
    df.to_csv(r'/Users/geovannymolina/Desktop/IRS.csv')
    index = index + 25

    while index < page_max_sliced:
      
        if index == page_max_sliced:
            break
        else:
            return open_pages(index)

open_pages(0)





