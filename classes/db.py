import json
import os

## Função para criar os dados:
def mkDb(nome):
    db_path = "./data/"

    if not os.path.exists(db_path):
        os.makedirs(db_path) #Se não tiver a pasta, crie.

    try:
        with open(f'{db_path}{nome}.json', 'w') as f:
            json.dump({}, f)
        print("db created")

    except (OSError, IOError) as e:
        print(f"db can't be created. Error: {e}")

def mkData(db, nome):
    db_path = f"./data/{db}.json"

    try:
        # Abrindo o arquivo JSON existente para leitura
        with open(db_path, 'r') as f:
            # Carrega o conteúdo do arquivo em um dicionário Python
            dados = json.load(f)

        new_data = {
            nome: {},
        }

        # Adicionando os novos dados ao dicionário carregado
        dados.update(new_data)  # Atualiza o dicionário com os novos dados

        # Abrindo o arquivo novamente, agora para escrita
        with open(db_path, 'w') as f:
            # Grava o dicionário atualizado de volta no arquivo
            json.dump(dados, f, indent=4)

        print("Dados adicionados com sucesso!")

    except FileNotFoundError:
        print(f"Erro: O arquivo '{db}' não foi encontrado.")
    except json.JSONDecodeError:
        print(f"Erro: O arquivo '{db}' não contém um JSON válido.")
    except Exception as e:
        print(f"Erro inesperado: {e}")
