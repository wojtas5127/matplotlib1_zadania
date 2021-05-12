import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xlrd
import openpyxl

#zadanie1

# x = np.arange(1.0,21.0,1.0)
# y = 1/x
#
# plt.plot(x,y,label='f(x)')
# plt.legend()
# plt.ylabel('f(x)')
# plt.xlabel('x')
# plt.title('Wykres funkcji f(x) dla x [1,20]')
# plt.show()

#zadanie2

# x = np.arange(1.0,21.0,1.0)
# y = 1/x
#
# plt.plot(x,y,'g>:',label='f(x) = 1/x')
# plt.legend()
# plt.ylabel('f(x)')
# plt.xlabel('x')
# plt.title('Wykres funkcji f(x) dla x [1,20]')
# plt.show()

#zadanie3

# x1 = np.arange(0.0, 30.0, 0.1)
# x2 = np.arange(0.0, 30.0, 0.1)
# y1 = np.sin(x1)
# y2 = np.cos(x2)
#
# plt.plot(x1,y1,'-',label='sin(x)')
# plt.plot(x2,y2,'r-',label='cos(x)')
# plt.legend()
# plt.xlabel('x')
# plt.ylabel('cos(x) sin(x)')
# plt.title('Wykresy sin(x) i cos(x)')
#
# plt.show()

#zadanie4

# x1 = np.arange(0.0, 30.0, 0.1)
# x2 = np.arange(0.0, 30.0, 0.1)
# y1 = np.sin(x1)+2
# y2 = np.sin(x1)
#
#
# plt.plot(x1,y1,'b-',label='sin(x)')
# plt.plot(x2,-y2,'y-',color='orange',label='sin(x)')
# plt.legend(loc='center left')
# plt.xlabel('x')
# plt.ylabel('sin(x)')
# plt.title('Wykresy sin(x), sin(x)')
#
# plt.show()

#zadanie5

# xlsx = pd.ExcelFile('imiona.xlsx')
# data = pd.read_excel(xlsx,header=0)

#zadanie6

#zadanie7
# df = pd.read_csv('zamowienia.csv',header=0,sep=';',decimal='.')
# print(df)
# gr= df.groupby(['Sprzedawca']).agg({'idZamowienia':['count']})
#
#
# wykres = gr.plot.pie(subplots=True,legend=False,explode=(0,0,0,0,0,0,0,0.1,0),shadow=True,
#                         autopct=lambda pct:
#                         '{:.1f}%'.format(pct),textprops=dict(color='black',fontsize=10)
#                         )
# plt.ylabel('')
# plt.xticks(rotation=0)
# plt.title('Ilość zamówień poszczególnych sprzedawców')
# plt.show()