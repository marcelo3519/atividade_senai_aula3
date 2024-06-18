# Você é um analista de dados, e decidiu trocar de emprego.
# Utilize a media, moda, mediana e o desvio padrão para decidir qual empresa faz sentido para você:
# Justificar por que decidiu por essa empresa.
# ***Verifique isso através dos salários:***
# empresa1 = [1000,6000,1200,8000,1400]
# empresa2 = [5000,4000,3000,2000,7000]
# empresa3 = [1200,1300,8000,3000,15000]
# empresa4 = [1400,1750,2000,4500,5900,7000]
# empresa5 = [1400,1750,2000,4500,5900,7000]

from media import *
from moda import *
from desvio_padrao import *
from mediana import *

empresa1 = [1000,6000,1200,8000,1400]
empresa2 = [5000,4000,3000,2000,7000]
empresa3 = [1200,1300,8000,3000,15000]
empresa4 = [1400,1750,2000,4500,5900,7000]
empresa5 = [1400,1750,2000,4500,5900,7000]

n1=empresa1
n2=empresa2
n3=empresa3
n4=empresa4
n5=empresa5

print('media das empresas :')
media(n1) # menor media salarial
media(n2) 
media(n3) # maior media salarial
media(n4) 
media(n5) 
print('\n')

print('desvio padrao das empresas :')
dp(n1)
dp(n2) # menor desvio  salarial
dp(n3) # maior desvio padrão salarial
dp(n4)
dp(n5)
print('\n')

print('mediana das empresas:')
mediana(n1) # menor mediana salarial
mediana(n2) # maior mediana salarial
mediana(n3)
mediana(n4)
mediana(n5)
print('\n')

print('moda das empresas :')
moda(n1) # menor moda salarial
moda(n2) # maior moda salarial
moda(n3)
moda(n4)
moda(n5)

# ANALISE

# A empresa 3 tem a maior MÉDIA (5700), seguida pela empresa 2 (4200).
# A empresa 2 tem a maior MEDIANA (4000), sugerindo que a maioria dos salários está acima de outras empresas.
# A empresa 3 tem a maior variação (5662.95), indicando salários muito diversos, enquanto a empresa 2 tem a menor variação (1923.53),
# sugerindo salários mais uniformes.

# DECISÃO

# Empresa 2 parece ser a melhor escolha baseada nos seguintes motivos:

# Média alta (4200) comparada com a maioria das empresas, indicando um bom salário médio.
# Mediana alta (4000), sugerindo que a maioria dos salários está acima de outras empresas.
# Desvio Padrão mais baixo (1581.14), indicando menor variação e mais estabilidade salarial.
# Essa análise sugere que a empresa 2 oferece uma boa combinação de salários médios altos e menor variação,
# proporcionando tanto um bom rendimento quanto estabilidade.




