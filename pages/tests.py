def test_accueil_repond(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "GIC Bénie" in response.content.decode()
