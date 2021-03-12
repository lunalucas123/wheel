import json
# index = 25 
# count = 0
list_of_input = []
# user_input = input("Enter form : ").lower()
# print(type(user_input))
target_form = []
geo_list = []
dic = {}
count = int(input("Please enter the number of forms you want to search for :  "))



def user_input_count(count):
    
    
    while count > 0:
        # count = count - 1 
        if count == 0:
            break
        else:
            target_obj = {}
            list_of_input.append(input("Enter form: ").upper())
            print(list_of_input)
            with open('data.json') as data_file:    
                data = json.load(data_file)
                for item in list_of_input:
                    # for item in list_of_input:
                        for form in data:
                    # print(item)
                            if form['form'] == item:
                                target_form.append(form)

                        min_form = target_form[-1]    
                        max_form = target_form[0] 
                        

            target_obj = {"form_number": max_form['form'],
                    "form_title": max_form['title'],
                    "min_year": min_form['year'],
                    "max_year": max_form['year']}



            geo_list.append(target_obj)
            list_of_input.pop()                    
                        
            print(geo_list)   
            # print(target_obj.clear())
            target_form.clear()               
            return user_input_count(count - 1)

user_input_count(count)          


    
        
        
        

        # print(target_form)
        # print(max_form)
        # print(min_form)

        # print(max_form['form'])
        # print(max_form['title'])

        # print(max_form['year'])
        # print(min_form['year'])


# target_obj = {  "form_number": "",
#                 "form_title": "No record",
#                 "min_year": "No min year",
#                 "max_year": "No max year"}


# with open('data.json') as data_file:    
#         data = json.load(data_file)
        # for form in data:
        # for item in list_of_input:
        #     print(item)
                # if form['form_number'] == item:
                #     print(form['form_number'],form['form_title'])
            # print(form['form_number'])
            
                # print(item)

            
                
        #             target_form.append(form['form_number'])
        #             target_title.append(form['form_title'])
        #             target_year.append(form['year'])




        # target_obj['form_number'] = target_form[0]
        # target_obj['form_title'] = target_title[0]
        # target_obj['min_year'] = target_year[-1]
        # target_obj['max_year'] = target_year[0]
# print(target_obj)



