# Codificador Zenit Polar
correspondencias = {
    'Z': 'P',
    'E': 'O',
    'N': 'L',
    'I': 'A',
    'T': 'R',
    'P': 'Z',
    'O': 'E',
    'L': 'N',
    'A': 'I',
    'R': 'T'
}

text = str(input("Digite o text a ser convertido: "))
text = text.upper()
lista = list(text)
result = ""

for letra in lista:
    if letra in correspondencias:
        converted = correspondencias[letra]
        result = result + converted
    else:
        result = result + letra        
    
print(result)
