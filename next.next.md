Excellente question ! Laissez-moi vous expliquer pourquoi on utilise `temp.next.next` :

## Visualisation avec un exemple

Prenons votre liste : `[2 -> 1 -> 10]`

```
temp     temp.next    temp.next.next
  ↓          ↓             ↓
  2    ->    1       ->   10   -> None
```

## Pourquoi `temp.next.next` ?

- **`temp`** = élément actuel
- **`temp.next`** = élément suivant  
- **`temp.next.next`** = élément après le suivant

**Pour s'arrêter à l'avant-dernier :**
- Si `temp.next.next` existe → on n'est PAS à l'avant-dernier
- Si `temp.next.next` est `None` → on EST à l'avant-dernier

## Étape par étape dans votre exemple

**État initial :** `[2 -> 1 -> 10]`

1. **temp = 2**
   - `temp.next` = 1
   - `temp.next.next` = 10 (existe !)
   - → Continue la boucle

2. **temp = 1** (après `temp = temp.next`)
   - `temp.next` = 10
   - `temp.next.next` = None (n'existe pas !)
   - → Sort de la boucle

3. **temp pointe sur 1** (l'avant-dernier)
   - `temp.next = None` supprime le lien vers 10

## Comparaison avec `temp.next`

Si on utilisait juste `while temp.next:`, on s'arrêterait au **dernier** élément, pas l'avant-dernier :

```python
# Avec temp.next - MAUVAIS pour supprimer
while temp.next:  # S'arrête au dernier élément (10)
    temp = temp.next
# temp pointe sur 10, mais on ne peut pas le supprimer !
```

C'est pourquoi on a besoin de `temp.next.next` pour s'arrêter **un cran avant** !