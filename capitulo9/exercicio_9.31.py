import os.path
if os.path.exists('z') and os.path.isdir('z'):
    print('Existe e é um diretório')
else:
    print('Não existe, possivelmente exista apenas o arquivo.')