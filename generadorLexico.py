import ply.lex as lex

# Lista de tokens
tokens = (
    'OP_RELACIONAL', 'OP_ARITMETICO', 'OP_MULTIPLICATIVO', 'OP_ASIGNACION', 
    'OP_LOGICO', 'OP_UNITARIO', 'IDENTIFICADORES', 'LITERALES',
    'COMENTARIO', 'VAR', 'CONS', 'METODO', 
    'FUNCION', 'ENTONCES', 'EXCEPTO', 'PARA', 'SI',
    'REGRESAR', 'INTENTAR', 'MIENTRAS','A_PARENTESIS','C_PARENTESIS','A_CORCHETE',
    'C_CORCHETE','A_LLAVE','C_LLAVE','P_COMA','DOS_P','COMA','PUNTO'
)

# Diccionario de palabras reservadas con sus tokens específicos
reservadas = {
    'var': 'VAR',
    'cons': 'CONS',
    'romper': 'METODO',
    'siguiente': 'METODO',
    'funcion': 'FUNCION',
    'entonces': 'ENTONCES',
    'excepto': 'EXCEPTO',
    'para': 'PARA',
    'si': 'SI',
    'en': 'METODO',
    'regresar': 'REGRESAR',
    'intentar': 'INTENTAR',
    'mientras': 'MIENTRAS',
    'mayusculas': 'METODO',
    'minusculas': 'METODO',
    'dividir': 'METODO',
    'unir': 'METODO',
    'agregar': 'METODO',
    'insertar': 'METODO',
    'eliminar': 'METODO',
    'sacar': 'METODO',
    'ordenar': 'METODO',
    'invertir': 'METODO',
    'tamanio': 'METODO',
    'claves': 'METODO',
    'valores': 'METODO',
    'elementos': 'METODO',
    'obtener': 'METODO',
    'actualizar': 'METODO',
    'imprimir': 'METODO',
    'entrada': 'METODO',
    'abrir': 'METODO',
    'redondear': 'METODO',
    'minimo': 'METODO',
    'maximo': 'MAXIMO',
    'leer': 'METODO',
    'leerlinea': 'METODO',
    'escribir': 'METODO',
    'cerrar': 'METODO'
}
t_A_PARENTESIS=r'\('
t_C_PARENTESIS=r'\)'
t_A_LLAVE=r'\{'
t_C_LLAVE=r'\}'
t_A_CORCHETE=r'\['
t_C_CORCHETE=r'\]'
t_P_COMA=r';'
t_DOS_P=r':'
t_COMA=r','
t_PUNTO=r'\.'
#comentarios
def t_COMENTARIO(t):
    r'//.*'
    return t
#literales
def t_LITERALES(t):
    r'(verdadero|falso|ninguno)|\d+(\.\d+)?|".*?"|\'.*?\''
    return t

# OPERADORES
def t_OP_RELACIONAL(t):
    r'==|<=|>=|<|>|!='
    return t

def t_OP_UNITARIO(t):
    r'\+\+|--'
    return t

def t_OP_ASIGNACION(t):
    r'\+=|-=|\*=|/=|%=|='
    return t

def t_OP_MULTIPLICATIVO(t):
    r'\*\*|\*|/|%'
    return t

def t_OP_ARITMETICO(t):
    r'\+|\-'
    return t

def t_OP_LOGICO(t):
    r'YY|OO|NO'
    return t

def t_CARACTERESPECIAL(t):
    r'\.'
    return t


# Identificadores y palabras reservadas
def t_IDENTIFICADORES(t):
    r'[a-z][a-zA-Z0-9]*'
    if t.value in reservadas:
        t.type = reservadas[t.value]
    return t

# Ignorar espacios y saltos de línea
t_ignore = ' \t\r\n'

# Errores
def t_error(t):
    print(f"Carácter ilegal: '{t.value[0]}'")
    t.lexer.skip(1)

# Crear lexer
lexer = lex.lex()