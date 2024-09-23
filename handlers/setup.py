from pathlib import Path 
import sys 
from pyclis.utils import files_from_dict, construct_bat_script

def setup(in_dir: Path):
  files_from_dict(in_dir, {
    'atuaizar.bat': construct_bat_script("--i %~dp0 --up true"), 
    'criar.bat': construct_bat_script('--i %~dp0'), 
    'executar.bat': construct_bat_script('--i %~dp0 --exec true')
  })
  sys.exit(1)