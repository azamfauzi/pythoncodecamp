import string
with open("model.txt") as my_template:
    data = my_template.read()
    print('Template loaded')
    print(data)
    date_template = string.Template(data)

filename = 'Jobtype_model.php'
row = {'import': "JobType", 'tablename': "l_jobtype",'primarykey':"jobtype_id",'Model_model':"Jobtype_model"}
print(date_template.safe_substitute(row))
with open(filename, 'w') as output_file:
    output_file.write(date_template.safe_substitute(row))