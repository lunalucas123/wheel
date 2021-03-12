import json

list_of_input = []
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
            # print(list_of_input)
            with open('data2.json') as data_file:    
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
                    "max_year": max_form['year'],
                    "pdf_link": max_form['link']}



            geo_list.append(target_obj)
            list_of_input.pop()                    
                        
            print(geo_list)   
            # print(target_obj.clear())
            target_form.clear()               
            return user_input_count(count - 1)

user_input_count(count)          




