import datetime


data= datetime.date(2000,9,12)
print(data)
dia=int(input("Digite o dia-->"))
mes=int(input("Digite o mês-->"))
ano=int(input("Digite o ano-->"))

data_nova=data.replace(day=dia,month=mes,year=ano)
print(data_nova)

dn=data_nova.day
mn=data_nova.month
an=data_nova.year
print(dn,mn,an, sep="/")

