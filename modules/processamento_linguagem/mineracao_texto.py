# import nltk
# Rodar esse comando download antes de seguir
# nltk.download()

# Import
from nltk.corpus import PlaintextCorpusReader
from nltk.corpus import stopwords
from nltk import FreqDist
from matplotlib.colors import ListedColormap
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from os import path
import string

diretorio = path.abspath('.')
diretorio = path.join(diretorio, "dados\\Arquivos")

corpus = PlaintextCorpusReader(diretorio, '.*')

# Explorando os dados
# Obtem todos os nomes dos arquivos
arquivos = corpus.fileids()

# Obtem apenas o primeiro arquivo
arquivos[0]
# Obtem os 100 primeiros registros
arquivos[0:100]

# itera todos os arquivos
for a in arquivos:
    print(a)

# Lê o conteudo do primeiro arquivo
texto = corpus.raw('1.txt')

# Lê o conteudo de todos os arquivos do corpus
todo_texto = corpus.raw()

# Obtem todas as palavras 
palavras = corpus.words()

# Obtem a quantidade de palavras existentes no corpus
len(palavras)

# Obtem apenas uma unica palavra
palavras[170]

# Remoção de palavras sem valor semantico para o contexto
# e, do, da....
stops = stopwords.words('english')
mapa_cores = ListedColormap(['orange', 'green', 'red', 'magenta', 'blue', 'gray'])
nuvem_palavras = WordCloud(background_color= 'white',
                           colormap= mapa_cores,
                           stopwords= stops,
                           max_words=100)

nuvem_palavras.generate(todo_texto)
plt.imshow(nuvem_palavras)

palavras_sem_stop = [p for p in palavras if p not in stops]
len(palavras_sem_stop)

palavras_sem_pontuacao = [p for p in palavras_sem_stop if p not in string.punctuation]
palavras_sem_digitos = [p for p in palavras_sem_pontuacao if p not in string.digits]

len(palavras_sem_digitos)

frequencia = FreqDist(palavras_sem_pontuacao)

mais_frequentes = frequencia.most_common(100)