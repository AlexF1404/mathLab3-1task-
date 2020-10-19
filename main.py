import numpy as np
import cvxpy as cvx

x = cvx.Variable(2)

mass = np.array([[1, 3],
              [1, 1],
              [1, 2]])

b = np.array([1500, 1200, 1300])

c = np.array([16, 20.5])

func = [mass * x <= b]

resh = cvx.Maximize(c * x)
rez = cvx.Problem(resh, func)
rez.solve()
print('Значение целевой функции: '+ str(round(rez.value)))
print('Сорт А    |   Сорт Б')
print(str(round(x.value[0]))+"    |   "+str(round(x.value[1])))

