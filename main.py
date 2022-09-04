from googlesearch import search

palavras_pesquisa = input("Insira o termo que deseja pesquisar no Google: ")
print(palavras_pesquisa)

lista_urls = search(palavras_pesquisa, tld="com.br", lang="pt", num=5, stop=10, pause=2)
print(lista_urls)

for url in lista_urls:
    print(url)
