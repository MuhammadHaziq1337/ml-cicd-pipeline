import unittest
import numpy as np
from app.model import train, predict
import os
import tempfile

class TestModel(unittest.TestCase):
    def test_train_predict(self):
        # Simple test data
        X = np.array([[1, 2], [3, 4], [5, 6]])
        y = np.array([0, 1, 0])
        
        # Use a temporary file for the model
        with tempfile.NamedTemporaryFile() as tmp:
            os.environ['MODEL_PATH'] = tmp.name
            
            # Train
            model = train(X, y)
            self.assertIsNotNone(model)
            
            # Predict
            pred = predict([1, 2])
            self.assertIsNotNone(pred)

if __name__ == '__main__':
    unittest.main()