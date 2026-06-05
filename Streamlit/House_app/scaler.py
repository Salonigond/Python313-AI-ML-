# scaler.py

from sklearn.preprocessing import StandardScaler
import joblib

def train_scaler(X_train):
    """
    Train scaler on training data
    """
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X_train)
    return scaler, X_scaled
def save_scaler(scaler, filename="scaler.pkl"):
    """
    Save scaler to file
    """
    joblib.dump(scaler, filename)
    print(f"Scaler saved as {filename}")
def load_scaler(filename="scaler.pkl"):
    """
    Load scaler from file
    """
    scaler = joblib.load(filename)
    return scaler
def transform_data(scaler, data):
    """
    Transform new input data using trained scaler
    """
    return scaler.transform(data)