from pyclis.interface import IArg
from pathlib import Path
from pyclis.utils import get_projects_dir

class Arg(IArg):
  def __init__(self, args):
    self.in_dir: Path = args.i
    """O diretório onde os projetos são armazenados"""
    self.project_dir: Path = args.p
    """O diretório do projeto que será manipulado"""

    self.mode = "create"
    if args.setup:
      self.mode = "setup"
    elif args.exec:
      self.mode = "execute"
    elif args.up or self.project_dir != None:
      self.mode = "update"
  
  def in_dir_len(self):
    return len(list(filter(lambda x: x.is_dir(), get_projects_dir(self.in_dir).iterdir())))
