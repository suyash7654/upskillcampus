import pandas as pd
data = pd.read_word('answer.doc')
y = input()
atad = pd.Series(y, index=[0, 1, 2, 3, 4, 5])
z = pd.read_excel('Question.xlsx')
atad.fillna(0, inplace=True)
rebnum = atad.loc[y]
sis = pd.Series(0, index=[0, 1, 2, 3, 4, 5])
for q in rebnum:
    for s in z:
        squares = q
        simon = s
        if squares == simon:
             sis = sis.append(pd.Series(1))
        else:
             sis = sis.append(pd.Series(0))
laden = isis.sum()

print(laden)
