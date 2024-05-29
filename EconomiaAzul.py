import random

# Função para capturar dados simulados de espécies marinhas
def capturar_dados(quantidade):
    especies_possiveis = ['peixe-palhaço', 'peixe-leão','coral-vermelho','coral-negro', 'caranguejo-verde', 'estrela-do-mar-coroa-de-espinhos','mexilhão-zebra','ascídia-dourada', 'tubarão-martelo','Sardinha', 'atum']
    dados_capturados = []
    for _ in range(quantidade):
        especie = random.choice(especies_possiveis)
        localizacao = (random.uniform(-90, 90), random.uniform(-180, 180))  # Coordenadas aleatórias
        dados_capturados.append((especie, localizacao))
    return dados_capturados

# Função para identificar espécies invasoras
def identificar_invasoras(dados):
    especies_invasoras = ['peixe_leão', 'caranguejo_verde', 'mexilhão-zebra','ascídia-dourada','estrela-do-mar-coroa-de-espinhos']
    invasoras_detectadas = [dado for dado in dados if dado[0] in especies_invasoras]
    return invasoras_detectadas

# Função para apresentar dados
def apresentar_dados(dados):
    for especie, localizacao in dados:
        print(f"Espécie: {especie}, Localização: {localizacao}")

# Função para salvar dados em arquivo
def salvar_dados(dados, filename):
    try:
        with open(filename, 'w') as file:
            for especie, localizacao in dados:
                file.write(f"{especie},{localizacao[0]},{localizacao[1]}\n")
    except Exception as e:
        print(f"Erro ao salvar dados: {e}")

# Função para ler dados de arquivo
def ler_dados(filename):
    dados = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                especie, lat, lon = line.strip().split(',')
                dados.append((especie, (float(lat), float(lon))))
    except FileNotFoundError:
        print(f"Arquivo {filename} não encontrado.")
    except Exception as e:
        print(f"Erro ao ler dados: {e}")
    return dados

# Função principal
def main():
    try:
        quantidade = 20  # Quantidade de dados a serem capturados
        dados_capturados = capturar_dados(quantidade)
        print("Dados Capturados:")
        apresentar_dados(dados_capturados)

        invasoras = identificar_invasoras(dados_capturados)
        print("\nEspécies Invasoras Detectadas:")
        apresentar_dados(invasoras)

        salvar_dados(dados_capturados, 'dados_capturados.csv')
        salvar_dados(invasoras, 'invasoras_detectadas.csv')
        print("\nDados salvos em arquivos 'dados_capturados.csv' e 'invasoras_detectadas.csv'.")

        dados_lidos = ler_dados('dados_capturados.csv')
        print("\nDados Lidos do Arquivo 'dados_capturados.csv':")
        apresentar_dados(dados_lidos)
    except Exception as e:
        print(f"Erro no sistema: {e}")

if __name__ == "__main__":
    main()
