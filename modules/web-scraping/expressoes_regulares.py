import re
import pandas as pd

lista_pesquisa = ['informações', 'Négocios']

texto = 'Existem muitos desafios para o Big Data. O primeiro deles é a coleta dos dados, pois fala-se aqui de '\
        'enormes quantidades sendo geradas em uma taxa maior do um servidor comum seria capaz de processar e armazenar. '\
        'O segundo desafio é justamente o de processar essas informações. Como elas estão distribuidas, a aplicação deve ser ' \
        ' capaz de consumir partes das informações e gerar pequenas quantidades de dados processados, que serão calculados em '\
        'conjunto depois para criar o resultado final. Outro desafio e a exibição dos resultados, de forma que as informações '\
        'estejam disponíveis de forma clara para os tomadores de decisão'

# Exemplo básico de data mining
for item in lista_pesquisa:
    print('Buscando por "%s" em \n\n %s' % (item, texto))
    
    # Verificado se o termo de pesquisa existe no texto
    if re.search(item, texto):
        print('\n')
        print('Paravra encontrada')
        print('\n')
    else:
        print('\n')
        print('Palavra não encontrada')
        print('\n')

# termo usado para dividir a string
split_term = '@'
frase = 'Qual o domínio de alguém com email: aluno@gmail.com'

re.split(split_term, frase)

def encontrar_padrao(lista: [], frase: str):

    for item in lista:
        print('Pesquisando na frase %r' % item)
        print(re.findall(item, frase))
        print('\n')

frase_padrao = 'zLzL..zzzLLL...zLLLzLL...LzLz...dzzzzz...zLLLL'
list_padrao = [
    'zL*',          # z seguido de zero ou mais L
    'zL+',          # z seguido por um ou mais L
    'zL?',          # z seguido por zero ou um L
    'zL{3}'         # z seguido por três L
    'zL{2,3}'       # z seguido por dois a três L
]

encontrar_padrao(list_padrao, frase_padrao)

frase = 'Esta é uma string com pontuação. Isso pode ser um problema quando fazemos mineração de dados em busca ' \
        'de padrões! Não seria melhor retirar os sinais ao fim de cada frase ?'

# A expressão [^!.?] verifica por valores que não sejam pontuação
# (!, ., ?) e o sinal de adição (+) verifica se o item aparece pelo menos
# uma vez. Traduzindo: esta expressão diz: Traga apenas as palavras na frase

re.findall('[^!.? ]+', frase)

frase = 'Esta é uma frase de exemplo. Vamos verificar quais padrões serão encontrados'

list_padrao = [
    '[a-z]+',        # sequencia de letras minusculas
    '[A-Z]*'         # sequencia de letras maiusculas
    '[a-zA-Z]+',     # sequencia de letras maiusculas e minusculas
    '[A-Z][a-z]+'    # uma letra maiuscula, seguida de uma letra menuscula
]

encontrar_padrao(list_padrao, frase)

# Escape Codes
codigo = ['\d', '\D', '\s', '\S', '\w', '\W']
descricao = ['um digito', 'um não digito', 'espaço (tab, espaço, nova linha, etc..)', 'não espaço', 'alfanumérico', 'não alfanumérico']
pd.DataFrame(zip(codigo, descricao), columns= ['Codigo', 'Significado'])

# o prefixo r antes da expressão regular evita o pre-processamento da ER
# pela linguagem. Colocamos o modificador r (do ingles 'raw', crú)
# imediatamente antes da aspas
r'\b'

frase = 'Esta é uma string com alguns números, como 1287 e símbolos #hashtag'
list_padrao = [
    r'\d+',     #'sequencia de dígitos'
    r'\D+',     #'sequencia de não dígitos'
    r'\s+',     #'sequencia de espaços'
    r'\S+',     #'sequencia de não espeços'
    r'\w+',     #'sequencia de caracteres alfanuméricos'
    r'\W+',     #'sequencia de não alfanuméricos'
]

encontrar_padrao(list_padrao, frase)