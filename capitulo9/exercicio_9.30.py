# Gerando pagina web a partir de um dicionario

filmes = {
    'drama': ['Cidadao kane', 'O Poderoso Chefao'],
    'comedia': ['Tempos modernos', 'American Pie', 'Dr. Dolittle'],
    'policial': ['Chuva Negra', 'Desejo de matar', 'Dificil de matar'],
    'guerra': ['Rambo', 'Platoon', 'Tora!Tora!Tora!']
}

with open('filmes.html', 'w', encoding='utf-8') as pagina:
    pagina.write('''
!DOCTYPE html>
<html lang="pt-br">
<head>
<meta charset="utf-8">
<title>filmes</title>
</head>
<body> 
    ''')
    for c, v in filmes.items():
        pagina.write('<h1>{}</h1>\n'.format(c))
        pagina.write('<ul>')
        for e in v:
            pagina.write('<li>{}</li>\n'.format(e))
            pagina.write('</ul>')
    pagina.write('''</body>
    </html>''')
pagina.close()