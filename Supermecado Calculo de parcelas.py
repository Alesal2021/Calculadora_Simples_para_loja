print('Supermecado')
print('1 - Pagamento a vista')
print('2 - Pagamento em 3X')
print('3 - Pagamento de 5X')
print('4 - Pagamento de 10X')
op = input('Escolha uma opção acima:')# COLOQUEI UM INT MAS TEM QUE COLOCAR FLOAT E TRATAR OS RESULTADOS
s1 = int(input('Digite o valor da compra:'))
if op == '1':
   # res = s1 * 0.95 # AQUI E UMA FORMA DE FAZER O CALCULO
    preco = (s1 * 5) /100 # NESTA LINHA UMA SEGUNDA FORMA DE CALCULO
    res = s1 - preco
    print('O valor do desc  e {} o total a pagar`{} :'.format(preco,res))
elif op == '2':
    res = s1
    preco = s1 / 3
    print('A parcela do produto = {} e total a pagar = {}'.format(preco,res))
elif op == '3':
    #res = s1 * 1.02 # AQUI E UMA FORMA DE FAZER O CALCULO
    #parc = res / 5
    preco = s1 * 2 / 100 # NESTA LINHA UMA SEGUNDA FORMA DE CALCULO
    res1= preco + s1
    res = (preco + s1) / 5
    print('O valor total a pagar = {} e o valor das parcelas a pagar = {} '.format(res1,res))
elif op == '4':
    res = s1 * 1.08
    parc = res / 10
    print('O Valor total a pagar = {} e o valor das parcelas = {}'.format(res,parc))
else:
    print('Operação Invalida')