from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

iris = load_iris()

x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size = 0.3, random_state = 50)

rede = MLPClassifier((3,2), activation='logistic', max_iter = 200, learning_rate_init = 0.05)
model = rede.fit(x_train, y_train)

predict_train = model.predict(x_train)
confusao = confusion_matrix(y_train, predict_train)
taxa_acerto = accuracy_score(y_train, predict_train)
taxa_erro = 1 - taxa_acerto
print('Taxa de acerto: %s - Taxa de erro %s' % (taxa_acerto, taxa_erro))

predict_test = model.predict(x_test)
confusao_test = confusion_matrix(y_test, predict_test)
taxa_acerto_test = accuracy_score(y_test, predict_test)
taxa_erro_test = 1 - taxa_acerto_test

print('Taxa de acerto: %s - Taxa de erro %s' % (taxa_acerto_test, taxa_erro_test))