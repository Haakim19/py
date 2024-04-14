basic_salary=input("your basic salary: ")
bonus_salary=input("bonus salary: ")
salary_deduc=input("salary deduction: ")
salary_incr=input("salary increment %(0.1 for 10%): ")

incresed_salary=float(basic_salary)+float(basic_salary)*float(salary_incr)

net_salary=incresed_salary+float(bonus_salary)-float(salary_deduc)

print(f'your Net salary is: {net_salary}')