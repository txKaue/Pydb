import json
import os

## Função para useDB

#Isso aqui é uma instancia do banco todo, do app todo
#Dentro dessa instancia eu vou criar as databases
class DB:
    def __init__ (self, data_path, dbItens):

        if not os.path.exists(self.db_path):
            os.makedirs(self.db_path) #Se não tiver a pasta, crie.

        self.db_path = data_path
        self.dbItens = dbItens




    ## Função para criar um "tabela":
    def mkDb(self, nome): 
        try:
            with open(f'{self.db_path}{nome}.json', 'w') as f:
                json.dump({}, f)
            
            self.dbItens.append(nome)
            print("db created")

        except (OSError, IOError) as e:
            print(f"db can't be created. Error: {e}")


    #Use database (equivalente)
    def useDb(self, nome):
        if nome in self.dbItens and os.path.exists(self.db_path):
            index = self.dbItens.index(nome)
            return index
        else:
            print(f"{nome} não exsite")





##Função para deletar dados
def rmDb(nome):
    caminho_arquivo = f'./data/{nome}.json'

    try:
        os.remove(caminho_arquivo)
        print(f"{nome} deletado com sucesso")
    except FileNotFoundError:
        print(f"{nome}' não existe.")
    except Exception as e:
        print(f"Erro na deleção: {e}")

##Função para criar uma "tabela" no banco

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
