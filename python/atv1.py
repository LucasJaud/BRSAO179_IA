
def hello_world():
    print("hello word")

def sum(a , b): 
    print(f'{a} + {b} = {a + b}')

def calc_volume(base ,height, width):
    print( f'area: {base * width * height} cm³ ')

def calc_total_shop(nome,preco, quant):
    print(f'Produto: {nome} \nPreço unitário: {preco}R$ \nQuantidade: {quant} \nValor Total: {(preco * quant):.2f}')
    
    pass    
    
    


print('atividade 1:')
hello_world()
print('\natividade 2:')
sum(12,14)
print('\natividade 3:')
calc_volume(12, 14, 20)
print('\natividade 4:')
calc_total_shop('Cadeira infantil',12.40,3)
