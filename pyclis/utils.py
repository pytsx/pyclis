import os, json
from pathlib import Path

def files_from_dict(dir: Path, data: dict[str, str | dict]):
  for file, content in data.items(): 
    path = Path(dir / file)
    if path.suffix == ".json":
      with open(path, "w") as f:
        json.dump(content, f, indent=4)
    else:
     path.write_text(content)

def get_root_path() -> Path:
  return Path(os.getcwd()).absolute()

def create_dir(path: Path) -> Path:
  path.parent.mkdir(exist_ok=True, parents=True)
  path.mkdir(exist_ok=True, parents=True)
  return path

root = get_root_path()

def construct_bat_script(args: str) -> str:
  """
    @echo off
    cd {root}
    python . {args}
  """
  return f"@echo off\ncd {root}\npython . {args}"


def get_projects_dir(in_dir: Path) -> Path: 
  return create_dir(
    in_dir / 
    "projects"
  )

def get_project_path(in_dir: Path, project_name: str) -> Path:
  return create_dir(get_projects_dir(in_dir) / project_name)

def normalize_schema_path(path: Path) -> str:
    """
    Args:
        path (Path): O caminho completo do schema.
    
    Returns:
        str: O caminho normalizado sem driver.
    """
    return "/" + os.path.relpath(path, path.anchor).replace("\\", "/")