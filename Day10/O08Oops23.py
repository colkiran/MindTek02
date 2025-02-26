
class Mystr(str):

    def AppendMr(self):
        return "Mr." + self

st = Mystr("Yuvraj")
print(st.AppendMr())

print("-" * 60)

class MylistClass(list):

    def append(self, object):
        print("Record :", object)
        super().append(object)

l1 = MylistClass()
l1.append("Sachin")
l1.append("Rahul")
l1.append('Sourav')

print(f"l1 :{l1}")
