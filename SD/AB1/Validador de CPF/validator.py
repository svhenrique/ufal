"""
- Esse script para validar CPF foi construido de acordo com o algoritmo utilizado pela Receita Federal. 
- É verificado se o formato do CPF estaria correto, mas não significa que ele exista ou não.
- Link explicando o algoritmo: http://cpfgenerator.com.br/calculo-cpf.html  
"""
def calcular_valores(digitos):
    total = 0

    # script para calcular valores (segundo algoritmo)
    multiplicador = len(digitos) + 1
    for valor in digitos:
        total += (int(valor) * multiplicador)
        multiplicador -= 1

    resto = total%11 # 11 é o número exigido pelo algoritmo

    return resto

def calcular_digito_verificador(digitos):
    resto = calcular_valores(digitos)
    resultado  = 11 - resto
    digito_verificador = resultado if resultado <= 9 else 0
    return digito_verificador

def validar_primeiro_digito_verificador(cpf):
    primeiro_digito = calcular_digito_verificador(cpf[:9])
    return primeiro_digito == int(cpf[-2])

def validar_segundo_digito_verificador(cpf):

    segundo_digito = calcular_digito_verificador(cpf[:10])
    return segundo_digito == int(cpf[-1])

def verificar_estrutura(cpf):
    """
        Aceita apenas números 
        Aceita apenas 11 digitos
    """    

    if cpf.isnumeric() and len(cpf) == 11:
        return True
    return False 

def validar_cpf(cpf):
    if verificar_estrutura(cpf) and validar_primeiro_digito_verificador(cpf) and validar_segundo_digito_verificador(cpf):
        return True
    return False
    
    

   

    
    
