"""
Base Page Object providing common utilities and interactions across all pages.
"""
from playwright.sync_api import Page, Locator
from config.config import Config


class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.page.set_default_timeout(Config.DEFAULT_TIMEOUT)

    # Common locators in IndustrValytics header
    @property
    def header_title(self) -> Locator:
        return self.page.locator(".header-title, header h1, header h2, .main-title").first

    @property
    def shopfloor_live_badge(self) -> Locator:
        return self.page.locator("text=Shopfloor Live").first

    @property
    def active_gateways_text(self) -> Locator:
        return self.page.locator("text=Active Gateways:").first

    @property
    def refresh_button(self) -> Locator:
        return self.page.locator("button:has-text('Refresh')").first

    @property
    def notification_bell(self) -> Locator:
        return self.page.locator("header button svg, header svg").first

    def navigate_to(self, url: str):
        """Navigate to URL and wait until network is idle."""
        self.page.goto(url, wait_until="networkidle")

    def wait_for_seconds(self, seconds: float):
        """Explicit wait for micro-animations or rendering."""
        self.page.wait_for_timeout(seconds * 1000)

    def get_current_url(self) -> str:
        return self.page.url

    def get_title(self) -> str:
        return self.page.title()
