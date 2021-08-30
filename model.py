import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import _tree
import numpy as np
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
    def tree_to_code(self,tree, feature_names):
        tree_ = tree.tree_
        feature_name = [
            feature_names[i] if i != _tree.TREE_UNDEFINED else "undefined!"
            for i in tree_.feature
        ]
        feature_names = [f.replace(" ", "_")[:-5] for f in feature_names]
        def recurse(f,node, depth):
            indent = "    " * depth
            if tree_.feature[node] != _tree.TREE_UNDEFINED:
                name = feature_name[node]
                threshold = tree_.threshold[node]
                f.write("{}if {} <= {}:\n".format(indent, name, np.round(threshold,2)))
                recurse(f,tree_.children_left[node], depth + 1)
                f.write("{}else:\n".format(indent, name, np.round(threshold,2)))
                recurse(f,tree_.children_right[node], depth + 1)
            else:
                for i in range(0,len(tree_.value[node][0])):
                    if(tree_.value[node][0][i] >= 1):
                        name = self.dataset['Nome'][i]
                        f.write("{}x = {}\n".format(indent, str('"'+name+'"')))

        with open('rules.txt', 'w') as f:
            f.write('global x\n')
            recurse(f,0, 0)
    def predict(self,Preço, Resistência, Câmera, Desempenho, fiveG, RAM, Armazenamento, Tela, Digital, Bateria, file):
        exec(file.read())
        return x
    def fitModel(self):
        model = self.createModel()
        model.fit(self.dataset[['Preço', 'Resistência', 'Câmera', 'Desempenho', 'fiveG', 'RAM', 'Armazenamento', 'Tela', 'Digital', 'Bateria']],self.dataset['Nome'])
        self.tree_to_code(model, list(self.dataset.columns[1:]))
        return model
    def replaceData(self):
        le = LabelEncoder()
        self.dataset["Preço"] = self.dataset["Preço"].apply(lambda x: replaceVirg(x))
        self.dataset = self.dataset.rename(columns={'Resistência a água': 'Resistência', '5G': 'fiveG'})
        # sim = 1, não = 0
        self.dataset['Resistência'] = le.fit_transform(self.dataset['Resistência'])
        # bom = 0, medio = 1, ruim = 2
        self.dataset['Câmera'] = le.fit_transform(self.dataset['Câmera'])
        # bom = 0, medio = 1, ruim = 2
        self.dataset['Desempenho'] = le.fit_transform(self.dataset['Desempenho'])
        # sim = 1, não = 0
        self.dataset['fiveG'] = le.fit_transform(self.dataset['fiveG'])
        # sim = 1, não = 0
        self.dataset['Digital'] = le.fit_transform(self.dataset['Digital'])

