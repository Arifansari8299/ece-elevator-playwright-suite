"""
Test Suite: Maintenance Analysis & Electrical Health
Covers: Machine maintenance health cards and electrical telemetry charts
"""
import pytest
from playwright.sync_api import Page, expect
from pages.maintenance_page import MaintenancePage


@pytest.mark.maintenance
class TestMaintenanceAnalysis:

    def test_maintenance_overview_cards(self, authenticated_page: Page):
        """Verify maintenance overview displays machine health status."""
        maint_page = MaintenancePage(authenticated_page)
        maint_page.navigate_overview()

        expect(authenticated_page.locator("text=Bending Machine").first).to_be_visible()

    def test_electrical_health_telemetry_rendering(self, authenticated_page: Page):
        """Verify electrical health page loads telemetry and charts without errors."""
        maint_page = MaintenancePage(authenticated_page)
        maint_page.navigate_electrical_health()

        expect(authenticated_page.locator("text=Active Gateways:").first).to_be_visible()
        expect(maint_page.electrical_telemetry_containers.first).to_be_visible()
