!pip install fuzzywuzzy
!pip install python-Levenshtein

from fuzzywuzzy import fuzz

# Similaridade da string em ordem
fuzz.ratio('Apple Inc.', 'Apple')

# Similaridade da string parcial
fuzz.ratio('Apple Inc.', 'Apple')
fuzz.partial_ratio('Apple Inc.', 'Apple')

# Ignora as ordens da palavra
fuzz.ratio('Lakers X Chicago Bulls', 'Chicago Bulls X Lakers')
fuzz.partial_ratio('Lakers X Chicago Bulls', 'Chicago Bulls X Lakers')
fuzz.token_sort_ratio('Lakers X Chicago Bulls', 'Chicago Bulls X Lakers')

# Ignora palavras duplicadas
fuzz.ratio('Today we have a great game: Lakers X Chicago Bulls', 'Chicago Bulls X Lakers')
fuzz.partial_ratio('Today wa have a great game: Lakers X Chicago Bulls', 'Chigado Bulls X Lakers')
fuzz.token_sort_ratio('Today wa have a great game: Lakers X Chicago Bulls', 'Chigado Bulls X Lakers')
fuzz.token_set_ratio('Today wa have a great game: Lakers X Chicago Bulls', 'Chigado Bulls X Lakers')