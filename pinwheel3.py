import json
# index = 25 
# count = 0
list_of_input = []
# user_input = input("Enter form : ").lower()
# print(type(user_input))

def user_input_count():
    count = int(input("Please enter the number of forms you want to search for :  "))
    while count > 0:
        list_of_input.append(input("Enter form : ").upper())
        count = count - 1

    with open('data.json') as data_file:    
        data = json.load(data_file)
        for form in data:
            for item in list_of_input:
                # print(item)
                    if form['form'] == item:
                        print(form)
                # print(form['form_number'])
user_input_count()  

# fixed_list = []
# target_form = []
# target_title = []
# target_year = []
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



