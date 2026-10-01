"""
Page Object for Overall Plant Details view (/oee?view=overall).
"""
from playwright.sync_api import Page, Locator
from pages.base_page import BasePage
from config.config import Config


class OverallPlantPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.url = Config.VIEWS["overall"]

    def navigate(self):
        self.page.goto(self.url, wait_until="networkidle")

    # Locators
    @property
    def machine_heading(self) -> Locator:
        return self.page.locator("h2, h3, .machine-title").first

    @property
    def status_card(self) -> Locator:
        return self.page.locator("text=MACHINE STATUS").first

    @property
    def average_voltage_card(self) -> Locator:
        return self.page.locator("text=AVERAGE VOLTAGE").first

    @property
    def average_current_card(self) -> Locator:
        return self.page.locator("text=AVERAGE CURRENT").first

    @property
    def meter_temperature_card(self) -> Locator:
        return self.page.locator("text=METER TEMPERATURE").first

    @property
    def bend_count_today_card(self) -> Locator:
        return self.page.locator("text=BEND COUNT TODAY").first

    @property
    def total_bend_count_card(self) -> Locator:
        return self.page.locator("text=TOTAL BEND COUNT").first

    # Telemetry Chart sections
    @property
    def phase_neutral_voltages_chart(self) -> Locator:
        return self.page.locator("text=Phase-Neutral Voltages").first

    @property
    def phase_currents_chart(self) -> Locator:
        return self.page.locator("text=Phase Currents").first

    @property
    def phase_line_voltages_chart(self) -> Locator:
        return self.page.locator("text=Phase-Phase (Line) Voltages").first

    def get_kpi_card_count(self) -> int:
        return self.page.locator(".card, [class*='kpi'], [class*='stat-card']").count()
