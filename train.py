import logging
import random
from keras.models import load_model
from sklearn.model_selection import train_test_split
from neuralnets.BiLSTMCRF import BiLSTMCRF
from neuralnets.keraslayers.ChainCRF import create_custom_objects
from util.data import Data

# :: Logging level ::
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

inputPath = 'data/family/train.txt'


data = Data(inputPathList=[inputPath])
data.loadCoNLL(inputPath)

X = data.sentences
y = data.labels

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=0)

modelWrapper = BiLSTMCRF(data)
model = modelWrapper.buildModel()

model.fit(X_train, y_train, epochs=5, validation_split=0.1, shuffle=True)
model.save('model.h5')

model = load_model('model.h5', custom_objects=create_custom_objects())
model.summary()
