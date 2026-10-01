"""
Page Object for the Sidebar Navigation and Profile Actions.
"""
from playwright.sync_api import Page, Locator
from pages.base_page import BasePage
from config.config import Config


class SidebarPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    # Brand / Logo
    @property
    def brand_logo(self) -> Locator:
        return self.page.locator("aside img, aside .logo, text=IndustrValytics").first

    # Main Navigation Items
    @property
    def nav_overall_plant(self) -> Locator:
        return self.page.locator(".nav-item", has_text="Overall Plant Details")

    @property
    def nav_production_analysis(self) -> Locator:
        return self.page.locator(".nav-item", has_text="Production Analysis")

    @property
    def nav_maintenance_analysis(self) -> Locator:
        return self.page.locator(".nav-item", has_text="Maintenance Analysis")

    @property
    def nav_alert_settings(self) -> Locator:
        return self.page.locator(".nav-item", has_text="Alert Settings")

    @property
    def nav_reports(self) -> Locator:
        return self.page.locator(".nav-item", has_text="Reports")

    @property
    def nav_user_management(self) -> Locator:
        return self.page.locator(".nav-item", has_text="User Management")

    # Sub-items
    def get_production_machine_overview(self) -> Locator:
        # First ensure Production Analysis is open
        return self.page.locator(".nav-subitem", has_text="Machine Overview").first

    def get_production_trend(self) -> Locator:
        return self.page.locator(".nav-subitem", has_text="Production Trend").first

    def get_maintenance_electrical_health(self) -> Locator:
        return self.page.locator(".nav-subitem", has_text="Electrical Health").first

    # User Profile / Logout
    @property
    def user_profile_badge(self) -> Locator:
        return self.page.locator("aside").locator("text=ADMIN").first

    @property
    def logout_button(self) -> Locator:
        return self.page.locator("aside button:has(svg), aside [title*='Logout'], aside [aria-label*='Logout']").last

    # Navigation Actions
    def go_to_overall_plant(self):
        self.nav_overall_plant.click()
        self.page.wait_for_url("**/oee?view=overall", timeout=Config.DEFAULT_TIMEOUT)

    def go_to_production_overview(self):
        self.page.goto(Config.VIEWS["prod_overview"], wait_until="networkidle")

    def go_to_production_trend(self):
        self.page.goto(Config.VIEWS["prod_trend"], wait_until="networkidle")

    def go_to_maintenance_overview(self):
        self.page.goto(Config.VIEWS["maint_overview"], wait_until="networkidle")

    def go_to_electrical_health(self):
        self.page.goto(Config.VIEWS["electrical_health"], wait_until="networkidle")

    def go_to_alerts(self):
        self.page.goto(Config.VIEWS["alerts"], wait_until="networkidle")

    def go_to_reports(self):
        self.page.goto(Config.VIEWS["reports"], wait_until="networkidle")

    def go_to_user_management(self):
        self.page.goto(Config.VIEWS["users"], wait_until="networkidle")

    def logout(self):
        """Click logout and wait for redirect to /login."""
        self.logout_button.click()
        self.page.wait_for_url("**/login", timeout=Config.DEFAULT_TIMEOUT)
