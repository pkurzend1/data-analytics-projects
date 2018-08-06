import sklearn.metrics
import sklearn.datasets
import sklearn.model_selection
import sklearn
import numpy as np
import numpy.random

# keras
from keras.layers import Input, Dense
from keras.models import Model
import keras

# PSO
import myPSO 


num_classes = 10
digits =  sklearn.datasets.load_digits()
X, X_test, y, y_test = sklearn.model_selection.train_test_split(digits.images, digits.target)

X = X.reshape(X.shape[0], -1)
X_test = X_test.reshape(X_test.shape[0],-1)
y = y.reshape(y.shape[0], 1)
y_test = y_test.reshape(y_test.shape[0], 1)

one_hot_y = keras.utils.to_categorical(y, num_classes=10)
one_hot_y_test = keras.utils.to_categorical(y_test, num_classes=10)

print(type(X)) #numpy.ndarray
print("X shape: ", X.shape)
print("X_test shape: ", X_test.shape)
print("y shape: ", y.shape)
print("y_test shape: ", y_test.shape)
print("one_hot_y shape: ", one_hot_y.shape)
print("one_hot_y_test shape: ", one_hot_y_test.shape)

models = {}
i = 0

def ann_model(num_layers, layer_dims ,X, X_test, y, y_test):
    num_layers = int(num_layers)
    layer_dims = int(layer_dims)

    inputs = Input(shape=(64,))
    x = Dense(layer_dims, activation='relu')(inputs)

    for _ in range(num_layers-1):
        x = Dense(layer_dims, activation='relu')(x)

    predictions = Dense(10, activation='softmax')(x)

    # This creates a model that includes
    # the Input layer and three Dense layers
    model = Model(inputs=inputs, outputs=predictions)
    model.compile(optimizer='adam',
                loss='categorical_crossentropy',
                metrics=['accuracy'])
    model.fit(X, one_hot_y, epochs=25)  # starts training

    score = model.evaluate(X_test, one_hot_y_test)

    global i
    models[str(i)] = {"model" : model, "num_layers" : num_layers, "layer_dims" : layer_dims, "cost" : score[0], "accuracy" : score[1]}
    i += 1

    print(score)
    return score[0] # cost



def costFunction(x):
    num_layers = int(x[0])
    layer_dims = int(x[1])

    cost = ann_model(num_layers, layer_dims ,X, X_test, y, y_test)
    return cost

problem = myPSO.OptimizationProblem(costFunction=costFunction, varNames=["num_layers", "layer_dims"], nVar=2, varMin=[1, 10], varMax=[10, 64])
pso = myPSO.PSO(problem, MaxIter=10, PopSize=10, c1=2, c2=2, w = 2)
g = pso.optimize()

solution = pso.get_solution()
print(solution)

layer_dims = int(solution['layer_dims'])
num_layers = int(solution['num_layers'])

# get best model:
modelIndex = None
for i, model_dict in models.items():
    if model_dict["cost"] == g["cost"] and model_dict["num_layers"] == num_layers and model_dict["layer_dims"] == layer_dims:

        print("solution found")
        modelIndex = i
        break
else:
    assert False, "An error occurred: No match"

print(models)
model = models[str(modelIndex)]["model"]
score = model.evaluate(X_test, one_hot_y_test)
print(score)

    

