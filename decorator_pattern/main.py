from plain_pizza import PlainPizza
from cheese_pizza import CheesePizza

plain_pizza = PlainPizza(10)


pizza = CheesePizza(plain_pizza)

print(pizza.cost)