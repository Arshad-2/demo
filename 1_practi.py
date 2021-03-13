class student:
    def __init__(self, name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print("hello",self.name)
        print("your marks is",self.marks)
st=student("nadeem",5)
st.display()