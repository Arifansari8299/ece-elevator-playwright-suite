"""
Page Object for Production Report and Data Exports (/oee?view=reports).
"""
from playwright.sync_api import Page, Locator
from pages.base_page import BasePage
from config.config import Config


class ReportsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.url = Config.VIEWS["reports"]

    def navigate(self):
        self.page.goto(self.url, wait_until="networkidle")

    # Filter Inputs
    @property
    def start_date_input(self) -> Locator:
        return self.page.locator("input[type='date']").nth(0)

    @property
    def end_date_input(self) -> Locator:
        return self.page.locator("input[type='date']").nth(1)

    @property
    def machine_dropdown(self) -> Locator:
        return self.page.locator("select").first

    @property
    def run_query_button(self) -> Locator:
        return self.page.locator("button", has_text="Run Query").first

    @property
    def export_excel_button(self) -> Locator:
        return self.page.locator("button", has_text="Export Excel").first

    # Table
    @property
    def report_table(self) -> Locator:
        return self.page.locator("table").first

    @property
    def report_table_headers(self) -> Locator:
        return self.page.locator("table th")

    @property
    def report_table_rows(self) -> Locator:
        return self.page.locator("table tbody tr")

    def run_report(self, start_date: str = None, end_date: str = None, machine_val: str = "all"):
        if start_date:
            self.start_date_input.fill(start_date)
        if end_date:
            self.end_date_input.fill(end_date)
        if machine_val:
            self.machine_dropdown.select_option(machine_val)
        self.run_query_button.click()
        self.page.wait_for_timeout(1000)
