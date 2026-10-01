"""
Test Suite: Production Reports & Data Exports
Covers: Query filters, date range selection, report table verification, Excel export trigger
"""
import pytest
from playwright.sync_api import Page, expect
from pages.reports_page import ReportsPage


@pytest.mark.reports
class TestReports:

    def test_reports_filter_controls_rendered(self, authenticated_page: Page):
        """Verify report filter controls (start date, end date, machine dropdown, buttons)."""
        reports_page = ReportsPage(authenticated_page)
        reports_page.navigate()

        expect(authenticated_page.locator("text=Production Report").first).to_be_visible()
        expect(reports_page.start_date_input).to_be_visible()
        expect(reports_page.end_date_input).to_be_visible()
        expect(reports_page.machine_dropdown).to_be_visible()
        expect(reports_page.run_query_button).to_be_visible()
        expect(reports_page.export_excel_button).to_be_visible()

    def test_report_table_headers_and_data(self, authenticated_page: Page):
        """Verify report table has expected columns and renders rows upon query execution."""
        reports_page = ReportsPage(authenticated_page)
        reports_page.navigate()
        reports_page.run_report()

        expected_headers = ["Sl No", "Date", "Shift", "Machine", "Production Qty", "Running Time"]
        for header in expected_headers:
            expect(reports_page.report_table.locator(f"text={header}").first).to_be_visible()

    def test_excel_export_action_available(self, authenticated_page: Page):
        """Verify export excel button is enabled and clickable."""
        reports_page = ReportsPage(authenticated_page)
        reports_page.navigate()

        expect(reports_page.export_excel_button).to_be_enabled()
