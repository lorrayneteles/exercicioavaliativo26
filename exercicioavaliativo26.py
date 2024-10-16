# faça o preco de 3 produtos e calcule o valor total da compra

prod1 = float(input('Qual o preço do primeiro produto?'))
prod2 = float(input('Qual o preço do segundo produto?'))  
prod3 = float(input('Qual o preço do terceiro produto?'))
total = prod1 + prod2 + prod3
print(f'O valor total da compra é R${total:.2f}')
