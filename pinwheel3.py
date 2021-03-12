import json
# index = 25 
count = 0
list_of_input = ['Publ 1', 'Publ 1', 'Publ 1', 'Publ 1', 'Publ 1', 'Publ 1', 'Publ 1', 'Publ 1 (AR)', 'Publ 1 (BN)', 'Publ 1 (CN-T)', 'Publ 1 (FA)', 'Publ 1 (FR)', 'Publ 1 (GUJ)', 'Publ 1 (HT)', 'Publ 1 (IT)', 'Publ 1 (JA)', 'Publ 1 (KM)', 'Publ 1 (KO)', 'Publ 1 (PA)', 'Publ 1 (PL)', 'Publ 1 (PT)', 'Publ 1 (RU)', 'Publ 1 (SP)', 'Publ 1 (SP)', 'Publ 1 (SP)', 'Publ 1 (TL)', 'Publ 1 (UR)', 'Publ 1 (VIE)', 'Publ 1 (ZH-T)', 'Publ 3', 'Publ 3', 'Publ 3', 'Publ 3', 'Publ 3', 'Publ 3', 'Publ 3', 'Publ 3', 'Publ 3', 'Publ 3', 'Publ 3', 'Publ 3', 'Publ 3', 'Publ 3', 'Publ 3', 'Publ 3', 'Publ 3', 'Publ 3', 'Publ 3', 'Publ 3', 'Publ 3', 'Publ 3', 'Publ 3', 'Publ 3', 'Publ 3', 'Publ 3', 'Publ 4', 'Publ 4', 'Publ 4', 'Publ 4', 'Publ 4', 'Publ 4', 'Publ 4', 'Publ 5 (SP)', 'Form 11-C', 'Form 11-C', 'Form 11-C', 'Form 11-C', 'Form 11-C', 'Form 11-C', 'Form 11-C', 'Form 11-C', 'Form 11-C', 'Form 11-C', 'Form 11-C', 'Form 11-C', 'Form 11-C', 'Form 11-C', 'Form 11-C', 'Form 11-C', 'Form 11-C', 'Form 11-C', 'Form 11-C', 'Form 11-C', 'Publ 15', 'Publ 15', 'Publ 15', 'Publ 15', 'Publ 15', 'Publ 15', 'Publ 15', 'Publ 15', 'Publ 15', 'Publ 15', 'Publ 15', 'Publ 15', 'Publ 15', 'Publ 15', 'Publ 15', 'Publ 15', 'Publ 15']
for i in list_of_input:
    count += 1
print(count)
# user_input = input("Enter form : ").lower()
# print(type(user_input))

def user_input_count():
    count = int(input("Please enter the number of forms you want to search for :  "))
    while count > 0:
        list_of_input.append(input("Enter form : ").upper())
        count = count - 1

user_input_count()  

# fixed_list = []
target_form = []
target_title = []
target_year = []
target_obj = {  "form_number": "",
                "form_title": "No record",
                "min_year": "No min year",
                "max_year": "No max year"}


with open('data.json') as data_file:    
        data = json.load(data_file)
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



