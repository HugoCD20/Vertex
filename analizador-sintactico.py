import ply.yacc as yacc
from generadorLexico import tokens, lexer  

def p_programa(p):
    '''programa : sentencia_sent'''
    p[0] = {'tipo': 'programa', 'contenido': p[1]}

def p_sentencia_sent(p):
    '''sentencia_sent : sent_linea P_COMA sentencia_sent
                      | sentencia sentencia_sent
                      | '''
    if len(p) == 4:  # sent_linea ; sentencia_sent
        if p[3] is None:
            p[0] = [p[1]]
        else:
            p[0] = [p[1]] + p[3]
    elif len(p) == 3:  # sentencia sentencia_sent
        if p[2] is None:
            p[0] = [p[1]]
        else:
            p[0] = [p[1]] + p[2]
    else:  # épsilon (regla vacía)
        p[0] = []

def p_sent_linea(p):
    '''sent_linea : declarar_var
                  | declarar_cons
                  | asignacion
                  | inst_fun
                  | metodo'''
    p[0] = p[1]

def p_sentencia(p):
    '''sentencia : sent_if
                 | sent_for
                 | sent_while
                 | sent_fun
                 | sent_try'''
    p[0] = p[1]

def p_declarar_var(p):
    '''declarar_var : VAR IDENTIFICADORES
                    | VAR IDENTIFICADORES OP_ASIGNACION valor'''
    if len(p)==3:
        p[0]={'tipo':'declarar_var','id':p[2]}
    else:
        p[0]={'tipo':'declarar_var','id':p[2],'valor':p[4]}

def p_valor(p):
    '''valor : expresion
            | estructura_datos 
            | metodo
            | IDENTIFICADORES'''
    p[0]=p[1]
def p_expresion(p):
    '''expresion : termino exp_e'''
    p[0]=p[1]

def p_termino(p):
    '''termino : factor term_ext'''
    p[0]=p[1]

def p_factor(p):
    '''factor : selec_dato
             | A_PARENTESIS expresion C_PARENTESIS'''
    if len(p)==2:
        p[0]=p[1]
    else:
        p[0]=p[2]
def p_selec_dato(p):
    '''selec_dato : IDENTIFICADORES
                 | LITERALES'''
    p[0]=p[1]
    
def p_term_ext(p):
    '''term_ext : OP_MULTIPLICATIVO factor term_ext
               | '''
    if len(p)>1:
        p[0]={'tipo':'term_ext','factor':p[2],'term_ext':p[3]}
    else:
        p[0]=None
def p_exp_e(p):
    '''exp_e : OP_ARITMETICO termino exp_e
            | '''
    if len(p)>1:
        p[0]={'tipo':'exp_e','termino':p[2],'exp_e':p[3]}
    else:
        p[0]=None
    
def p_estructura_datos(p):
    '''estructura_datos : lista
                       | tupla
                       | diccionario'''
    p[0]=p[1]

def p_lista(p):
    '''lista : A_CORCHETE dato dato_extra C_CORCHETE
            | A_CORCHETE C_CORCHETE'''
    if len(p)==1:
        p[0]={'tipo':'lista','dato':p[2],'dato_extra':p[3]}
    else:
        p[0]=None

def p_tupla(p):
    '''tupla : A_PARENTESIS dato dato_extra C_PARENTESIS'''
    p[0]={'tipo':'tupla','dato':p[2],'dato_extra':p[3]}

def p_dato_extra(p):
    '''dato_extra : COMA dato dato_extra
                 | '''
    if len(p)>1:
        p[0]={'tipo':'dato_extra','dato':p[2],'dato_extra':p[3]}
    else:
        p[0]=None
        
def p_diccionario(p):
    '''diccionario : A_LLAVE LITERALES DOS_P dato element_ext C_LLAVE
                  | A_LLAVE C_LLAVE'''
    if len(p)==7:
        p[0]={'tipo':'diccionario','dato':p[4],'element_ext':p[5]}
    else:
        p[0]=None

def p_element_ext(p):
    '''element_ext : COMA LITERALES DOS_P dato element_ext
                 | '''
    if len(p)>1:
        p[0]={'tipo':'element-ext','dato':p[4],'element_ext':p[5]}
    else:
        p[0]=None

def p_dato(p):
    '''dato : IDENTIFICADORES
           | LITERALES
           | expresion'''
    if p[1]=='expresion':
        p[0]=p[1]
    else:
        p[0]=None
def p_asignacion(p):
    '''asignacion : IDENTIFICADORES OP_ASIGNACION valor'''
    p[0]=p[3]

def p_declarar_cons(p):
    '''declarar_cons : CONS IDENTIFICADORES OP_ASIGNACION LITERALES'''
    p[0]=None

def p_inst_fun(p):
    '''inst_fun : IDENTIFICADORES A_PARENTESIS atributo C_PARENTESIS'''
    p[0]=p[3]

