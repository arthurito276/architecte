# architecte : 3D

Cette version correspond au projet amélioré et ne tient pas compte du cahier des charges.

Il est toujours possible de dessiner la rue en 2D avec les améliorations proposées : 
```py 
rue(tridi = None)
```

>Des nouveaux paramètres de la fonction principales sont introduits:
>1. tridi : Angle de la perspective cavalière (en degrés)
>2. heure_force : Force l'heure du dessin (entier)

Les fonctions supplémentaires sont entièrement commentées.

Les ajouts, corrections et optimisations par rapport au projet original sont listées dans la partie annexe du compte rendu, lui-même disponible sur la branche "main".

> Exemple d'exécution :
> ```py
>rue(tridi = 45, heure_force = 12)
>```
> Une rue sera dessinée avec un angle de 45 degrés, à midi.