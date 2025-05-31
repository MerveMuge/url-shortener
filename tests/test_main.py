import pytest
from httpx import AsyncClient
from src.main import app, url_map
from httpx import ASGITransport

@pytest.mark.asyncio
async def test_create_short_url_has_expected_response_structure():
    url_map.clear()
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        response = await client.post("/shorten", json={"url": "https://example.com"})
        assert response.status_code == 200
        data = response.json()
        assert "short_url" in data

@pytest.mark.asyncio
async def test_create_short_url_returns_valid_short_url():
    url_map.clear()
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        response = await client.post("/shorten", json={"url": "https://example.com"})
        assert response.status_code == 200
        data = response.json()
        assert "short_url" in data
        assert data["short_url"].startswith("http://test/")

@pytest.mark.asyncio
async def test_redirect_existing_short_id_returns_redirect():
    url_map.clear()
    short_id = "abc123"
    long_url = "https://example.com"
    url_map[short_id] = long_url

    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        response = await client.get(f"/{short_id}", follow_redirects=False)
        assert response.status_code in (307, 301)
        assert response.headers["location"] == long_url

@pytest.mark.asyncio
async def test_redirect_with_invalid_short_id_returns_404():
    url_map.clear()

    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        response = await client.get("/nonexistent")
        assert response.status_code == 404
        assert response.json()["detail"] == "URL not found"