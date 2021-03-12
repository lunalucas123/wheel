import json

list_of_input = []
target_form = []
geo_list = []
dic = {}
# count = int(input("Please enter the number of forms you want to search for :  "))



def user_input_count():
    
    
    # while count > 0:
    #     # count = count - 1 
    #     if count == 0:
    #         break
    #     else:
        target_item = []
        list_of_input.append(input("Enter form: ").upper())
        # print(list_of_input)
        with open('data.json') as data_file:    
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

        #             min_form = target_form[-1]    
        #             max_form = target_form[0] 
                    

        # target_obj = {"form_number": max_form['form'],
        #         "form_title": max_form['title'],
        #         "min_year": min_form['year'],
        #         "max_year": max_form['year']}



        # geo_list.append(target_obj)
        # list_of_input.pop()                    
                    
        print(target_item)   
        # print(target_obj.clear())
        # target_form.clear()               
        # return user_input_count()

user_input_count()          




