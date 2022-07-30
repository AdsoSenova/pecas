from django import template


register = template.Library()

#This the custom filter, name is getitems

def getdata(json_data, args):
    func_name = args.strip("/")
    if func_name == '':
        func_name = 'index'
    print("Funtion name>>>: ",func_name)
    return json_data.get(func_name)


register.filter('getdata', getdata)



# request.path	                  /home/
# request.get_full_path	         /home/?q=test
# request.build_absolute_uri	 http://127.0.0.1:8000/home/?q=test