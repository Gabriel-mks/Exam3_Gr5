#PSEUDO-CODE

# faire un dictionnaire contenant un pseudo ,une liste de messages et leurs signatures

# pour chaque message = séparer les messages en mots

# conserver que les mots ayant moin de 3 lettre

# faire les signatures pour obtnenir les signature attendue

# comprarer la signature générer a celle donner

# classer les messages si ils sont valides ou invalides

# retourner les listes

messages_gr5 = {
    "pseudo" : "IronCode",
    "messages" : ["Le monstre est au niveau 7", "Code 9 activé demain", "La réponse est 142"],
    "signatures" : ["fresea", "odivai", "nses14"]
}

def generer_signature(messages):
    """
    générer la signature d'un message
    :param messages:
    :return: retourner la signature pour les mot ayant moin de 3 lettre
    """

    mots = messages_gr5
    signature = ""
    for mot in mots :
        if len(mot) >= 3:
            signature  += mot[-3:-1] # pour enlever l'avant dernière lettre du mot en dessous de 3 lettre ou égal a 3 lettre #CodeBro youtube et vue en classe
        return signature

def verifier_messages(messages_dict: dict):# dict = vue avec les dictionnaire et vue sur la video dictionnaire de CodeBro sur Youtube
    """
    générer les signature des messges
    :param messages_dict:
    :return: les liste valides et altérés
    """
    messages = messages_dict["messages"]
    signature_attendues = messages_dict["signatures"]

    messages_valides = []
    messages_alteres = []

    for messages,signature_attendues in zip(messages,signature_attendues): # fonction zip vue a l'aide des videos CodeBro sur Youtube
        signatures_calcule = generer_signature(messages)
        if signatures_calcule == signature_attendues:
            messages_valides.append(messages)
        else:
            messages_alteres.append(messages)

    return messages_valides,messages_alteres

if __name__ == "__main__": # vue a l'aide d'exercice compltéter avec chatgpt et vue en classe
    valides,alteres = verifier_messages(messages_gr5)

    print("Messages avec signature validées :")
    for m in valides: #value vue en classe mais au lieu de i = m
        print(m)

    print("Messages altérés, signatures non valides :")
    for m in alteres :
        print(m)




