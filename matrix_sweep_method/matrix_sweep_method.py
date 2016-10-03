import numpy as np

init_data = open("init.dat", 'r')
# Начальные условия
start_func = init_data.readline()
# Функция вычисляющая первое граничное условие по x
first_x_condition_func = init_data.readline()
# Функция вычисляющая u(n)-второе граничное условие по x
second_x_condition_func = init_data.readline()
# Функция вычисляющая первое граничное условие по y
first_y_condition_func = init_data.readline()
# Функция вычисляющая u(n)-второе граничное условие по y
second_y_condition_func = init_data.readline()

param_data = open("parameters.dat", 'r')
# считываем количество точек
N = int(param_data.readline())
# считываем шаг по времени
dt = float(param_data.readline())
# считываем точку x0
x0 = float(param_data.readline())
# считываем точку xN
xN = float(param_data.readline())
# считываем точку y0
y0 = float(param_data.readline())
# считываем точку yN
yN = float(param_data.readline())
# считываем погрешность
dx = (xN - x0) / N
dy = (yN - y0) / N
eps = float(param_data.readline())
a_const_array = np.zeros((N, N))
b_const_array = np.zeros((N, N))
c_const_array = np.zeros((N, N))
d_const_array = np.array(N)
for i in range(N):
    a_const_array[i][i] = - 1 / (dx * dx)
    c_const_array[i][i] = - 1 / (dx * dx)
    b_const_array[i][i] = 2 / (dx * dx) + 2 / (dy * dy) + 1 / (dt * dt)
    if i < N - 1:
        b_const_array[i][i + 1] = -1 / (dy * dy)
    if i >= 1:
        b_const_array[i][i - 1] = -1 / (dy * dy)
t = 0
T_old = np.zeros((N, N))
T_new = np.zeros((N, N))
for i in range(N):
    for j in range(N):
        T_old = 
while True:
    if (t > 0.01):
        break
    t += dt
print(b_const_array)
