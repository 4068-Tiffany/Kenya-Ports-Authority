def predict_delay(coords):
    features = prepare_features(coords)
    prediction = model.predict([features])
    return int(prediction[0])