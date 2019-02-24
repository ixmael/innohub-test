'''Obtinene la puntuación de un XML

Este programa calcula la puntuación de un documento XML que es proporcionado a
través de la entrada estándar de la línea de comandos. El formato que se espera
es que la primera línea indica el número de líneas del documento y las
siguientes líneas es el documento XML. Ejemplo de entrada:
    5
    <xml>
        <tag></tag>
        <tag />
        <tag></tag>
    </xml>

Example:
    python calculate_score.py
    cat archivo.txt | python calculate_score.py
'''

state = ''

def get_score(xml_string):
    '''Obtiene la puntuación de una cadena XML.

    Args:
        xml_string (str): cadena xml.
    
    Returns:
        int: el total de atributos en la cadena xml.
    '''
    global state
    
    score = 0
    count_limiters = 0
    for c in xml_string:
        if state == 'open' and c == '/':
            state = 'end_tag'
            continue
        
        if c == '<':
            state = 'open'
            continue
        
        if c == '>':
            if state == 'attr':
                score += 1
            
            if state == 'end_tag':
                state = ''
            else:
                state = 'content'
            
            continue
        
        if (state == 'open' or state == 'separator' ) and c == ' ':
            state = 'separator'
            continue
        
        if state == 'separator' and c != ' ':
            state = 'attr'
            continue
        
        if state == 'attr' and c == ' ':
            score += 1
            state = 'separator'
            continue
        
        if state == 'attr' and (c.isdigit() or c.isalpha()):
            continue

    return score

if __name__ == "__main__":
    lines_input = input()
    
    lines = 0
    try:
        lines = int(lines_input)
    except:
        print("Debe proporcionar el número de líneas del documento XML")
        sys.exit(0)
    
    score = 0
    document = []
    while (lines > 0):
      xml_line = input()
      score += get_score(xml_line)
      lines -= 1
    
    print(score)
    
