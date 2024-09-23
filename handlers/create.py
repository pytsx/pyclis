from pathlib import Path 

from pyclis.utils import(
  files_from_dict, 
  construct_bat_script, 
  get_project_path, 
  create_dir, 
  get_root_path, 
  normalize_schema_path
)

def create(in_dir: Path) -> Path:
  project_name = input("informe o nome do projeto: ")
  project_path = get_project_path(in_dir, project_name)

  files_from_dict(project_path, {
    "executa.bat": construct_bat_script(f"--i {in_dir} --p %~dp0 --exec true"),
    "config.json": {
      "$schema": normalize_schema_path(create_dir(get_root_path() / "schemas") / "schema.json")
    }
  })

  return project_path
