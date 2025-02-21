
def get_name(surname):
    print(f"surname is :{surname}")

    while True:
        name = yield            # accepts data from the user
        print(f"received name :{name}")
        print("-" * 60)
        if surname in name:
            print(f"surname found {surname} in {name}")

coObj  = get_name("Pillai")
print(coObj)
coObj.__next__()
coObj.send("Sachin Tendulkar")
coObj.send("Virat Kholi")
coObj.send("Rohit Sharma")
coObj.send("Dhanraj Pillai")

