import ply.lex as lex

# Definición de tokens
tokens = (
    # OPERADORES ARITMETICOS
    'OP_SUMA',
    'OP_RESTA',
    'OP_MULTIPLICA',
    'OP_DIVIDE',
    'OP_MODULO',
    'OP_POTENCIA',
    # OPERADORES DE ASIGNACION
    'OP_ASIGNACION',
    'OP_ASUMA',
    'OP_ARESTA',
    'OP_AMULTIPLICA',
    'OP_ADIVIDE',
    'OP_AMODULO',
    # OPERADORES RELACIONALES O DE COMPARACION
    'OP_RIGUAL',
    'OP_RMENORIGUAL',
    'OP_RMAYORIGUAL',
    'OP_RMENOR',
    'OP_RMAYOR',
    'OP_RDIFERENTE',
    # OPERADORES LOGICOS
    'OP_AND',
    'OP_OR',
    'OP_NOT',
    #OPERADORES UNITARIOS
    'OP_UINCREMENTO',
    'OP_UDECREMENTO',
    # IDENTIFICADORES
    'IDENTIFICADORES',
    # PALABRAS RESERVADAS
    'P_VAR',
    'P_CONS',
    'P_FALSO',
    'P_VERDADERO',
    'P_NINGUNO',
    'P_ROMPER',
    'P_SIGUIENTE',
    'P_FUNCION',
    'P_ENTONCESSI',
    'P_ENTONCES',
    'P_EXCEPTO',
    'P_PARA',
    'P_SI',
    'P_EN',
    'P_REGRESAR',
    'P_INTENTAR',
    'P_MIENTRAS',
    'P_MAYUSCULAS',
    'P_MINUSCULAS',
    'P_DIVIDIR',
    'P_UNIR',
    'P_AGREGAR',
    'P_INSERTAR',
    'P_ELIMINAR',
    'P_SACAR',
    'P_ORDENAR',
    'P_INVERTIR',
    'P_TAMANIO',
    'P_CLAVES',
    'P_VALORES',
    'P_ELEMENTOS',
    'P_OBTENER',
    'P_ACTUALIZAR',
    'P_IMPRIMIR',
    'P_ENTRADA',
    'P_ABRIR',
    'P_REDONDEAR',
    'P_MINIMO',
    'P_MAXIMO',
    'P_LEER',
    'P_LEERLINEA',
    'P_ESCRIBIR',
    'P_CERRAR',
    #LITERALES
    'LITERALES',
    #DELIMITADORES
    'D_APARENTESIS',
    'D_CPARENTESIS',
    'D_ALLAVE',
    'D_CLLAVE',
    'D_ACORCHETE',
    'D_CCORCHETE',
    'D_PUNTOYCOMA',
    'D_COMA',
    #COMENTARIOS
    'COMENTARIO'

)

# PALABRAS RESERVADAS
reservadas = {
    'var': 'P_VAR',
    'cons': 'P_CONS',
    'falso': 'P_FALSO',
    'verdadero': 'P_VERDADERO',
    'ninguno': 'P_NINGUNO',
    'romper': 'P_ROMPER',
    'siguiente': 'P_SIGUIENTE',
    'funcion': 'P_FUNCION',
    'entonces': 'P_ENTONCES',
    'excepto': 'P_EXCEPTO',
    'para': 'P_PARA',
    'si': 'P_SI',
    'en': 'P_EN',
    'regresar': 'P_REGRESAR',
    'intentar': 'P_INTENTAR',
    'mientras': 'P_MIENTRAS',
    'mayusculas': 'P_MAYUSCULAS',
    'minusculas': 'P_MINUSCULAS',
    'dividir': 'P_DIVIDIR',
    'unir': 'P_UNIR',
    'agregar': 'P_AGREGAR',
    'insertar': 'P_INSERTAR',
    'eliminar': 'P_ELIMINAR',
    'sacar': 'P_SACAR',
    'ordenar': 'P_ORDENAR',
    'invertir': 'P_INVERTIR',
    'tamanio': 'P_TAMANIO',
    'claves': 'P_CLAVES',
    'valores': 'P_VALORES',
    'elementos': 'P_ELEMENTOS',
    'obtener': 'P_OBTENER',
    'actualizar': 'P_ACTUALIZAR',
    'imprimir': 'P_IMPRIMIR',
    'entrada': 'P_ENTRADA',
    'abrir': 'P_ABRIR',
    'redondear': 'P_REDONDEAR',
    'minimo': 'P_MINIMO',
    'maximo': 'P_MAXIMO',
    'leer': 'P_LEER',
    'leerlinea': 'P_LEERLINEA',
    'escribir': 'P_ESCRIBIR',
    'cerrar': 'P_CERRAR'
}

# OPERADORES ARITMETICOS
t_OP_SUMA = r'\+'
t_OP_RESTA = r'-'
t_OP_MULTIPLICA = r'\*'
t_OP_DIVIDE = r'/'
t_OP_MODULO = r'%'
t_OP_POTENCIA = r'\*\*'

# OPERADORES DE ASIGNACION
t_OP_ASIGNACION = r'='
t_OP_ASUMA = r'\+='
t_OP_ARESTA = r'-='
t_OP_AMULTIPLICA = r'\*='
t_OP_ADIVIDE = r'/='
t_OP_AMODULO = r'%='

# OPERADORES RELACIONALES O DE COMPARACION
t_OP_RIGUAL = r'=='
t_OP_RMENORIGUAL = r'<='
t_OP_RMAYORIGUAL = r'>='
t_OP_RMENOR = r'<'
t_OP_RMAYOR = r'>'
t_OP_RDIFERENTE = r'!='

# OPERADORES LOGICOS
t_OP_AND = r'YY'
t_OP_OR = r'OO'
t_OP_NOT = r'NO'

#OPERADORES UNITARIOS
t_OP_UINCREMENTO=r'\+\+'
t_OP_UDECREMENTO=r'--'

#DELIMITADORES O SEPARADORES
t_D_APARENTESIS=r'\('
t_D_CPARENTESIS=r'\)'
t_D_ALLAVE=r'{'
t_D_CLLAVE=r'}'
t_D_ACORCHETE=r'\['
t_D_CCORCHETE=r']'
t_D_PUNTOYCOMA=r';'
t_D_COMA=r','

# RECONOCER IDENTIFICADORES Y PALABRAS RESERVADAS
def t_IDENTIFICADORES(t):
    r'[a-z][a-zA-Z0-9]*' 
    if t.value in reservadas:  
        t.type = reservadas[t.value] 
    return t

#LITERALES

def t_LITERALES(t):
    r'(verdadero|falso|\d+(\.\d+)?|".*?"|\'.*?\')'
    return t

#comentario

def t_COMENTARIO(t):
    r'//.*'
    return t

# Ignorar espacios y tabulaciones
t_ignore = ' \t\n'

# Maneja errores
def t_error(t):
    print(f"Carácter ilegal '{t.value[0]}'")
    t.lexer.skip(1)

# Crear el analizador léxico
lexer = lex.lex()

# Prueba del analizador
leer=open('lenguaje.txt','r')
data=leer.read()
#data = "var x = (42 + 7) * y continuar -5.25 i-- entoncessi"
lexer.input(data)

for tok in lexer:
    print(tok)

leer.close()
