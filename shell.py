import json
from my_app.models import Account, Work, Customer

with open('data.json', 'r') as file:
    json_dicts = json.load(file)

for one_dict in json_dicts:
    customer = Customer.objects.create(name=one_dict['name'], email=one_dict['email'], phone=one_dict['phone'])
    work = Work.objects.create(address=one_dict['address'], city=one_dict['city'], company=one_dict['company'],
                               postalZip=one_dict['postalZip'], customer=customer)
    account = Account.objects.create(pin=one_dict['pin'], acc_num=one_dict['acc_num'], pan=one_dict['pan'], cvv=one_dict['cvv'],
                                     customer=customer)

