import typer
import os
import templates
import subprocess

app = typer.Typer()

@app.command()
def create(
  name: str, 
  path: str = os.path.join('src', 'components')
):
  # relative path to the directory of the component
  path_to_component = os.path.join(path, name)
  
  try:
    # absolute path to the directory of the component
    abs_component_path = os.path.join(os.getcwd(), path_to_component)
    
    # create the directory of the component
    os.makedirs(abs_component_path)
    
    # create code files
    os.chdir(abs_component_path)
    typescript_file = open(f'{name}.tsx', 'x')
    css_file = open(f'{name}.module.css', 'x')
    
    # write the templates to the files
    typescript_file.write(templates.ts(name))
    css_file.write(templates.css(name))
    
  except FileExistsError:
    # handle error
    print('This component is already exists')
  

@app.command()
def remove(
  name: str, 
  path: str = os.path.join('src', 'components')
):
  os.chdir(os.path.join(os.getcwd(), path))
  subprocess.run('rm -rf ' + name)

if __name__ == '__main__':
  app()