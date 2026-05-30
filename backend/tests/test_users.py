import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_get_users_as_admin(client: AsyncClient, admin_token: str):
    """Test getting users as admin."""
    response = await client.get(
        "/api/v1/users",
        headers={"Authorization": f"Bearer {admin_token}"}
    )
    
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)


@pytest.mark.asyncio
async def test_get_users_unauthorized(client: AsyncClient, user_token: str):
    """Test getting users as non-admin."""
    response = await client.get(
        "/api/v1/users",
        headers={"Authorization": f"Bearer {user_token}"}
    )
    
    assert response.status_code == 403


@pytest.mark.asyncio
async def test_get_user_by_id_as_admin(client: AsyncClient, admin_token: str, user_id: str):
    """Test getting user by ID as admin."""
    response = await client.get(
        f"/api/v1/users/{user_id}",
        headers={"Authorization": f"Bearer {admin_token}"}
    )
    
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == user_id


@pytest.mark.asyncio
async def test_update_user_as_admin(client: AsyncClient, admin_token: str, user_id: str):
    """Test updating user as admin."""
    response = await client.patch(
        f"/api/v1/users/{user_id}",
        json={"full_name": "Updated Name"},
        headers={"Authorization": f"Bearer {admin_token}"}
    )
    
    assert response.status_code == 200
    data = response.json()
    assert data["full_name"] == "Updated Name"


@pytest.mark.asyncio
async def test_delete_user_as_admin(client: AsyncClient, admin_token: str):
    """Test deleting user as admin."""
    # Create a user to delete
    create_response = await client.post(
        "/api/v1/auth/register",
        json={
            "email": "todelete@example.com",
            "password": "testpassword123",
            "full_name": "To Delete"
        }
    )
    user_id = create_response.json()["user"]["id"]
    
    # Delete the user
    response = await client.delete(
        f"/api/v1/users/{user_id}",
        headers={"Authorization": f"Bearer {admin_token}"}
    )
    
    assert response.status_code == 204
