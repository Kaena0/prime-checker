# Prime Checker

Цей проєкт містить функцію на Python, яка перевіряє, чи є передане число простим.

## Опис

Функція `is_prime(n)` приймає ціле число `n` і повертає:
- `True` — якщо число є простим;
- `False` — якщо ні.

Прості числа — це числа, які мають лише два дільники: 1 і саме себе.

## Приклад використання

```python
from prime import is_prime

print(is_prime(2))    # True
print(is_prime(10))   # False
print(is_prime(17))   # True
