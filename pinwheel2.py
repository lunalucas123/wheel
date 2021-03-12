import requests
import bs4
from bs4 import BeautifulSoup
from pandas import DataFrame
import pandas as pd
import json
import csv
import re
# index = 25 

# user_input = input("Enter form : ").lower()
# print(type(user_input))

# def user_input_count():
#     count = int(input("Please enter how many forms you want to search for :  "))
#     while count > 0:
#         list_of_input.append(input("Enter form : ").lower())
#         count = count - 1

# user_input_count()  

# fixed_list = []
# for f in list_of_input:
#     user_input = f.replace(' ','+')
#     fixed_list.append(user_input[0].upper() + user_input[1:])
    #['Form+1040', 'Form+1040']




# user_input = fixed_form.replace('+',' ')
list_of_input = []

list_of_json = []
list_title = []

list_year = []
table_dictionary = []
list_form_number = []
list_title = []
list_year = []


def open_pages(index):
    
    # list_of_json = []
    

    

        url = f'https://apps.irs.gov/app/picklist/list/priorFormPublication.html?indexOfFirstRow={index}&sortColumn=sortOrder&value=&criteria=&resultsPerPage=25&isDescending=false'
        
    
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        
        # results_table = soup.find('table', attrs={"class": "searchFieldsTable"})
        # results_page = results_table.find_all('tr')
        # print(results_page)
        # results_number = results_page.find('tr', attrs={"class": "ShowByColumn"} )
        # for r in range(len(results_page)):
        #     result_number = results_page[r].find_all('th', 'ShowByColumn')
            # print(result_number)

            # for e in result_number: 
            #     page_max_num = e.text.strip()
            #     # print(page_max_num)
            
            #     page_max_sliced = page_max_num[-13:-5].strip()
                
            #     res = int(''.join([n for n in page_max_sliced if n.isdigit()]))
            #     # print(res)
                
                
                    
        # print(page_max_sliced)
        

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
                list_form_number.append(f.text.strip())
            for t in title: 
                list_title.append(t.text.strip())
            for y in year: 
                list_year.append(y.text.strip())

        while index < 20150:
            index += 25
            
            if index == 20150:
                table_dictionary = [{'form': list_form_number.upper(), 'title': list_title, 'year': list_year} for list_form_number,list_title,list_year in zip(list_form_number,list_title,list_year)]
                with open('data.json', 'w') as outfile:
                    json.dump(table_dictionary, outfile)
            else:
                return open_pages(index)

    # table_dictionary = [{'form': list_form_number.upper(), 'title': list_title, 'year': list_year} for list_form_number,list_title,list_year in zip(list_form_number,list_title,list_year)]
    # print(table_dictionary)
    # index = index + 5
    
    # with open('data.json', 'w') as outfile:
    #     json.dump(table_dictionary, outfile)

            
    # with open('data.json', 'w') as outfile:
    #         json.dump(table_dictionary, outfile)

    # print(table_dictionary)
        # for form in data:
            
            # print(form['form_number'].upper(), user_input.upper())
            
            # if form['form_number'].upper() == user_input.upper():
            # target_form.append(form['form_number'])
            # target_title.append(form['form_title'])
            # target_year.append(form['year'])

    

open_pages(0)











    # for l in list_form_number:
    #     obj_form_number[" form " + l ] = l.upper()
    # # list_of_json.append(obj_form_number)  
    # for t in list_title:
    #     obj_form_number["title" + t] = t  
        

        
    # list_of_json.append(obj_form_number)  
    # for y in list_year:
    #     obj_form_number["year" + y] = int(y)
    #     obj_form_number["title" + t] = t  
    #     obj_form_number[" form " + l ] = l.upper() 
    # list_of_json.append(obj_form_number)   

    
    # print(list_of_json)
        # title = first_page_rows[x].find_all('td', 'MiddleCellSpacer')
        
        # for t in title: 
        #     list_title.append(t.text.strip())
        # for t in list_title:
        #     obj_form_number[t] = t
        # list_of_json.append(obj_form_number)
        # # print(title)

   
        # year = first_page_rows[x].find_all('td', 'EndCellSpacer')

        # for y in year: 
        #     list_year.append(y.text.strip())
        # for y in list_year:
        #     obj_form_number[y] = int(y)
        # list_of_json.append(obj_form_number)
        # # new_form = fixed_form.replace('+',' ')
        # # form_result_list = []
        # # title_result_list = []
        # # year_result_list = []
    
    # print(list_of_json)


            # for y in list_year:
            #     print(y)
            #     obj_form_number['year'] = int(y)
            #     list_of_json.append(obj_form_number)
    # print(list_of_json)    
    # print(list_year)
        
                    
    # print(obj_form_number)

            

    
    
    # list_of_json.append
    # (obj_form_number)
    # print(list_of_json)
    # print(obj_form_number)
    # list_of_json.append(obj_form_number)
    # with open('data.json', 'w') as outfile:
    #     json.dump(obj_form_number, outfile)
    # print(list_of_json)
  
    
    # print(list_form_number,list_title, list_year)
    
    # data = { 'Form_number': form_result_list,'Title':title_result_list, 'year':year_result_list}
    # df = DataFrame(data, columns = ['Form_number','Title','year'])
    # df.to_csv(r'/Users/geovannymolina/Desktop/IRS.csv')

    # print(obj_form_number)
    
    # with open('data.json', 'w') as outfile:
    #     json.dump(list_of_json, outfile)
    
    # print(index, type(res))
    # print(index)
    # index = index + 25
    
    # # print(index, type(res))
    # while index < 100:
  
    #     if index == 100:
    #         break
    #     else:
    #         return open_pages(index)




    # print(list_of_json)
# target_form = []
# target_title = []
# target_year = []
# target_obj = {"form_number": "",
#                 "form_title": "No record",
#                 "min_year": "No min year",
#                 "max_year": "No max year"}


# with open('data.txt', 'w') as outfile:
#     json.dump(obj_form_number, outfile)
#         # for form in data:
            
        #     # print(form['form_number'].upper(), user_input.upper())
            
        #     # if form['form_number'].upper() == user_input.upper():
        #     target_form.append(form['form_number'])
        #     target_title.append(form['form_title'])
        #     target_year.append(form['year'])




        # target_obj['form_number'] = target_form[0]
        # target_obj['form_title'] = target_title[0]
        # target_obj['min_year'] = target_year[-1]
        # target_obj['max_year'] = target_year[0]
        # print(target_obj)



