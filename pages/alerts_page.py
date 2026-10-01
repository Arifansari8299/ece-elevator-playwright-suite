"""
Page Object for Alerts & Threshold Management (/oee?view=alert-settings).
"""
from playwright.sync_api import Page, Locator
from pages.base_page import BasePage
from config.config import Config


class AlertsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.url = Config.VIEWS["alerts"]

    def navigate(self):
        self.page.goto(self.url, wait_until="networkidle")

    # Tabs
    @property
    def tab_active_alarms(self) -> Locator:
        return self.page.locator("button", has_text="Active Alarms").first

    @property
    def tab_alarms_history(self) -> Locator:
        return self.page.locator("button", has_text="Alarms History").first

    @property
    def tab_threshold_rules(self) -> Locator:
        return self.page.locator("button", has_text="Threshold Rules").first

    # Content
    @property
    def empty_active_alarms_message(self) -> Locator:
        return self.page.locator("text=No Active Alarms").first

    @property
    def rules_list(self) -> Locator:
        return self.page.locator(".rule-card, table tr, [class*='rule']")

    def switch_to_history(self):
        self.tab_alarms_history.click()
        self.page.wait_for_timeout(500)

    def switch_to_rules(self):
        self.tab_threshold_rules.click()
        self.page.wait_for_timeout(500)
