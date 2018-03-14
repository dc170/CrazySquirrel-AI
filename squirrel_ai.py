# By Pablo Gay pablo.gay@udg.edu
# http://eia.udg.edu/~pgay/practiques/squirrel
#
# Released under a "Simplified BSD" license

import random

class SquirrelAI:
    '''
    Aquesta classe implementa la funcio moveSquirrel, que sera cridada per la
    iteració principal del joc en cada refresc d'imatge.
    '''

    def __init__(self):
        '''
        Constructor de la classe.
        definiu aqui les variables d'estats que volgeu guardar.
        '''
        #self.variable = valor
        pass

    def moveSquirrel(self, squirrel, other_squirrel):
        '''
        Funcio que defineix el moviment de l'esquirol en la seguent iteracio.
        Entrades:
          - squirrel: hashmap, objecte que representa al jugador. Conte les
                      seguents claus.
             * x: coordinada x en l'univers (enter)
             * y: coordinada y en l'univers (enter)
             * size: tamany d'un costat de l'esquirol (es quadrat) (enter)
             * health: vida restant (enter)
          - other_squirrels: vector, objecte que conte els altres esquirols.
                             Cada index conte un hashmap representatn un esquirol
                             amb les seguents claus.
             * id: identificador unic d'esquirol (enter)
             * x:  coordinada x en l'univers (enter)
             * y:  coordinada y en l'univers (enter)
             * movex: increment en la coordinada x (velocitat en x) (enter)
             * movey: increment en la coordinada y (velocitat en x) (enter)
             * height: alcada de l'esquirol
             * width: amplada de l'esquirol
        Sortida:
        Tupla/Vector boolea indicant les quatre components moviment:
          - (amunt, abaix, esquerra, dreta)
        '''

        movements = [False, False, False, False]
        movements[random.randint(0,3)] = True
        return movements
