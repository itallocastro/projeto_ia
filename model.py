import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder

def replaceVirg(x):
  x = x.split(',')[0]
  x = x.replace('.', '')
  return x

class DecisionTreePhone:
    def __init__(self):
        self.dataset = pd.read_csv('dadosia.csv', sep=',')
        self.replaceData()
    def createModel(self):
        return DecisionTreeClassifier(random_state=0)
    def fitModel(self):
        model = self.createModel()
        model.fit(self.dataset[['Preço', 'Resistência a água', 'Câmera', 'Desempenho', '5G', 'RAM', 'Armazenamento', 'Tela', 'Digital', 'Bateria']],self.dataset['Nome'])
        return model
    def replaceData(self):
        le = LabelEncoder()
        self.dataset["Preço"] = self.dataset["Preço"].apply(lambda x: replaceVirg(x))
        # sim = 1, não = 0
        self.dataset['Resistência a água'] = le.fit_transform(self.dataset['Resistência a água'])
        # bom = 0, medio = 1, ruim = 2
        self.dataset['Câmera'] = le.fit_transform(self.dataset['Câmera'])
        # bom = 0, medio = 1, ruim = 2
        self.dataset['Desempenho'] = le.fit_transform(self.dataset['Desempenho'])
        # sim = 1, não = 0
        self.dataset['5G'] = le.fit_transform(self.dataset['5G'])
        # sim = 1, não = 0
        self.dataset['Digital'] = le.fit_transform(self.dataset['Digital'])

