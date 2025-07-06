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

    def append(self, data):
        newnode = Node(data) # on créer un node avec notre elt soit data
        curr = self.head # on créer un var curr qui va partir de la head
        while curr.next != None: # on avance jusqu'à la fin
            curr = curr.next # on incrémente
        
        curr.next= newnode # on ajoute au suivant après le dernier le new node donc exemple 1->2-> on est arriver a 2 donc le curr.next donc celui après 2 sera le newnode
    
    def print_list(self):
        # dans le cas où notre head est null donc vide c'est que la liste n'existe pas
        if self.head is None:
            print("Liste vide")
            return
        curr = self.head
        result = ""
        while curr:
            # ajoute la données de notre node dans une var
            result += str(curr.data) + '->'
            # fait avancer notre node
            curr = curr.next
        print(result)
        
    # il a pas de next donc on dit none
    def insert_at_end(self, data):
        # si on call cette methode quand la liste est vide
        if self.head is None:
            # on dit que la head est vide
            self.head = Node(data, None)
            return
        
        # on va a la head et on avance pour arriver a la limite qui est la fin de la liste
        curr = self.head
        while curr.next:
            curr = curr.next
        # quand on est arriver a la fin de la liste chaine le next sera node data, None (car fin donc pas de next)
        curr.next = Node(data, None)
    
    def remove_last(self):
        if self.head is None:
            print("Liste vide")
            return
        
        curr = self.head
        while curr.next.next: # On s'arrête à l'avant-dernier élément
            curr = curr.next
        
        curr.next = None # On supprime le lien vers le dernier élément

    def length(self):
        if self.head is None:
            print("Liste vide")
            return
        
        curr = self.head
        size = 0
        while curr.next != None:
            size +=1
            curr = curr.next
        print(size)

    def remove_at_pos(self, pos):
        if self.head is None:
            print("Liste vide")
            return

        if pos == 0:
            self.head = self.head.next
            return

        curr = self.head
        count = 0

        while curr is not None and curr.next is not None:
            if count == pos-1:
                print(f"count : {count}")
                curr.next = curr.next.next
                return
            curr = curr.next
            count+=1


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_begining(1)
    ll.append(2)
    ll.append(3)
    ll.print_list()
    ll.length()
    ll.insert_at_end(10)
    ll.print_list()
    ll.length()
    ll.remove_last()
    ll.print_list()
    ll.length()
    ll.remove_last()
    ll.print_list()
    ll.length()
    print("remove at pos")
    ll.append(9)
    ll.append(10)
    ll.print_list()
    ll.length()
    ll.remove_at_pos(1)
    ll.print_list()
    ll.length()