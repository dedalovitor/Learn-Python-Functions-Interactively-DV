# Your code goes here:
def render_person(name,date,color,age,gender):
    return str(name)+str(" is a ")+str(age)+ str(" years old male born in ") +str(date)+ str(" with ") +str(color)+str(" eyes")


# Do not edit below this line
print(render_person('Bob', '05/22/1983', 'green', 23, 'male'))