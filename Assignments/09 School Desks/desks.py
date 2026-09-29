a = int(input())
b = int(input())
c = int(input())



def desk_count(students):
    desks = students//2
    if students%2 == 1:
        desks += 1
    return desks

a_desks = desk_count(a)
b_desks = desk_count(b)
c_desks = desk_count(c)

desks = a_desks + b_desks + c_desks

print(desks)