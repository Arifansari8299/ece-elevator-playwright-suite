"""
Page Object for Maintenance Analysis (Machine Overview and Electrical Health).
"""
from playwright.sync_api import Page, Locator
from pages.base_page import BasePage
from config.config import Config


class MaintenancePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    def navigate_overview(self):
        self.page.goto(Config.VIEWS["maint_overview"], wait_until="networkidle")

    def navigate_electrical_health(self):
        self.page.goto(Config.VIEWS["electrical_health"], wait_until="networkidle")

    @property
    def machine_health_cards(self) -> Locator:
        return self.page.locator(".card, [class*='card']").filter(has_text="Bending Machine")

    @property
    def electrical_telemetry_containers(self) -> Locator:
        return self.page.locator(".chart-container, .card, canvas, svg, [class*='chart']")
