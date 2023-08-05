import itertools 
import math

def create_betti_numbers(n):

    alpha_sequence = [1] * n
    beta_sequence = alpha_sequence

    numbers = range(1,n+1)

    banned_couples_list = create_banned_couples_list(alpha_sequence, beta_sequence, numbers)
    admitted_couples_list = create_admitted_couples_list(numbers, banned_couples_list)

    Betti_number = [1, len(numbers), len(admitted_couples_list)]

    old_order_list = admitted_couples_list
    step = 2

    while(Betti_number[step]>0):
        #phi_index and lenght of the correpsonding vector

        # Lista di liste costruita allo step n-1 esimo con tutti gli elementi ordinati per numero finale
        sorted_list = order_list(old_order_list, numbers, n)

        #Lista con tutte le tuple di lunghjezza i FILTRATE
        new_list_filtered = create_filtered_list(sorted_list, step)

        semifinal_list = eliminate_banned(new_list_filtered, banned_couples_list, step, numbers)

        final_list = eliminate_superbanned(semifinal_list, banned_couples_list, step)


        Betti_number.append(len(final_list))

        old_order_list = final_list
        step = step +1

    Betti_number.pop()
    return Betti_number


def create_banned_couples_list(alpha_sequence, beta_sequence, numeri):
    s = 0
    banned_couples_list = []
    for i in range(0, len(numeri)-2):
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
    for numero in numbers[1:n]:
        number_list = []
        for elem in vect:
            if elem[len(elem)-1] == numero:
             number_list.append(elem)
        ordered_list.append(number_list)
    return ordered_list

def create_filtered_list(lista_smistata, step):
    new_list_filtered = []
    for lista in lista_smistata:
        # Creo tutti i possibili vettori di lunghezza n partendo da quelli di lunghezza n-1
        combinazioni_smistate = list(itertools.combinations((lista), 2))
        
        for combinazione in combinazioni_smistate:
            # Li sommo tra di loro e prendo solo gli elementi una volta sola
            
            new_vector = ()
            for index in range(len(combinazione)):
                new_vector = new_vector + combinazione[index]
            new_vector = tuple(sorted(set(new_vector)))
            
            # Li aggiungo ai filtrati
            if len(new_vector)==step+1 and new_vector not in new_list_filtered:
                new_list_filtered.append(new_vector)
    return new_list_filtered

def eliminate_banned(new_list_filtered, lista_coppie_proibite, step, numeri):
    semifinal_list = []
    banned_list = create_banned(new_list_filtered, lista_coppie_proibite, step,  numeri)
    if step == 3:
        print(len(banned_list))

    for elem in new_list_filtered:
        if elem not in banned_list:
             semifinal_list.append(elem)

    return semifinal_list

def create_banned(new_list_filtered, lista_coppie_proibite, step, numeri):
    lista_proibite = []
    for coppia in lista_coppie_proibite:

        #tolgo a numeri  gli elemnti della coppia e quello centrale
        numeri_accettati = []
        for numero in numeri:
            if numero not in (coppia[0], coppia[0]+1, coppia[1]):
                numeri_accettati.append(numero)

    #coi numeri accettati creo dei sottovettori di lunghezza step - 1 (alle terne sono allo step 2 e volgio dei sottovettori lunghi 1)
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

def eliminate_superbanned(semifinal_list, lista_coppie_proibite, step):
    final_list = []

    for elem in semifinal_list:
        skip_elem = False
        for coppia in lista_coppie_proibite:
            if coppia[0] in elem and coppia[0]+1 in elem and coppia[1] in elem:
                skip_elem = True
                break

        if not skip_elem:
            final_list.append(elem)

    return final_list



numero_Betti = create_betti_numbers(10)
print(numero_Betti)
