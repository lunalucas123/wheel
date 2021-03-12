import json
list_of_input = []
target_form = []
geo_list = []
dic = {}

def user_input_count():

        target_item = []
        list_of_input.append(input("Enter form: ").upper())
        # print(list_of_input)
        with open('data2.json') as data_file:    
            data = json.load(data_file)
            for item in list_of_input:
                
                    for form in data:
                # print(item)
                        if form['form'] == item and form['year'] == '2018' :
                            target_item.append(form)
                        if form['form'] == item and form['year'] == '2019' :
                            target_item.append(form)
                        if form['form'] == item and form['year'] == '2020':
                            target_item.append(form)

        print(target_item)   

user_input_count()          
               
                    




