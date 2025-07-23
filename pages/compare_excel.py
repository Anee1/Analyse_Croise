import streamlit as st
import pandas as pd

def comparer_excel(file1, file2):
    # Charger les fichiers Excel
    df1 = pd.read_excel(file1)
    df2 = pd.read_excel(file2)

    # Comparaison ligne par ligne et colonne par colonne
    diffs = pd.DataFrame(columns=['Ligne', 'Colonne', 'Valeur File1', 'Valeur File2'])

    for index, (row1, row2) in enumerate(zip(df1.values, df2.values)):
        for col_index, (val1, val2) in enumerate(zip(row1, row2)):
            if val1 != val2:  # Si les valeurs diffèrent
                diff_row = pd.DataFrame({
                    'Ligne': [index + 1],
                    'Colonne': [df1.columns[col_index]],
                    'Valeur File1': [val1],
                    'Valeur File2': [val2]
                })
                diffs = pd.concat([diffs, diff_row], ignore_index=True)

    return diffs




# Interface Streamlit
st.title("Comparaison de Fichiers Excel")

# Téléchargement des fichiers Excel
uploaded_file1 = st.file_uploader("Télécharger le premier fichier Excel", type=["xlsx"])
uploaded_file2 = st.file_uploader("Télécharger le deuxième fichier Excel", type=["xlsx"])

if uploaded_file1 and uploaded_file2:
    # Comparer les fichiers si les deux sont téléchargés
    diffs = comparer_excel(uploaded_file1, uploaded_file2)

    if diffs.empty:
        st.write("✅ Les fichiers sont identiques.")
    else:
        st.write("⚠️ Les différences entre les fichiers sont :")
        st.dataframe(diffs)  # Afficher les différences sous forme de tableau interactif
        
        