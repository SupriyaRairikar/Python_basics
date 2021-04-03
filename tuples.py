"""
list is mutable----can be modified

tuple_name = (item1,item2)
immutable in nature: no add,udate operations are allowed
collection of different type of datat type
"""
desd_stu_prj_group_1 = ("a","b","c","d")
print(desd_stu_prj_group_1)
#desd_stu_prj_group_1[2] = "q"  #cant be modified

#unpacking of tuple-----read single entry
name1,name2,name3,name4 = desd_stu_prj_group_1
print(name1)

#to access any member
print(desd_stu_prj_group_1[2])

#tuple of single member
tup=("hi",)   #need to use comma here
print(tup)
print(type(tup))

#to create empty tuple
tup1=()
print(type(tup1))