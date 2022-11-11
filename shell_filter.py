from django.db.models import Subquery, Q

from my_app.models import Account, Customer, Work

icloud_customers = Customer.objects.filter(email__icontains='icloud.com')
# print(icloud_customers)

ltd_customer = Customer.objects.filter(work__company__icontains='ltd')
print(ltd_customer)

protonmail_accounts = Account.objects.filter(customer__email__icontains='protonmail')
# print(protonmail_accounts)