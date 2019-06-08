# #list/array

menu = ["Com", "chao", "Thit", "Rau", "Dau"]
# #0 1 2 3 4 
# #index
# # print(menu[4])


# #CRUD
# #1.Create
# new_food="Tom"
# menu.append(new_food)
# print(*menu, sep=", ")

# #2.READ
# #2.1 Read one
# print(menu[2])
# #2.2 Read many
# for food in menu:
#     print(food)

#loop by index, len là viết tắt của độ dài
# for i in range(len(menu):
#     print(i)

#loop by value, index
# for index, value in enumerate(menu):
#     print(index, value)

# #3.UPDATE
# menu[1]="Bun"
# print(menu)

#4.DELETE
#Xoa index se xoa luon value
#delete by index
del menu[2]
print(menu)

#del by value
menu.remove("Dau")
print(menu)