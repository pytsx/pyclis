import sys 

from pathlib import Path 
from prompt_toolkit.shortcuts import radiolist_dialog

from pyclis.utils import create_dir

def select(in_dir: Path) -> Path: 
  projects_dir = create_dir(in_dir / "projects")

  project_path=radiolist_dialog(
    title="selecione um projeto",
    values=[[project, project.name] for project in projects_dir.iterdir() if project.is_dir()]
  ).run()
  
  if not project_path:
    sys.exit(1)
  return project_path
