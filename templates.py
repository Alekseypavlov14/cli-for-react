def ts(name: str):
  return '\n'.join([
    "import { FC } from 'react'",
    "import styles from './" + name + ".module.css'",
    "",
    "interface " + name + "Props {}",
    "",
    "export const " + name + ": FC<" + name + "Props> = () => {",
    "  return (",
    "    <div className={styles." + name + "}>",
    "      $1",			
    "    </div>",
    "  )",
    "}"
  ])
  
  
def css(name: str):
  return '\n'.join([
    name + ' {',
    ' ',
    '}'
  ])