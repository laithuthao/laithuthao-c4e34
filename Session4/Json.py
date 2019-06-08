salary_table = [
    {
        "name": "Duc", "salary": 30, "hour": 8, "days":20
    }, 
    {
        "name": "Hoan", "salary": 50, "hour": 5, "days":25
    },
    {
        "name": "Dat", "salary": 40, "hour": 7, "days":30
    }
]

total_salary=0

for employee in salary_table:
    month_salary=employee["salary"]*employee["hour"]*employee["days"]
    total_salary += month_salary
    total_salary = total_salary + month_salary
    print("Luong thang cua {0} la {1}".format(employee["name"], month_salary))

print("Tong luong cua 3 nguoi la {0}".format(total_salary))


# luonghoan=salary_table[1]["salary"]*salary_table[1]["hour"]*salary_table[1]["days"]
# print("Luong cua Hoan la", luonghoan)

# luongdat=salary_table[2]["salary"]*salary_table[2]["hour"]*salary_table[2]["days"]
# print("Luong cua Hoan la", luonghoan)

# tongluong=luongduc+luonghoan+luongdat
# print("Tong luong 3 nguoi", tongluong)

letters = ["a", "b", "c"]
for letter in letters:
    print(letter)