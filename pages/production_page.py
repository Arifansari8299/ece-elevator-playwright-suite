"""
Page Object for Production Analysis (Machine Overview and Production Trend).
"""
from playwright.sync_api import Page, Locator
from pages.base_page import BasePage
from config.config import Config


class ProductionPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    def navigate_overview(self):
        self.page.goto(Config.VIEWS["prod_overview"], wait_until="networkidle")

    def navigate_trend(self):
        self.page.goto(Config.VIEWS["prod_trend"], wait_until="networkidle")

    # --- Machine Overview Elements ---
    @property
    def filter_all(self) -> Locator:
        return self.page.locator("button, .pill, [class*='filter']").filter(has_text="All").first

    @property
    def filter_running(self) -> Locator:
        return self.page.locator("button, .pill, [class*='filter']").filter(has_text="Running").first

    @property
    def filter_idle(self) -> Locator:
        return self.page.locator("button, .pill, [class*='filter']").filter(has_text="Idle").first

    @property
    def filter_off(self) -> Locator:
        return self.page.locator("button, .pill, [class*='filter']").filter(has_text="OFF").first

    @property
    def machine_cards(self) -> Locator:
        return self.page.locator(".card, [class*='machine-card']").filter(has_text="Bending Machine")

    def get_machine_card(self, machine_code: str) -> Locator:
        return self.page.locator(".card, [class*='machine-card']").filter(has_text=machine_code).first

    # --- Production Trend Elements ---
    @property
    def trend_machine_status_card(self) -> Locator:
        return self.page.locator("text=MACHINE STATUS").first

    @property
    def trend_shift_running_time_card(self) -> Locator:
        return self.page.locator("text=SHIFT RUNNING TIME").first

    @property
    def trend_shift_total_output_card(self) -> Locator:
        return self.page.locator("text=SHIFT TOTAL OUTPUT").first

    @property
    def machine_select_dropdown(self) -> Locator:
        return self.page.locator("select").first

    @property
    def hourly_table(self) -> Locator:
        return self.page.locator("table").first

    @property
    def hourly_table_rows(self) -> Locator:
        return self.page.locator("table tbody tr")

    def filter_by_status(self, status: str):
        """Click status filter pill: 'All', 'Running', 'Idle', or 'OFF'."""
        status_lower = status.lower()
        if "all" in status_lower:
            self.filter_all.click()
        elif "run" in status_lower:
            self.filter_running.click()
        elif "idle" in status_lower:
            self.filter_idle.click()
        elif "off" in status_lower:
            self.filter_off.click()
        self.page.wait_for_timeout(500)
