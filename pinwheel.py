import requests
import bs4
from bs4 import BeautifulSoup
from pandas import DataFrame
import pandas as pd
import json
import csv

# user_input = input("Enter form : ").lower()
# user_input = user_input.replace(' ','+')
# fixed_form = user_input[0].upper() + user_input[1:]

# url = f'https://apps.irs.gov/app/picklist/list/priorFormPublication.html?indexOfFirstRow=0&sortColumn=sortOrder&value={fixed_form}&criteria=formNumber&resultsPerPage=25&isDescending=false'

# # search_field = soup.find_all('table', {"class": 'searchFieldsTable'})
# # field_tr = soup.find_all('th', {"class": "NumResultsDisplayed"})
# response = requests.get(url)
# html = response.text
# soup = BeautifulSoup(html, 'html.parser')
# table = soup.find('table', attrs={"class": "picklist-dataTable"})
# first_page_rows = table.find_all('tr')
# first_page_rows_len = len(first_page_rows)
# # print(first_page_rows)

# for x in range(first_page_rows_len):
#     form_number = first_page_rows[x].find_all('td', 'LeftCellSpacer')
#     for e in form_number: 
#         print(e.text.strip())

# for x in range(first_page_rows_len):
#    title = first_page_rows[x].find_all('td', 'MiddleCellSpacer')
#    for td in title:
#         stripped_title = td.text.strip()
#         print(stripped_title)

# for x in range(first_page_rows_len):
#     year = first_page_rows[x].find_all('td', 'EndCellSpacer')
#     for td in year:
#         stripped_year = td.text.strip()
#         print(stripped_year)





# website = f'https://apps.irs.gov/app/picklist/list/priorFormPublication.html?indexOfFirstRow={index}&sortColumn=sortOrder&value={fixed_form}&criteria=formNumber&resultsPerPage=25&isDescending=false'


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

    # while page_max_sliced > index:
    #     index = index + 25
        
    #     if index >= page_max_sliced:
    #         break
    #     else:
    #         continue
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









# response2 = requests.get(url2)
# html2 = response2.text

# soup2 = BeautifulSoup(html2, 'html.parser') 
# field_tr2 = soup2.find_all('th', {"class": "NumResultsDisplayed"})
# table2 = soup2.find('table', attrs={"class": "picklist-dataTable"})  

# second_page_rows = table2.find_all('tr')

# print(first_page_rows)
# print(second_page_rows)
































# for x in range(first_page_rows_len):
#     form_number = first_page_rows[x].find_all('td', 'LeftCellSpacer')
#     for e in form_number: 
#         print(e.text.strip())

# for x in range(first_page_rows_len):
#    title = first_page_rows[x].find_all('td', 'MiddleCellSpacer')
#    for td in title:
#         stripped_title = td.text.strip()
#         print(stripped_title)

# for x in range(first_page_rows_len):
#     year = first_page_rows[x].find_all('td', 'EndCellSpacer')
#     for td in year:
#         stripped_year = td.text.strip()
#         print(stripped_year)

# with open('IRS.csv', mode='w') as csv_file:
#    fieldnames = ['form_number', 'title', 'year']
#    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
#    writer.writeheader()


#Creating an empty lists of variables
# irs_form_number= []
# irs_title = []
# irs_year = []

# #Defining the irs function

# def opencodezscraping():
#     irs_year = []
#     next_page = webpage + str(page_number)
#     response= requests.get(str(next_page))
#     soup = BeautifulSoup(html, 'html.parser')
#     soup_form= soup.first_page_rows.find_all('td', 'LeftCellSpacer')
#     soup_title= soup.first_page_rows.find_all('td', 'MiddleCellSpacer')
#     soup_year= soup.first_page_rows.find_all('td', 'EndCellSpacer')
    

#     for x in range(len(soup_title)):
#         irs_form_number.append(soup_form[x].text.strip())
#         irs_title.append(soup_title[x].p.text.strip()) 
#         irs_year.append(soup_year[x].text.strip())
        


              
    # if page_number < 25:
    #     page_number = page_number + 25
    #     opencodezscraping(webpage, page_number)

    # opencodezscraping('https://www.opencodez.com/page/', 0)





# for tr in rows:
#     target_column_one = tr.find_all('td', 'LeftCellSpacer')
#     target_column_two = tr.find_all('td', 'MiddleCellSpacer')
#     target_column_three = tr.find_all('td', 'EndCellSpacer')
#     # print(target_column[0].find('a'))
#     if target_column_one:
#         forms = target_column_one[0].find('a')
        

#         
#         for e in forms.find_all() : 
#             e.decompose()
#         form = forms.text 
#         # print(type(form))

#         for td in target_column_two:
#             stripped_title = td.text.strip()

#         for td in target_column_three:
#             stripped_year = td.text.strip()
           
#             outcome.append({'form_number': str(form),
#                    'title': str(stripped_title),
#                    'year' : int(stripped_year)
#                   })






#         content_url = json.dumps(outcome)

# print(content_url)
 
        
        
    
   
# https://apps.irs.gov/app/picklist/list/priorFormPublication.html?indexOfFirstRow=0&sortColumn=sortOrder&value=form+w-2&criteria=formNumber&resultsPerPage=200&isDescending=false

# https://apps.irs.gov/app/picklist/list/priorFormPublication.html?indexOfFirstRow=200&sortColumn=sortOrder&value=form+w-2&criteria=formNumber&resultsPerPage=200&isDescending=false

# <a href="https://apps.irs.gov/app/picklist/list/priorFormPublication.html?indexOfFirstRow=1225&amp;sortColumn=sortOrder&amp;value=form+1040&amp;criteria=formNumber&amp;resultsPerPage=25&amp;isDescending=false">« Previous</a>