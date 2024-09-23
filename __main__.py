from pathlib import Path
from pyclis import newPyclis

from interface import Arg
from workflow import workflow

def main():
  newPyclis(
    arg=Arg, 
    title="Cria um novo projeto em um diretório especificado.",
    args={
      "--i":{
        "type":Path, 
        "help":"O diretório onde os projetos são armazenados", 
        "required":True, 
        "mode":"create"
      },
      "--p":{
        "type":Path,
        "help":"O diretório do projeto que será manipulado",
        "mode":"update"
      },
      "--up":{
        "type":bool,
        "help":"Abre uma janela que lista todos os projetos e permite selecionar um para ser atualizado",
        "mode":"update"
      },
      "--exec":{
        "type":bool,
        "help":"Executa um projeto",
        "mode":"execute"
      },
      "--setup":{
        "type":bool,
        "help":"Cria os atalhos de intereção com o sistema na raiz do diretório onde os projetos permanecem armazenados",
        "mode":"setup"
      }
    }
  )(workflow)

if __name__=="__main__":
  main() 