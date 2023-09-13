import pandas as pd


def extrair_dados(dados):
    df = pd.read_csv('dados.csv')
    return df


def transformar_dados(dados):
    dados['Valor Ao Quadrado'] = dados['User ID'] ** 2
    return dados


def carregar_dados(dados, caminho_saida):
    dados.to_csv(caminho_saida, index=False)


def main():
    arquivo_entrada = 'dados.csv'
    arquivo_saida = 'dados_transformados.csv'
    dados_extraidos = extrair_dados(arquivo_entrada)
    dados_transformados = transformar_dados(dados_extraidos)
    carregar_dados(dados_transformados, arquivo_saida)


if __name__ == '__main__':
    main()
