import json

with open('task3/tests.json') as t:
    tests = json.load(t)
with open('task3/values.json') as v:
    values = json.load(v)
t.close()
v.close()

for i in tests['tests']:  
    
    for k in values['values']:
        if i['id'] == k['id']:
            i['value'] = k['value']
        
    for item_values in i:
        if item_values == "values":
            for under_obj in i['values']:
                
                for k in values['values']:
                    if under_obj['id'] == k['id']:
                        under_obj['value'] = k['value']
                
                for under_obj_attr in under_obj:
                    if under_obj_attr == "values":
                        for lower_obj in under_obj['values']:
                            
                            for k in values['values']:
                                if lower_obj['id'] == k['id']:
                                    lower_obj['value'] = k['value']
                            
                            for the_lowest_obj in lower_obj:
                                if the_lowest_obj == "values":
                                    for lower_attr in lower_obj['values']:
                                        
                                        for k in values['values']:
                                            if lower_attr['id'] == k['id']:
                                                lower_attr['value'] = k['value']
  
report = open("task3/report.json", "w")
json.dump(tests, report, sort_keys=True, indent=2)
report.close()
print('JSON записан')
        

    