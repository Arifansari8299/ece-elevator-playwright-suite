"""
Test Suite: Production Analysis (Machine Overview & Production Trend)
Covers: Machine Cards, Gateways, Shift Metrics, Status Filtering, Hourly Production
"""
import pytest
from playwright.sync_api import Page, expect
from pages.production_page import ProductionPage


@pytest.mark.production
@pytest.mark.smoke
class TestProductionAnalysis:

    def test_production_machine_overview_cards(self, authenticated_page: Page):
        """Verify machine cards display correct machine codes, names, and gateway IDs."""
        prod_page = ProductionPage(authenticated_page)
        prod_page.navigate_overview()

        # Verify page title/header
        expect(authenticated_page.locator("text=Production Analysis · Machine Overview").first).to_be_visible()

        # Check MCH-01 card
        mch01 = prod_page.get_machine_card("MCH-01")
        expect(mch01).to_be_visible()
        expect(mch01.locator("text=RG-100 Bending Machine")).to_be_visible()
        expect(mch01.locator("text=00WH9OUI")).to_be_visible()
        expect(mch01.locator("text=SHIFT PRODUCTION")).to_be_visible()
        expect(mch01.locator("text=RUNNING TIME")).to_be_visible()

        # Check MCH-02 card
        mch02 = prod_page.get_machine_card("MCH-02")
        expect(mch02).to_be_visible()
        expect(mch02.locator("text=HRB-1303 Bending Machine")).to_be_visible()
        expect(mch02.locator("text=012ZY5SC")).to_be_visible()

    def test_production_filter_pills(self, authenticated_page: Page):
        """Verify status filter tabs (All, Running, Idle, OFF) and counts."""
        prod_page = ProductionPage(authenticated_page)
        prod_page.navigate_overview()

        expect(prod_page.filter_all).to_be_visible()
        expect(prod_page.filter_running).to_be_visible()
        expect(prod_page.filter_idle).to_be_visible()
        expect(prod_page.filter_off).to_be_visible()

        # Click Idle filter
        prod_page.filter_by_status("idle")
        expect(prod_page.machine_cards.first).to_be_visible()

        # Click All filter
        prod_page.filter_by_status("all")
        assert prod_page.machine_cards.count() >= 2

    def test_production_trend_view(self, authenticated_page: Page):
        """Verify production trend metrics, charts, and hourly breakdown table."""
        prod_page = ProductionPage(authenticated_page)
        prod_page.navigate_trend()

        expect(prod_page.trend_machine_status_card).to_be_visible()
        expect(prod_page.trend_shift_running_time_card).to_be_visible()
        expect(prod_page.trend_shift_total_output_card).to_be_visible()
        expect(prod_page.hourly_table).to_be_visible()
        expect(prod_page.hourly_table.locator("text=HOURLY SHIFT INTERVAL")).to_be_visible()
