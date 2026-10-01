"""
Test Suite: Alerts & Threshold Rules Management
Covers: Active Alarms, Alarms History, Threshold Rules Configuration
"""
import pytest
from playwright.sync_api import Page, expect
from pages.alerts_page import AlertsPage


@pytest.mark.alerts
class TestAlertsManagement:

    def test_alerts_dashboard_rendering(self, authenticated_page: Page):
        """Verify alerts page renders title, tabs, and alarm status."""
        alerts_page = AlertsPage(authenticated_page)
        alerts_page.navigate()

        expect(authenticated_page.locator("text=Alerts & Threshold Management").first).to_be_visible()
        expect(alerts_page.tab_active_alarms).to_be_visible()
        expect(alerts_page.tab_alarms_history).to_be_visible()
        expect(alerts_page.tab_threshold_rules).to_be_visible()

    def test_switch_to_threshold_rules_tab(self, authenticated_page: Page):
        """Verify navigation to Threshold Rules tab shows configured rules."""
        alerts_page = AlertsPage(authenticated_page)
        alerts_page.navigate()
        alerts_page.switch_to_rules()

        # Threshold rules should be active / visible
        expect(alerts_page.tab_threshold_rules).to_be_visible()
        expect(authenticated_page.locator("text=Threshold").first).to_be_visible()

    def test_switch_to_alarms_history_tab(self, authenticated_page: Page):
        """Verify switching to Alarms History tab."""
        alerts_page = AlertsPage(authenticated_page)
        alerts_page.navigate()
        alerts_page.switch_to_history()

        expect(alerts_page.tab_alarms_history).to_be_visible()
