
#############################################################################################################################
#   filename:pyletras.py                                                       
#   created: 2022-05-25                                                              
#   import your librarys below                                                    
#############################################################################################################################
import requests
from bs4 import BeautifulSoup

def pyletras(name=input("Digite o nome da banda: "),cancao=input("Qual nome da canção que deseja buscar: ")):
    url = requests.get(f"https://www.letras.mus.br/{name.replace(' ', '-').lower()}/{cancao.replace(' ', '-').lower()}")
    soup = BeautifulSoup(url.content)
    try:
        lyrics = soup.find_all("div", class_="cnt-letra p402_premium")
        for i in lyrics:
            result = i.get_text("<p>").replace("<p>", "\n")

        with open(f"""{name.replace(" ","_").lower()}_{cancao.replace(" ","_").lower()}.txt""", "a", encoding='UTF-8') as output:
            output.write(f"""{name.replace("-", " ").upper()}-{cancao.replace("-", " ").upper()}'\n' {result.center(80)}'\n'""")
        print(f"""Os items banda: {name.replace("-", " ").upper()} e canção: {cancao.replace("-", " ").upper()} foram criadas com sucesso!""")

    except:
        print(f"""Banda: {name.replace("-", " ")} ou Letra {cancao.replace("-"," ")} não encontrada!""")
        