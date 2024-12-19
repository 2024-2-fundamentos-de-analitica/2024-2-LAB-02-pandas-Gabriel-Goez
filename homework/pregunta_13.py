"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""

import pandas as pd


PATH_0 = 'files/input/tbl0.tsv'
PATH_1 = 'files/input/tbl1.tsv'
PATH_2 = 'files/input/tbl2.tsv'

def pregunta_13():
    """
    Si la columna `c0` es la clave en los archivos `tbl0.tsv` y `tbl2.tsv`,
    compute la suma de `tbl2.c5b` por cada valor en `tbl0.c1`.

    Rta/
    c1
    A    146
    B    134
    C     81
    D    112
    E    275
    Name: c5b, dtype: int64
    """

    df_0 = pd.read_csv(PATH_0, sep = '\t')
    df_2 = pd.read_csv(PATH_2, sep = '\t') 

    df = pd.DataFrame(df_2.groupby('c0')['c5b'].sum())

    clave = pd.DataFrame(df_0.groupby('c1')['c0'].apply(list))
    clave = clave.explode('c0')
    clave = clave.reset_index().set_index('c0')
    
    resultado = df.join(clave)

    return resultado.groupby('c1')['c5b'].sum()

print(pregunta_13())