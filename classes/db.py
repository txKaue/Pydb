import json
import os
import subprocess

## Função para useDB

#Isso aqui é uma instancia do banco todo, do app todo
#Dentro dessa instancia eu vou criar as databases
class DB:

    def __init__(self, dataPath):
        self.dataPath = dataPath

        # Verifica se a pasta não existe e cria
        if not os.path.exists(self.dataPath):
            os.makedirs(self.dataPath)  # Se não tiver a pasta, crie.
            print(f"Pasta '{self.dataPath}' criada com sucesso.")
            
            # Caminho do arquivo .bat
            bat_file_path = "set_permissions.bat"

            # Conteúdo do script .bat para conceder permissões com privilégios elevados
            bat_content = f'''
            @echo off
            :: Solicita privilégios administrativos
            echo Executando como administrador...
            powershell -Command "Start-Process cmd -ArgumentList '/c icacls \"{self.dataPath}\" /grant Everyone:(F) /T' -Verb RunAs"
            echo Permissões aplicadas com sucesso!
            pause
            '''

            # Cria o arquivo .bat
            with open(bat_file_path, "w") as bat_file:
                bat_file.write(bat_content)

            # Executa o arquivo .bat para aplicar permissões
            subprocess.run([bat_file_path], check=True)
            print(f"Permissões para 'Everyone' aplicadas à pasta '{self.dataPath}'.")

        self.dbItens = []  # Inicializando a lista de itens no banco de dados
        self.useItem = None  # Nenhum item está sendo usado inicialmente





    ## Função para criar um "tabela":
    def mkDb(self, nome): 
        try:
            with open(f'{self.dataPath}{nome}.json', 'w') as f:
                json.dump({}, f)
            
            self.dbItens.append(nome)
            print("db created")

        except (OSError, IOError) as e:
            print(f"db can't be created. Error: {e}")




    #Use database (equivalente)
    def useDb(self, nome):
        if nome in self.dbItens and os.path.exists(self.dataPath):
            index = self.dbItens.index(nome)
            self.useItem = index
            print(self.dbItens[self.useItem])
        else:
            print(f"{nome} não exsite")


    
    def mkData(self, nome):

        try:
            # Abrindo o arquivo JSON existente para leitura
            with open(self.dataPath, 'r') as f:
                # Carrega o conteúdo do arquivo em um dicionário Python
                dados = json.load(f)

            new_data = {
                nome: {},
            }

            # Adicionando os novos dados ao dicionário carregado
            dados.update(new_data)  # Atualiza o dicionário com os novos dados

            # Abrindo o arquivo novamente, agora para escrita
            with open(self.dataPath, 'w') as f:
                # Grava o dicionário atualizado de volta no arquivo
                json.dump(dados, f, indent=4)

            print("Dados adicionados com sucesso!")

        except FileNotFoundError:
            print(f"Erro: O arquivo '{nome}' não foi encontrado.")
        except json.JSONDecodeError:
            print(f"Erro: O arquivo '{nome}' não contém um JSON válido.")
        except Exception as e:
            print(f"Erro inesperado: {e}")





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


