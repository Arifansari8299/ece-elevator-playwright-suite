"""
Page Object for User Management & System RBAC (/oee?view=user-management).
"""
from playwright.sync_api import Page, Locator
from pages.base_page import BasePage
from config.config import Config


class UserManagementPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.url = Config.VIEWS["users"]

    def navigate(self):
        self.page.goto(self.url, wait_until="networkidle")

    # Metrics
    @property
    def total_users_card(self) -> Locator:
        return self.page.locator("text=TOTAL USERS").first

    @property
    def active_users_card(self) -> Locator:
        return self.page.locator("text=ACTIVE USERS").first

    @property
    def administrators_card(self) -> Locator:
        return self.page.locator("text=ADMINISTRATORS").first

    # Actions & Tabs
    @property
    def add_user_button(self) -> Locator:
        return self.page.locator("button", has_text="Add User").first

    @property
    def tab_user_directory(self) -> Locator:
        return self.page.locator("button", has_text="User Directory").first

    @property
    def tab_audit_logs(self) -> Locator:
        return self.page.locator("button", has_text="Audit Logs").first

    @property
    def tab_login_history(self) -> Locator:
        return self.page.locator("button", has_text="Login History").first

    # User Table
    @property
    def users_table(self) -> Locator:
        return self.page.locator("table").first

    @property
    def user_table_headers(self) -> Locator:
        return self.page.locator("table th")

    @property
    def user_rows(self) -> Locator:
        return self.page.locator("table tbody tr")

    def get_user_row_by_username(self, username: str) -> Locator:
        return self.user_rows.filter(has_text=username).first
