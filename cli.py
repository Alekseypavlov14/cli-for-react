import typer
import os
import templates

app = typer.Typer()

@app.command()
def create(name: str, path: str = os.path.join('src', 'components')):
  path_to_component = os.path.join(path, name)
  
  try:
    os.makedirs(os.path.join(os.getcwd(), path_to_component))
    
    typescript_file = open(os.path.join(path_to_component, name + '.tsx'), 'x')
    css_file = open(os.path.join(path_to_component, name + '.module.css'), 'x')
    
    typescript_file.write(templates.ts(name))
    css_file.write(templates.css(name))
  except FileExistsError:
    print('This component is already exists')
  

@app.command()
def mkdir(name: str):
  os.makedirs(os.path.join(name, name))

if __name__ == '__main__':
  app()