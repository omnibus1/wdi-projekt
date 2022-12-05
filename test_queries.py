
import sqlite3

import matplotlib.pyplot as plt
connection_object=sqlite3.connect('filmy.db')
cursor=connection_object.cursor()
cursor.execute("SELECT AVG(TEN),AVG(NINE),AVG(EIGHT),AVG(SEVEN),AVG(SIX),AVG(FIVE),AVG(FOUR),AVG(THREE),AVG(TWO),AVG(ONE) FROM ALLVOTES")
x=cursor.fetchall()
arr=[]
for value in x[0]:
    arr.append(value)
y=[10,9,8,7,6,5,4,3,2,1]
plt.plot(y,arr)
plt.show()
print(arr)