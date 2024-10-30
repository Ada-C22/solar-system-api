import pytest


# def test_get_all_planets_with_no_records(client):
#     # Act
#     response = client.get("/planets")
#     response_body = response.get_json()

#     # Assert
#     assert response.status_code == 200
#     assert response_body == []

# def test_get_one_planet_404(client):
#     # Arrange
#     # No setup needed - we want an empty database
#     # Act
#     response = client.get(f" / planets /10")
#     response_body = response.get_json()
#     # Assert
#     assert response.status_code == 404
#     assert response_body == {f"message": "Planet not found"}
    
def test_get_one_planet_success(client, two_saved_planets):
    # arrange is in the conftest
    # act
    
    response = client.get(f"/planets/2") 
    response_body = response.get_json()
    
    #assert
    assert response.status_code == 200
    assert response_body == {
        "id": 2,
        "name": "Vulcan",
        "description": "the best",
        "moon": 2
    }
    
def test_create_new_planet_with_data(client, create_new_planet):
    #arrange is in the conftest
    #act
    response = client.post("/planets",json ={
        "name": "Romulus",
        "description": "Homeworld of the Romulan Star Empire, featuring green-tinted skies and advanced architecture.",
        "moon": 2
    })
    response_body = response.get_json()
    response_body.pop("id")
    
    #assert
    assert response.status_code == 201
    assert response_body == {
        "name": "Romulus",
        "description": "Homeworld of the Romulan Star Empire, featuring green-tinted skies and advanced architecture.",
        "moon": 2
    }
    
