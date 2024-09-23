import argparse
from pyclis.interface import IArg, CMDArg

class CLI: 
  def __init__(self, values: dict[str, CMDArg], title: str):
    self.parser = self.add_arguments(argparse.ArgumentParser(description=title), values)

  def get_arg(self, cls) -> IArg:
    args = self.parser.parse_args()
    return cls(args) if issubclass(cls, IArg) else IArg(args)
  
  def add_arguments(self, parser: argparse.ArgumentParser, values: dict[str, CMDArg]) -> argparse.ArgumentParser:
    for cmd, content in values.items():
      parser.add_argument(
        cmd, 
        **{key: value for key, value in content.items() if key in ["type", "required", "help"]},
        default=False if isinstance(content["type"], bool) else None
      )
    return parser
  
def buildCLIArg(cls, values: dict[str, CMDArg], title: str) -> IArg:
  return CLI(values, title).get_arg(cls)
