name=input("Имя студента:")
surname=input("Фамилия студента:")
year=input("Год рождения студента:")
print(name+'_'+surname+'_'+year)
buff=name
name=surname
surname=buff
print(name+'_'+surname+'_'+str(int(year)+60))
