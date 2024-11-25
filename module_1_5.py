immutable_var = (1,"Johan",False)
print(immutable_var)
#immutable_var[1] = "jon";
#print(immutable_var)
# не изменяеться потому что картеж не изменяеммый тип данных
# (он как констатна в сишарпе)
# можно изметить такие данные как список внутри кортежа
mutable_list = ([9,4], [5,6])
mutable_list[1][1] = "$"
print(mutable_list)
