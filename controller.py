import string
with open("controller.txt") as my_template:
    data = my_template.read()
    print('Template loaded')
    print(data)
    date_template = string.Template(data)

filename = 'Jobtype.php'
row = {'ControllerName': "Jobtype", 'Model_model': "Jobtype_model",'class':"jobtype",'model':"jobtype",'model_model':"jobtype_model","primarykey":"jobtype_id","classcreate":"jobtypecreate","classlist":"jobtype","title":"Job Type"}
print(date_template.safe_substitute(row))
with open(filename, 'w') as output_file:
    output_file.write(date_template.safe_substitute(row))