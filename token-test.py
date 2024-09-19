# Definiamo i gettoni: forma, dimensioni e colori
class Token:
    def __init__(self, shape, size, color):
        self.shape = shape
        self.size = size
        self.color = color

# Creiamo i gettoni (6 colori e 2 forme, quadrati e cerchi)
tokens = [
    Token("circle", "big", "red"),
    Token("circle", "big", "green"),
    Token("circle", "big", "white"),
    Token("circle", "small", "red"),
    Token("circle", "small", "green"),
    Token("square", "big", "red"),
    Token("square", "big", "green"),
    Token("square", "big", "white"),
    Token("square", "small", "red"),
    Token("square", "small", "green")
]

# Funzione per trovare un gettone specifico
def find_token(shape=None, size=None, color=None):
    for token in tokens:
        if (shape is None or token.shape == shape) and \
           (size is None or token.size == size) and \
           (color is None or token.color == color):
            return token
    return None

# Funzione per eseguire un ordine e ricevere la risposta dal paziente
def give_instruction(instruction, shape=None, size=None, color=None):
    print(instruction)
    response = input("Tocca un gettone: (colore, forma, dimensione): ").lower()
    expected_token = find_token(shape, size, color)
    
    # Verifichiamo la risposta
    if expected_token and response == f"{expected_token.color} {expected_token.shape} {expected_token.size}":
        print("Corretto!")
    else:
        print("Sbagliato, prova di nuovo")

# Esecuzione delle consegne
def execute_token_test():
    # Parte I: con tutti i gettoni
    give_instruction("Tocca uno rosso", color="red")
    give_instruction("Tocca uno verde", color="green")
    give_instruction("Tocca uno bianco", color="white")

    # Parte II: solo gettoni grandi
    give_instruction("Tocca il cerchio verde", shape="circle", size="big", color="green")
    
    # Parte III: con tutti i gettoni
    give_instruction("Tocca il cerchio bianco", shape="circle", color="white")
    give_instruction("Tocca il quadrato verde", shape="square", color="green")
    give_instruction("Tocca il cerchio nero", shape="circle", color="black")

    # Parte IV: solo gettoni grandi
    give_instruction("Tocca il cerchio rosso e il quadrato verde", shape="circle", size="big", color="red")
    give_instruction("Tocca il cerchio bianco e il quadrato rosso", shape="circle", size="big", color="white")

    # Continua con le altre parti del test...

# Avviamo il test
if __name__ == "__main__":
    execute_token_test()
