class Test:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city
    def test(self):
        print({"name":self.name, "age":self.age, "city":self.city})

d = "John", 30, "New York"
Test(d).test()