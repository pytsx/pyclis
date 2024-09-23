from pyclis.cli import buildCLIArg, CMDArg
from pyclis.interface import IArg
from typing import  Callable, TypeVar

Arg = TypeVar("Arg", bound=IArg)

def newPyclis(title:str, arg: Arg, args: dict[str, CMDArg]):
  def execute(callback: Callable[[Arg], None]):
    if callable(callback):
      callback(buildCLIArg(arg, args, title))

  return execute