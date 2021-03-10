import requests
import bs4
from bs4 import BeautifulSoup
from pandas import DataFrame
import pandas as pd
import json
import csv

target_form = []
target_title = []
target_year = []
target_obj = {}
year = 0

with open('data.json') as data_file:    
        data = json.load(data_file)
        for form in data:
            year = form['year']
            # print(year)
            if form['form_number'] == "Form 1040" :
                target_form.append(form['form_number'])
                target_title.append(form['form_title'])
                target_year.append(form['year'])

        target_obj['form_number'] = target_form[0]
        target_obj['form_title'] = target_title[0]
        target_obj['min_year'] = target_year[-1]
        target_obj['max_year'] = target_year[0]
        print(target_obj)
        # print(target_list, target_title, target_year)