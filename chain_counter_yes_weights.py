import itertools 

# The edge is indicated by the number of alpha.
#                 index of the last used x_i
#                 1  2  3  4  5  6  7  8  9 10,11,12
alpha_sequence = [1, 4, 1, 1, 1, 1, 1, 1, 1]
#                 |  |  |  | 
#                 |  |  |  |
#                 |  |  |  |
#                 0  1  2  3  4  5  6  7
beta_sequence  = [1, 4, 1, 1, 1, 1, 1, 1, 1, 1]


def create_betti_numbers(alpha_sequence, beta_sequence):

    n = len(alpha_sequence)
    numbers = range(1,n+1)

    banned_couples_list = create_banned_couples_list(alpha_sequence, beta_sequence, numbers)
    print(banned_couples_list)
    admitted_couples_list = create_admitted_couples_list(numbers, banned_couples_list)

    Betti_number = [1, len(numbers), len(admitted_couples_list)]

    # entriamo ora nel ciclo 
    old_order_list = admitted_couples_list
    step = 2

    while(Betti_number[step]>0):
        #indice della Phi e lunghezza del vettore corrispondente

        # Lista di liste costruita allo step n-1 esimo con tutti gli elementi ordinati per number finale
        sorted_list = order_list(old_order_list, numbers, n)

        #Lista con tutte le tuple di lunghjezza i FILTRATE
        new_list_filtered = create_sorted_list(sorted_list, step)

        semifinal_list = eliminate_banned(new_list_filtered, banned_couples_list, step, numbers)

        final_list = eliminate_super_banned(semifinal_list, banned_couples_list, step)


        Betti_number.append(len(final_list))
        old_order_list = final_list
        step = step +1

    Betti_number.pop()
    return Betti_number

def create_banned_couples_list(alpha_sequence, beta_sequence, numbers):
    s = 0
    banned_couples_list = []
    for i in range(0, len(numbers)-2):
        if alpha_sequence[i]>=beta_sequence[i+1] and alpha_sequence[i+1]<= beta_sequence[i+2]:
            s = s+1
            banned_couples_list.append((i+1, i+3))
    return banned_couples_list

def create_admitted_couples_list(numbers, banned_couples_list):
    admitted_couples_list = []
    for coppia in tuple(itertools.combinations(numbers, 2)):
        if coppia not in banned_couples_list:
            admitted_couples_list.append(coppia)
    return admitted_couples_list

def order_list(vect, numbers, n):
    ordered_list = []
    for number in numbers[1:n]:
        number_list = []
        for elem in vect:
            if elem[len(elem)-1] == number:
             number_list.append(elem)
        ordered_list.append(number_list)
    return ordered_list

def create_sorted_list(sorted_list, step):
    new_list_filtered = []
    for lista in sorted_list:
        # Creo tutti i possibili vettori di lunghezza n partendo da quelli di lunghezza n-1
        combinazioni_smistate = list(itertools.combinations((lista), 2))
        
        for combinazione in combinazioni_smistate:
            # Li sommo tra di loro e prendo solo gli elementi una volta sola
            
            nuovo_vettore = ()
            for index in range(len(combinazione)):
                nuovo_vettore = nuovo_vettore + combinazione[index]
            nuovo_vettore = tuple(sorted(set(nuovo_vettore)))
            
            # Li aggiungo ai filtrati
            if len(nuovo_vettore)==step+1 and nuovo_vettore not in new_list_filtered:
                new_list_filtered.append(nuovo_vettore)
    return new_list_filtered

def eliminate_banned(new_list_filtered, banned_couples_list, step, numbers):
    semifinal_list = []
    lista_proibite = crea_proibite(new_list_filtered, banned_couples_list, step,  numbers)

    for elem in new_list_filtered:
        if elem not in lista_proibite:
             semifinal_list.append(elem)

    return semifinal_list

def crea_proibite(new_list_filtered, banned_couples_list, step, numbers):
    lista_proibite = []
    for coppia in banned_couples_list:

        #tolgo a numbers  gli elemnti della coppia e quello centrale
        numeri_accettati = []
        for number in numbers:
            if number not in (coppia[0], coppia[0]+1, coppia[1]):
                numeri_accettati.append(number)

    #coi numbers accettati creo dei sottovettori di lunghezza step - 1 (alle terne sono allo step 2 e volgio dei sottovettori lunghi 1)
        small_vect_list = tuple(itertools.combinations(numeri_accettati,step - 1))

        for small_vect in small_vect_list:
            eliminatore1 = tuple(sorted((coppia[0], coppia[0]+1) + small_vect))
            eliminatore2 = tuple(sorted((coppia[0]+1, coppia[1]) + small_vect))
            da_eliminare = tuple(sorted((coppia[0], coppia[1]) + small_vect))
            if eliminatore1 in new_list_filtered and eliminatore2 in new_list_filtered:
                lista_proibite.append(da_eliminare)
                if da_eliminare in new_list_filtered:
                    new_list_filtered.remove(tuple(sorted((coppia[0], coppia[1]) + small_vect)))
    
    return lista_proibite

def eliminate_super_banned(semifinal_list, banned_couples_list, step):
    final_list = []

    for elem in semifinal_list:
        skip_elem = False
        for coppia in banned_couples_list:
            if coppia[0] in elem and coppia[0]+1 in elem and coppia[1] in elem:
                skip_elem = True
                break

        if not skip_elem:
            final_list.append(elem)

    return final_list



Betti_number = create_betti_numbers(alpha_sequence, beta_sequence)
print("=======")
print(Betti_number)
print("=======")
