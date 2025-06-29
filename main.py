# linked list

# class pour un node donc un elt
class Node:
    def __init__(self, data=None, next=None):
        self.data = data # elt exemple un chiffre
        self.next = next # pointeur vers le prochain elt

class LinkedList:
    def __init__(self):
        self.head = None # la tête de notre list

    def insert_at_begining(self, data):
        node = Node(data, self.head) # on créer un node avec notre elt soit data et self.head qui est notre pointeur soit next
        # donc notre prochain elt du node sera notre current head
        self.head = node # maintenant notre head c'est le node qu'on vient de créer
    
    def print_list(self):
        # dans le cas où notre head est null donc vide c'est que la liste n'existe pas
        if self.head is None:
            print("Liste vide")
            return
        temp = self.head
        result = ""
        while temp:
            # ajoute la données de notre node dans une var
            result += str(temp.data) + '->'
            # fait avancer notre node
            temp = temp.next
        print(result)
        
    # il a pas de next donc on dit none
    def insert_at_end(self, data):
        # si on call cette methode quand la liste est vide
        if self.head is None:
            # on dit que la head est vide
            self.head = None(data, None)
            return
        
        # on va a la head et on avance pour arriver a la limite qui est la fin de la liste
        temp = self.head
        while temp.next:
            temp = temp.next
        # quand on est arriver a la fin de la liste chaine le next sera node data, None (car fin donc pas de next)
        temp.next = (data, None)


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_begining(1)
    ll.insert_at_begining(2)
    ll.insert_at_end(10)
    ll.print_list()