
import abc


nomefuncionario = str(input("qual o seu nome? "))
vendasq = int(input("Quantas vendas você fez? ")) 
somadev=0

for i in range(1,vendasq+1):
    abc_loop = float(input(f"Valor {i}:"))
    somadev+=abc_loop
    media = somadev/vendasq

if media>=100000:
    print("O funcionario atingiu a meta")
else:
    print("Funcionario nao atingiu a meta")