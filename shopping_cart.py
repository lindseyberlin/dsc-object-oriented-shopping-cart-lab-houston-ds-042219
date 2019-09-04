import statistics

class ShoppingCart:
    # write your code here
    def __init__(self, emp_discount=None):
        self.total = 0
        self.emp_discount = emp_discount
        self.items = []
        self.list_item_prices = []
    
    def add_item(self, name, price, quantity=1):
        for num in range(quantity):
            self.items.append({name: price})
            self.list_item_prices.append(price)
            self.total += (price)
        return self.total
    
    def mean_item_price(self):
        mean = statistics.mean(self.list_item_prices)
        return '{:.2f}'.format(round(mean, 2))
        
    def median_item_price(self):
        median = statistics.median(self.list_item_prices)
        return '{:.2f}'.format(round(median, 2))
        
    def apply_discount(self):
        if self.emp_discount:
            self.dec_discount = (self.emp_discount/100)
            self.discounted_total = self.total - (self.total * self.dec_discount)
            return self.discounted_total
        else:
            return "Sorry, there is no discount to apply to your cart :("

    def void_last_item(self):
        if self.items == []:
            return "There are no items in your cart!"
        else:
            self.total = (self.total - self.items[-1].values())
            self.items.pop()