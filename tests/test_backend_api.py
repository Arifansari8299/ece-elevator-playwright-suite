"""
Test Suite: FastAPI Backend Integration & Contract Testing
Tests direct REST endpoints using Playwright's built-in APIRequestContext.
"""
import pytest
from playwright.sync_api import APIRequestContext
from config.config import Config


@pytest.mark.api
class TestFastAPIBackend:

    def test_health_check_endpoint(self, api_client: APIRequestContext):
        """Verify GET /health returns 200 OK."""
        response = api_client.get("/health")
        assert response.status == 200
        data = response.json()
        assert data.get("status") in ["healthy", "ok"] or "status" in data

    def test_openapi_specification_available(self, api_client: APIRequestContext):
        """Verify OpenAPI schema is exposed and valid."""
        response = api_client.get("/openapi.json")
        assert response.status == 200
        schema = response.json()
        assert schema.get("info", {}).get("title") == "ECE Elevators IoT Platform API"
        assert len(schema.get("paths", {})) > 40

    def test_api_login_success(self, api_client: APIRequestContext):
        """Verify POST /api/auth/login with valid JSON returns JWT auth token."""
        response = api_client.post(
            "/api/auth/login",
            data={
                "username": Config.ADMIN_USERNAME,
                "password": Config.ADMIN_PASSWORD
            },
            headers={"Content-Type": "application/json"}
        )
        assert response.status == 200
        data = response.json()
        assert "access_token" in data
        assert data.get("token_type") == "bearer"
        assert data.get("user", {}).get("username") == "admin"

    def test_active_gateways_endpoint(self, authenticated_api_client: APIRequestContext):
        """Verify GET /api/machines/gateways/active returns registered IoT gateways."""
        response = authenticated_api_client.get("/api/machines/gateways/active")
        assert response.status == 200
        data = response.json()
        assert isinstance(data, list)
        for gw in Config.EXPECTED_GATEWAYS:
            assert any(gw in str(item) for item in data)

    def test_active_alerts_endpoint(self, authenticated_api_client: APIRequestContext):
        """Verify GET /api/alerts/active returns alert list structure."""
        response = authenticated_api_client.get("/api/alerts/active")
        assert response.status == 200
        data = response.json()
        assert isinstance(data, list)

    def test_admin_users_endpoint(self, authenticated_api_client: APIRequestContext):
        """Verify GET /api/admin/users returns list of system users."""
        response = authenticated_api_client.get("/api/admin/users")
        assert response.status == 200
        data = response.json()
        items = data.get("items", []) if isinstance(data, dict) else data
        assert any(u.get("username") == "admin" for u in items)
