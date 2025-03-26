class Palavra:  # Definir a palavra
    descricao: str

    def __init__(self, descricao):
        self.descricao = descricao

    def __str__(self):
        return self.descricao
    
