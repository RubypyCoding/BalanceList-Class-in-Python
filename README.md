## Ejercicio - BalanceList class en python

Crea la clase `BalanceList` que tiene dos atributos: `name` (nombre del cliente) y `balances` (lista de saldos por mes). Es importante poder leer el nombre `name` del cliente. Los comportamientos que `BalanceList` tendrá son los siguientes:

- `number_of_balances` regresa el número de saldos que contiene `BalanceList`.
- `total_balance` regresa el saldo total de la lista.
- `add_balance` que agrega un saldo a la lista.
- `current_balance_per_month` regresa el mes y su saldo.
- `next_balance` que regresa el siguiente saldo de la lista de saldos `BalanceList`. Para esto necesitarás llevar control de cuál es el mes actual. Si `BalanceList` se encuentra en el último mes debe de volver al mes inicial de la lista de saldos.

Desarrolla el código basado en las pruebas `specs` correspondientes.

Restricción: 

- Al crear una nueva instancia de `BalanceList` el saldo actual por default debería ser el saldo del primer mes de la lista que le pasen.

```python
"""BalanceList class"""

...

```

```python
"""Ejemplo de objeto y salida"""

balance_1 = BalanceList("Manuel", [["Julio", 234], ["Enero", 456], ["Agosto", 123]])
print(balance_1.name == "Manuel")
print(balance_1.number_of_balances() == 3)
print(balance_1.total_balance() == 813)
balance_1.add_balance(["Marzo", 678])
print(balance_1.number_of_balances() == 4)
print(balance_1.current_balance_per_month() == "Mes: Julio, Saldo: 234")
print(balance_1.next_balance() == 456)
print(balance_1.next_balance() == 123)
print(balance_1.next_balance() == 678)
print(balance_1.current_balance_per_month() == "Mes: Marzo, Saldo: 678")


```

```python
#Test Driven Development - TDD
$ test_balance_list.py
```

