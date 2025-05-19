# Autor: Eng. Charles Ferreira
# Data de implemnentação: 20240728 - 060000PM
# Data da última revisão: 
# Finalidade do programa: O programa tem por finalidade calcular a eficiẽncia de um transformador com base nos dados medidos
# fornecidos pelo usuário. As potências calculadas estão em VA (potência aparente). Para obter a potência real em Watts,
# deve-se conhecer o PF (Power Factor) do DUT (Device Under Test) e incluí-lo no cálculo.

# Descricao do programa
print('Programa para calculo de eficiencia de transformadores')
print('\nInstrucoes:')
print('Meca os seguintes valores e preencha os dados na ordem')
print('em que forem solicitados.')
# Entrada de dados pelo usuario
Vtri = float(input('\nTensao nominal da rede eletrica (V): '))
Itri = float(input('Corrente consumida no primario (A): '))
Vtro = float(input('Tensao do secundario escolhido (V): '))
Itro = float(input('Corrente drenada do secundario (A): '))

# Calculo do rendimento
Rend = ((Vtro * Itro) / (Vtri * Itri)) * 100

# Retorno ao usuario
print('\nO remdimento esperado do transformador e {:.4f}%.'.format(Rend))