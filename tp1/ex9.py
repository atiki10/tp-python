def analyse_texte(texte):
    mots = texte.split() 
    nb_mots = len(mots) 
    nb_caracteres = len(texte.replace(" ", ""))  
    resultat = {"nombre_de_mots": nb_mots, "nombre_de_caracteres": nb_caracteres}
    return resultat
print(analyse_texte("yassine el-atiki"))  

