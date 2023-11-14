class Pokenea:
    def __init__(self, id, nombre, altura, habilidad, imagen_url, frase_filosofica):
        self.id = id
        self.nombre = nombre
        self.altura = altura
        self.habilidad = habilidad
        self.imagen_url = imagen_url
        self.frase_filosofica = frase_filosofica

# Lista de Pokeneas
pokeneas = [
    Pokenea(1, 'Pikachu', 0.4, 'Electricidad', 'https://storage.googleapis.com/flask_pokeneas/1.png', 'La electricidad fluye como la vida misma.'),
    Pokenea(2, 'Bulbasaur', 0.7, 'Planta/Veneno', 'https://storage.googleapis.com/flask_pokeneas/10.png', 'En la dualidad de la naturaleza, la planta y el veneno coexisten.'),
    Pokenea(3, 'Charizard', 1.7, 'Fuego/Volador', 'https://storage.googleapis.com/flask_pokeneas/2.png', 'El fuego que arde dentro refleja la libertad en vuelo.'),
    Pokenea(4, 'Squirtle', 0.5, 'Agua', 'https://storage.googleapis.com/flask_pokeneas/3.png', 'El agua fluye suavemente, adaptándose a su entorno con sabiduría.'),
    Pokenea(5, 'Jigglypuff', 0.5, 'Normal/Hada', 'https://storage.googleapis.com/flask_pokeneas/4.png', 'La música es la expresión del alma, al igual que el canto de Jigglypuff.'),
    Pokenea(6, 'Mewtwo', 2.0, 'Psíquico', 'https://storage.googleapis.com/flask_pokeneas/5.png', 'En la mente se encuentra el poder que trasciende los límites del cuerpo.'),
    Pokenea(7, 'Gyarados', 6.5, 'Agua/Volador', 'https://storage.googleapis.com/flask_pokeneas/6.png', 'La ira convertida en fuerza, un Gyarados surge de las aguas turbulentas.'),
    Pokenea(8, 'Eevee', 0.3, 'Normal', 'https://storage.googleapis.com/flask_pokeneas/7.png', 'La versatilidad de Eevee refleja las múltiples facetas de la vida.'),
    Pokenea(9, 'Machamp', 1.6, 'Lucha', 'https://storage.googleapis.com/flask_pokeneas/8.png', 'La fuerza en la disciplina del entrenamiento, un Machamp domina con honor.'),
    Pokenea(10, 'Gengar', 1.5, 'Fantasma/Veneno', 'https://storage.googleapis.com/flask_pokeneas/9.png', 'En las sombras, Gengar acecha, recordándonos la dualidad de la luz y la oscuridad.'),
]