from typing import  TypedDict, Literal

type Mode = Literal["create"] | Literal["update"] | Literal["execute"] | Literal["setup"]

class CMDArg(TypedDict):
  type: any
  required: bool = False
  help: str 
  mode: Mode

class IArg:
  """
    A classe recebe como entrada o Namespace com os argumentos gerado a partir do argparse.parser.parse_args().

    A classe deve construir um objeto que abstrai a linha de comando injetada pelo usuário no sistema.
  """
  mode: Mode
  def __init__(self, args):
    self.args = args
