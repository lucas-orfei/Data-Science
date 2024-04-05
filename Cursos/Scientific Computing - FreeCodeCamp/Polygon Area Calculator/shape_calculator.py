class Rectangle:

# Um método que inicia o objeto retângulo

    def __init__(self, width, height):
        self.width = width
        self.height = height

# Um método que retorna uma string pedida

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

# Um método que define a largura

    def set_width(self, width):
        self.width = width

# Um método que define a altura
        
    def set_height(self, height):
        self.height = height
    
# Um método que retorna a área do retângulo

    def get_area(self):
        return self.width * self.height

# Um método que retorna o parâmetro do retângulo

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

# Um método que retorna a diagonal do retângulo

    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** .5)

# Um método que retorna uma figura do retângulo

    def get_picture(self):
        if(self.width > 50 or self.height >50):
            return "Too big for picture."
        string = (("*"*self.width) + "\n") * self.height
        return string

# Um método que retorna quantas figuras podem ser repetidas dentro do retângulo

    def get_amount_inside(self, shape):
        return int(self.get_area()/shape.get_area())
    
class Square(Rectangle):

# Um método que inicia o objeto quadrado

    def __init__(self, side):
        self.width = side
        self.height = side

# Um método que retorna uma string pedida

    def __str__(self):
        return f'Square(side={self.width})'

# Um método que define a largura e a altura do quadrado

    def set_side(self,side):
        self.width = side
        self.height = side
