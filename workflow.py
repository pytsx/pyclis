from interface import Arg
from handlers import (
  create,
  execute,
  select,
  setup,
  update
)

def workflow(arg: Arg):
  if arg.mode == "setup":
    setup(arg.in_dir)

  if arg.in_dir_len() == 0 and arg.mode != "create":
    project_dir = create(arg.in_dir)
    update(project_dir)
    arg.project_dir = project_dir

  match arg.mode:
    case "create":
      project_dir = create(arg.in_dir)
      if project_dir:
        update(project_dir)
    case "update":
      if arg.project_dir:
        update(arg.project_dir)
      else: 
        update(select(arg.in_dir))
    case "execute":
      if arg.project_dir:
        execute(arg.project_dir)
      else:
        execute(select(arg.in_dir)) 
