# Problema 3: Auditoría de inventario y reabastecimiento

def calcular_cantidad_pedir(stock_actual, stock_minimo):
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    else:
        return 0


inventario = [
    ["A001", "Arroz", 20, 50],
    ["A002", "Aceite", 15, 30],
    ["A003", "Azúcar", 40, 40],
    ["A004", "Café", 8, 25],
    ["A005", "Leche", 60, 45]
]

print("LISTA DE PEDIDOS PARA REABASTECIMIENTO")
print("--------------------------------------")

for articulo in inventario:
    codigo = articulo[0]
    nombre = articulo[1]
    stock_actual = articulo[2]
    stock_minimo = articulo[3]

    cantidad_pedir = calcular_cantidad_pedir(stock_actual, stock_minimo)

    print(f"Artículo: {nombre} | Cantidad a pedir: {cantidad_pedir}")
