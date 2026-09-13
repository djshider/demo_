class car:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
    def shijia(self):
        print(f"{self.brand}{self.model}在试驾中")
    def total_price(self,price,discount,rate):
        total_price = price*rate+price*discount
        return total_price
s1=car("奥迪","x7","7年")
s1.shijia()
total_price=s1.total_price(100000000,2,3)
print(f"该款车的2费用为：{total_price}元")
class education:
    def __init__(self,math,english,chinese):
        self.math = math
        self.english = english
        self.chinese=chinese
    def study(self):
        print("好好学习天天向上")
c1=education(math=100,english=99,chinese=77)
c1.study()

