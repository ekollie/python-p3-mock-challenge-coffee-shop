#!/usr/bin/env python3
import ipdb

from classes.many_to_many import Customer
from classes.many_to_many import Order
from classes.many_to_many import Coffee

if __name__ == '__main__':
    print("HELLO! :) let's debug")
    customer1 = Customer("Bill")
    customer2 = Customer("Rory")
    customer3 = Customer("Amanda")
    coffee1 = Coffee("latte")
    coffee2 = Coffee("cappuccino")
    coffee3 = Coffee("espresso")
    customer1.create_order(coffee1, 7.0)
    customer1.create_order(coffee2, 3.0)
    customer3.create_order(coffee3, 5.0)
    customer3.create_order(coffee2, 5.0)
    ipdb.set_trace()
