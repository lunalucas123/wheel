import requests
import bs4
from bs4 import BeautifulSoup
from pandas import DataFrame
import pandas as pd
import json
import csv
import re
# index = 25 
user_input = input("Enter form : ").lower()
user_input = user_input.replace(' ','+')
fixed_form = user_input[0].upper() + user_input[1:]
user_input = fixed_form.replace('+',' ')



# with open('IRS.csv', mode='w') as csv_file:
#    fieldnames = ['form_number', 'title', 'year']
#    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
#    writer.writeheader()

obj_form_number = {}
list_form_number = []
list_title = []
list_year = []
page_max_sliced = 0
list_of_json = []



def open_pages(index):
    
    url = f'https://apps.irs.gov/app/picklist/list/priorFormPublication.html?indexOfFirstRow={index}&sortColumn=sortOrder&value={fixed_form}&criteria=formNumber&resultsPerPage=25&isDescending=false'
    
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    
    results_table = soup.find('table', attrs={"class": "searchFieldsTable"})
    results_page = results_table.find_all('tr')
    # print(results_page)
    # results_number = results_page.find('tr', attrs={"class": "ShowByColumn"} )
    for r in range(len(results_page)):
        result_number = results_page[r].find_all('th', 'ShowByColumn')
        # print(result_number)

        for e in result_number: 
            page_max_num = e.text.strip()
            # print(page_max_num)
           
            
            page_max_sliced = page_max_num[-25:-5].strip()
            # print(page_max_sliced)
            # page_max_sliced = page_max_sliced.replace(',', '')
            # print(type(int(page_max_sliced)))
            res = int(''.join([n for n in page_max_sliced if n.isdigit()]))
            # res = list(map(int, temp)) 
            
            
                 
    # print(page_max_sliced)

    table = soup.find('table', attrs={"class": "picklist-dataTable"})
    first_page_rows = table.find_all('tr')
    # print(type(first_page_rows))
    first_page_rows_len = len(first_page_rows)
    # print(first_page_rows)
    

    for x in range(first_page_rows_len):
        form_number = first_page_rows[x].find_all('td', 'LeftCellSpacer')
        # print(form_number)
        title = first_page_rows[x].find_all('td', 'MiddleCellSpacer')
        # print(title)
        year = first_page_rows[x].find_all('td', 'EndCellSpacer')

        # new_form = fixed_form.replace('+',' ')
        # form_result_list = []
        # title_result_list = []
        # year_result_list = []
        for f in form_number: 
            list_form_number.append(f.text.strip())
            for f in list_form_number:
                obj_form_number = {"form_number" : f }


        for t in title: 
            list_title.append(t.text.strip())
            for t in list_title:
                obj_form_number['form_title'] = t
            
            # y = json.dumps(obj_form_number)

            # print(y)

        for y in year: 
            list_year.append(y.text.strip())
            for y in list_year:
                obj_form_number['year'] = int(y)

    


    list_of_json.append(obj_form_number)
    with open('data.json', 'w') as outfile:
        json.dump(list_of_json, outfile)
    # print(list_of_json)
  
    
    # print(list_form_number,list_title, list_year)
    
    # data = { 'Form_number': form_result_list,'Title':title_result_list, 'year':year_result_list}
    # df = DataFrame(data, columns = ['Form_number','Title','year'])
    # df.to_csv(r'/Users/geovannymolina/Desktop/IRS.csv')
    index = index + 25
    
    # print(index, type(res))
    while index < res:
      
        if index == page_max_sliced:
            break
        else:
            return open_pages(index)




open_pages(0)

target_form = []
target_title = []
target_year = []
target_obj = {}
year = 0

with open('data.json') as data_file:    
        data = json.load(data_file)
        for form in data:
            
            print(form['form_number'].upper(), user_input.upper())
            
            if form['form_number'].upper() == user_input.upper():
                target_form.append(form['form_number'])
                target_title.append(form['form_title'])
                target_year.append(form['year'])

        target_obj['form_number'] = target_form[0]
        target_obj['form_title'] = target_title[0]
        target_obj['min_year'] = target_year[-1]
        target_obj['max_year'] = target_year[0]
        print(target_obj)
# target_form = []
# target_title = []
# target_year = []
# target_obj = {}
# year = 0

# with open('data.json') as data_file:    
#         data = json.load(data_file)
#         for form in data:
#             year = form['year']
#             print(user_input)
#             if form['form_number'] == 'Form W-2':
#                 target_form.append(form['form_number'])
#                 target_title.append(form['form_title'])
#                 target_year.append(form['year'])

#         target_obj['form_number'] = target_form[0]
#         target_obj['form_title'] = target_title[0]
#         target_obj['min_year'] = target_year[-1]
#         target_obj['max_year'] = target_year[0]
#         print(target_obj)

  


