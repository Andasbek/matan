### Задачи на математический анализ

#### 1. Вычисление предела
Найти предел функции \( f(x) = \frac{\sin x}{x} \) при \( x \to 0 \).

```python
import sympy as sp

x = sp.symbols('x')
f = sp.sin(x) / x
limit = sp.limit(f, x, 0)
print("Предел:", limit)
```

#### 2. Вычисление производной
Найти производную функции \( f(x) = x^3 - 2x + 5 \).

```python
f = x**3 - 2*x + 5
derivative = sp.diff(f, x)
print("Производная:", derivative)
```

#### 3. Вычисление второй производной
Найти вторую производную функции \( f(x) = \ln(x^2 + 1) \).

```python
f = sp.ln(x**2 + 1)
second_derivative = sp.diff(f, x, 2)
print("Вторая производная:", second_derivative)
```

#### 4. Нахождение экстремума функции
Найти точки экстремума функции \( f(x) = x^3 - 6x^2 + 9x + 1 \).

```python
f = x**3 - 6*x**2 + 9*x + 1
critical_points = sp.solve(sp.diff(f, x), x)
print("Точки экстремума:", critical_points)
```

#### 5. Вычисление определенного интеграла
Найти определенный интеграл \( \int_1^2 x^2 \, dx \).

```python
integral = sp.integrate(x**2, (x, 1, 2))
print("Определенный интеграл:", integral)
```

#### 6. Вычисление неопределенного интеграла
Найти неопределенный интеграл \( \int e^x \, dx \).

```python
integral_indef = sp.integrate(sp.exp(x), x)
print("Неопределенный интеграл:", integral_indef)
```

#### 7. Разложение функции в ряд Тейлора
Разложить функцию \( f(x) = \sin(x) \) в ряд Тейлора до 5-го порядка около точки \( x = 0 \).

```python
taylor_series = sp.series(sp.sin(x), x, 0, 6)
print("Ряд Тейлора:", taylor_series)
```

#### 8. Решение простого дифференциального уравнения
Решить дифференциальное уравнение \( \frac{dy}{dx} = x^2 \).

```python
y = sp.Function('y')
dydx = sp.Derivative(y(x), x)
equation = sp.Eq(dydx, x**2)
solution = sp.dsolve(equation)
print("Решение дифференциального уравнения:", solution)
```

#### 9. Проверка на сходимость ряда
Проверить, сходится ли ряд \( \sum_{n=1}^{\infty} \frac{1}{n^2} \).

```python
n = sp.symbols('n')
series_sum = sp.summation(1 / n**2, (n, 1, sp.oo))
print("Сумма сходящегося ряда:", series_sum)
```

#### 10. Нахождение площади под кривой
Найти площадь под кривой \( f(x) = x^2 \) на интервале от \( x = 0 \) до \( x = 3 \).

```python
area = sp.integrate(x**2, (x, 0, 3))
print("Площадь под кривой:", area)
```