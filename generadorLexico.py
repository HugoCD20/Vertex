import ply.lex as lex

# Lista de tokens
tokens = (
    'OP_RELACIONAL',
    'OP_ARITMETICO',
    'OP_ASIGNACION',
    'OP_LOGICO',
    'OP_UNITARIO',
    'IDENTIFICADORES',
    'PALABRARESERVADA',
    'LITERALES',
    'DELIMITADOR',
    'COMENTARIO',
    'CARACTERESPECIAL'
)

# Palabras reservadas
reservadas = {
    'var': 'PALABRARESERVADA',
    'cons': 'PALABRARESERVADA',
    'ninguno': 'PALABRARESERVADA',
    'romper': 'PALABRARESERVADA',
    'siguiente': 'PALABRARESERVADA',
    'funcion': 'PALABRARESERVADA',
    'entonces': 'PALABRARESERVADA',
    'excepto': 'PALABRARESERVADA',
    'para': 'PALABRARESERVADA',
    'si': 'PALABRARESERVADA',
    'en': 'PALABRARESERVADA',
    'regresar': 'PALABRARESERVADA',
    'intentar': 'PALABRARESERVADA',
    'mientras': 'PALABRARESERVADA',
    'mayusculas': 'PALABRARESERVADA',
    'minusculas': 'PALABRARESERVADA',
    'dividir': 'PALABRARESERVADA',
    'unir': 'PALABRARESERVADA',
    'agregar': 'PALABRARESERVADA',
    'insertar': 'PALABRARESERVADA',
    'eliminar': 'PALABRARESERVADA',
    'sacar': 'PALABRARESERVADA',
    'ordenar': 'PALABRARESERVADA',
    'invertir': 'PALABRARESERVADA',
    'tamanio': 'PALABRARESERVADA',
    'claves': 'PALABRARESERVADA',
    'valores': 'PALABRARESERVADA',
    'elementos': 'PALABRARESERVADA',
    'obtener': 'PALABRARESERVADA',
    'actualizar': 'PALABRARESERVADA',
    'imprimir': 'PALABRARESERVADA',
    'entrada': 'PALABRARESERVADA',
    'abrir': 'PALABRARESERVADA',
    'redondear': 'PALABRARESERVADA',
    'minimo': 'PALABRARESERVADA',
    'maximo': 'PALABRARESERVADA',
    'leer': 'PALABRARESERVADA',
    'leerlinea': 'PALABRARESERVADA',
    'escribir': 'PALABRARESERVADA',
    'cerrar': 'PALABRARESERVADA'
}
#comentarios
def t_COMENTARIO(t):
    r'//.*'
    return t
#literales
def t_LITERALES(t):
    r'(verdadero|falso)|\d+(\.\d+)?|".*?"|\'.*?\''
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

def t_OP_ARITMETICO(t):
    r'\*\*|\+|\-|\*|/|%'
    return t

def t_OP_LOGICO(t):
    r'YY|OO|NO'
    return t

def t_CARACTERESPECIAL(t):
    r'\.'
    return t

def t_DELIMITADOR(t):
    r'[\(\)\{\}\[\]\;\:\,]'
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

# Leer archivo
with open('lenguaje.txt', 'r') as leer:
    data = leer.read()

lexer.input(data)

# Imprimir tokens
for tok in lexer:
    print(tok)