def p_atributo(p):
    '''atributo : IDENTIFICADORES atributo_dos
                | LITERALES atributo_dos
                | '''
    if len(p)>1:
        p[0]=p[2]
    else:
        p[0]=None

def p_atributo_dos(p):
    '''atributo_dos : COMA IDENTIFICADORES  atributo_dos
                    | COMA LITERALES atributo_dos
                    | '''
    if len(p)>1:
        p[0]=p[3]
    else:
        p[0]=None

def p_metodo(p):
    '''metodo : PUNTO METODO A_PARENTESIS atributo C_PARENTESIS
              | METODO A_PARENTESIS atributo C_PARENTESIS'''
    if len(p)==5:
        p[0]=p[4]
    else:
        p[0]=p[3]

def p_sent_if(p):
    '''sent_if : SI A_PARENTESIS exp_comparacion C_PARENTESIS A_LLAVE sentencia_sent C_LLAVE sent_else'''
    p[0]={'tipo':'sent_if','exp_comparacion':p[3],'sentencia_sent':p[5],'sent_else':p[7]}

def p_exp_comparacion(p):
    '''exp_comparacion : dato OP_RELACIONAL dato exp_ext
                       | LITERALES'''
    if len(p)>2:
        p[0]={'tipo': 'exp_comparacion', 'dato':p[1],'dato':p[3],'exp_ext':p[4]}
    else:
        p[0]=p[1]

def p_exp_ext(p):
    '''exp_ext : OP_LOGICO exp_comparacion 
               | '''
    if len(p)>1:
        p[0]=p[2]
    else:
        p[0]=None

def p_sent_else(p):
    '''sent_else : ENTONCES A_LLAVE sentencia_sent C_LLAVE 
                 | '''
    if len(p)>1:
        p[0]=p[3]
    else:
        p[0]=None

def p_sent_for(p):
    '''sent_for : PARA A_PARENTESIS declarar_var P_COMA expresion_comp P_COMA incremento C_PARENTESIS A_LLAVE sentencia_sent C_LLAVE'''
    p[0]={'tipo': 'sent_for','declarar_var':p[2],'expresion_comp':p[4],'incremento':p[6],'sentencia_sent':p[8]}

def p_expresion_comp(p):
    '''expresion_comp : IDENTIFICADORES OP_RELACIONAL dato'''
    p[0]=p[3]

def p_incremento(p):
    '''incremento : op_incremento_simple
                  | asignacion_expr'''
    p[0]=p[1]

def p_op_incremento_simple(p):
    '''op_incremento_simple : IDENTIFICADORES OP_UNITARIO'''
    p[0]=None
    
def p_asignacion_expr(p):
    '''asignacion_expr : IDENTIFICADORES OP_ASIGNACION expresion'''
    p[0]=p[3] 

def p_sent_while(p):
    '''sent_while : MIENTRAS A_PARENTESIS exp_comparacion C_PARENTESIS A_LLAVE sentencia_sent C_LLAVE'''
    p[0]={'tipo':'sent_while','exp_comparacion':p[3],'sentencia_sent':p[5]}

def p_sent_fun(p):
    '''sent_fun : FUNCION A_PARENTESIS atributo C_PARENTESIS A_LLAVE sentencia_sent REGRESAR valor C_LLAVE
                | FUNCION A_PARENTESIS atributo C_PARENTESIS A_LLAVE sentencia_sent C_LLAVE'''
    if len(p)==10:
        p[0]={'tipo':'sent_fun','atributo':p[3],'sentencia_sent':p[5],'sent_else':p[7],'valor':p[9]}
    else:
        p[0]={'tipo':'sent_fun','atributo':p[3],'sentencia_sent':p[5],'sent_else':p[7]}

def p_sent_try(p):
    '''sent_try : INTENTAR A_LLAVE sentencia_sent C_LLAVE EXCEPTO A_LLAVE sentencia_sent C_LLAVE'''
    p[0]={'tipo':'sent_try','sentencia_sent':p[3],'sentencia_sent':p[6]}

def p_error(p):
    if p:
        print(f"Error de sintaxis en '{p.value}' (línea {p.lineno})")
    else:
        print("Error de sintaxis al final del archivo")


parser = yacc.yacc()

# Función para analizar un archivo
def analizar_archivo(archivo):
    with open(archivo, 'r') as f:
        data = f.read()
    
    resultado = parser.parse(data, lexer=lexer)
    print("\n--- Árbol Sintáctico ---")
    return resultado

# Si ejecutamos este archivo directamente
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        archivo = sys.argv[1]
    else:
        archivo = 'lenguaje.txt'  # Archivo por defecto
    
    print(f"Analizando archivo: {archivo}")
    arbol = analizar_archivo(archivo)

