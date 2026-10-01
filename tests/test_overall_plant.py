"""
Test Suite: Overall Plant Details & Live Shopfloor Telemetry
Covers: Overall Plant KPIs, Active Gateways, Shopfloor Live status, Telemetry Timeseries
"""
import pytest
from playwright.sync_api import Page, expect
from pages.overall_plant_page import OverallPlantPage
from config.config import Config


@pytest.mark.regression
class TestOverallPlantDetails:

    def test_shopfloor_header_and_active_gateways(self, authenticated_page: Page):
        """Verify Shopfloor Live status indicator and gateway IDs in the header."""
        plant_page = OverallPlantPage(authenticated_page)
        plant_page.navigate()

        expect(plant_page.shopfloor_live_badge).to_be_visible()
        expect(plant_page.active_gateways_text).to_be_visible()
        for gw in Config.EXPECTED_GATEWAYS:
            expect(authenticated_page.locator(f"text={gw}").first).to_be_visible()

    def test_overall_plant_kpi_cards(self, authenticated_page: Page):
        """Verify all critical plant health KPI cards are displayed with data."""
        plant_page = OverallPlantPage(authenticated_page)
        plant_page.navigate()

        expect(plant_page.status_card).to_be_visible()
        expect(plant_page.average_voltage_card).to_be_visible()
        expect(plant_page.average_current_card).to_be_visible()
        expect(plant_page.meter_temperature_card).to_be_visible()
        expect(plant_page.bend_count_today_card).to_be_visible()
        expect(plant_page.total_bend_count_card).to_be_visible()

    def test_overall_plant_telemetry_charts(self, authenticated_page: Page):
        """Verify phase voltages and currents telemetry chart sections are present."""
        plant_page = OverallPlantPage(authenticated_page)
        plant_page.navigate()

        expect(plant_page.phase_neutral_voltages_chart).to_be_visible()
        expect(plant_page.phase_currents_chart).to_be_visible()
        expect(plant_page.phase_line_voltages_chart).to_be_visible()
