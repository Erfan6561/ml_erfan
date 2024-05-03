@@ -24,3 +24,11 @@ def test_predict_negative():
    json_data = response.json()
    assert response.status_code == 200
    assert json_data['label'] == 'NEGATIVE'


def test_predict_despise():
    response = client.post("/predict/",
                           json={"text": "I despise machine learning!"})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data['label'] == 'NEGATIVE'
