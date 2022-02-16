pergunta = float(input('Digite a velocidade do seu carro: '))

if pergunta > 80:
    resposta = (pergunta - 80) * 5 # pego a velocidade e subitraio para pegar a quantidade que passou e depois multiplico por 5 que eh o valor da multa
    print(f'Voce foi multado no valor de {resposta}')
if pergunta <= 80:
    print('Voce passou')