class Coffee:
    def __init__(self, name):
        self.name = name

    @property
    def name (self):
        return self._name
    @name.setter
    def name(self, name):
        if not (type(name) == str):
            raise Exception("Name must be String")
        elif len(name) < 3:
            raise Exception("Name must be longer than 2 characters")
        elif hasattr(self, "name"):
            raise Exception("Name cannot be changed after instantiation")
        else: self._name = name
    
    def orders(self):
        return [order for order in Order.all if order.coffee == self]
    
    def customers(self):
        return list(set([order.customer for order in self.orders()]))
        
    def num_orders(self):
        return len(self.orders())
    
    def average_price(self):
        return sum([order.price for order in self.orders()])/self.num_orders()

class Customer:
    def __init__(self, name):
        self.name = name

    @property
    def name (self):
        return self._name
    @name.setter
    def name(self, name):
        if not (type(name) == str):
            raise Exception("Name must be a string")
        elif len(name) < 1 or len(name) > 15:
            raise Exception("Name must be between 1 and 15 characters in length")
        else: self._name = name

        
    def orders(self):
        return [order for order in Order.all if order.customer == self]
    
    def coffees(self):
        return list(set([order.coffee for order in self.orders()]))
    
    def create_order(self, coffee, price):
        return Order(self, coffee, price)
    
    @classmethod
    def most_aficionado(cls, coffee):
        orders = [order for order in Order.all if order.coffee == coffee]
        most_aficionado = [0, None] #[price, customer_obj]
        for order in orders:
            if order.price > most_aficionado[0]:
                most_aficionado = [order.price, order.customer]
        return most_aficionado[1]

    
class Order:
    all = []
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)

    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, price):
        if type(price) != float:
            raise Exception("Price must be a float")
        elif price < 1.0 or price > 10.0:
            raise Exception ("price must be between 1.0 and 10.0")
        elif hasattr(self, "price"):
            raise Exception("Price cannot be changed after instantiation")
        else: self._price = price

    @property
    def customer (self):
        return self._customer
    @customer.setter
    def customer(self, customer):
        if isinstance(customer, Customer):
            self._customer = customer
        else:
            raise Exception ("Must be of type Customer")
    
    @property
    def coffee (self):
        return self._coffee
    @coffee.setter
    def coffee(self, coffee):
        if isinstance(coffee, Coffee):
            self._coffee = coffee
        else:
            raise Exception("Must be of type Coffee")