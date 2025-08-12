#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount = 0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.t_items = [] 

  def add_item(self, title, price, quantity = 1):
    item = {
      'title' : title,
      'price' : price,
      'quantity' : quantity
    }
    self.items.extend([title] * quantity)
    self.t_items.append(item)
    self.total += price * quantity

  def apply_discount(self):
    if self.total != 0:
      self.total = self.total * 0.8
      print(f'After the discount, the total comes to ${int(self.total)}.')
      return
    print("There is no discount to apply.")

  def items(self):
    return self.items
  
  def void_last_transaction(self):
    if len(self.t_items) == 0:
      self.total = 0.0
      return 
    self.total -= self.t_items[-1]['price'] * self.t_items[-1]['quantity']
    self.t_items.pop()
    self.items.pop()