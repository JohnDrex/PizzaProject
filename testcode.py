import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Pizzeria.settings")

import django
django.setup()

from pizzas.models import *

#select * from topic - gives all the rows and columns
pizzas = Pizza.objects.all()
#object oriented programsing for sql

#for topic in topics:
    #print(topic)
    #print(topic.date_added)


p = Pizza.objects.get(id=1)
print(p)

toppings = Topping.objects.filter(pizza=p)

for t in toppings:
    print(t.toppings)


#from django.contrib.auth.models import User

#for user in User.objects.all():
    #print(user.username)
    #print(user.last_login)


#<td>Comments: &nbsp <a href="{% url 'pizzas:comments' p.id %}"></a>{{3}}</a>&nbsp&nbsp</td>

#<img src="{% static 'hawaiian.jpg' %}">