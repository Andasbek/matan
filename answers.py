# 1. Найти первую производную
import sympy as sp

x = sp.symbols('x')
f = x**3 - 4*x + 6
derivative = sp.diff(f, x)
print("Первая производная:", derivative)

# 2. Найти первую и вторую производные
f = sp.sin(x) * sp.exp(x)
first_derivative = sp.diff(f, x)
second_derivative = sp.diff(f, x, 2)
print("Первая производная:", first_derivative)
print("Вторая производная:", second_derivative)

# 3. Производная сложной функции
f = sp.ln(x**2 + 1)
derivative = sp.diff(f, x)
print("Производная сложной функции:", derivative)

# 4. Производная функции с параметром
a, b, c = sp.symbols('a b c')
f = a * x**2 + b * x + c
derivative = sp.diff(f, x)
print("Производная функции с параметрами:", derivative)

# 5. Найти точку экстремума
f = x**3 - 6*x**2 + 9*x + 1
critical_points = sp.solve(sp.diff(f, x), x)
print("Точки экстремума:", critical_points)

# 6. Найти угловой коэффициент касательной
f = x**2 + 2*x + 1
slope_at_x1 = sp.diff(f, x).subs(x, 1)
print("Угловой коэффициент касательной в точке x=1:", slope_at_x1)

# 7. Проверка на возрастание/убывание функции
f = -x**3 + 3*x**2 + 5
derivative = sp.diff(f, x)
is_increasing = derivative.subs(x, 1) > 0
print("Производная функции:", derivative)
print("Функция возрастает при x=1 и выше:", is_increasing)


# 8. Нахождение точки перегиба
f = x**4 - 4*x**2 + 2
inflection_points = sp.solve(sp.diff(f, x, 2), x)
print("Точки перегиба:", inflection_points)

# 9. Скорость изменения функции
t = sp.symbols('t')
f = t**2 + 3*t + 2
rate_of_change = sp.diff(f, t).subs(t, 2)
print("Скорость изменения в точке t=2:", rate_of_change)

# 10. Найти производную параметрической функции
t = sp.symbols('t')
x_t = t**2
y_t = t**3
dx_dt = sp.diff(x_t, t)
dy_dt = sp.diff(y_t, t)
dy_dx = dy_dt / dx_dt
slope_at_t1 = dy_dx.subs(t, 1)
print("dy/dx в точке t=1:", slope_at_t1)
