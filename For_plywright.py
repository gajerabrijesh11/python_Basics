# problem 1
"""""

website=["google.com","www.google.com","https://google.com"]
for i in website:
 print(i)

 """
# problem 2
"""""
my_dictionary = dict(email= "gajera.brijesh@gmail.com", password= "xyz", role= "QA")
print(my_dictionary)

"""
# problem 3
"""""
def greet(name):

    print(f"Hello, {name}! How are you doing today?")

# Calling the function
greet("brijesh")

"""""
# problem 4
"""""
user_input = input("Enter No: ")
if int(user_input) >= 50:
    print("high")
else:
    print("low")
    """""
# problem 5
class Browser:
    def open_browser(self):
        print("Browser opened")
    def close_broser(self):
        print("Browser closed")
test=Browser()
test.open_browser()
test.close_broser()