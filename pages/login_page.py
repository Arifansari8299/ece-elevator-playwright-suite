"""
Page Object for the IndustrValytics Authentication / Login Page.
"""
from playwright.sync_api import Page, Locator
from pages.base_page import BasePage
from config.config import Config


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.url = f"{Config.BASE_URL}/login"

    # Locators
    @property
    def username_input(self) -> Locator:
        return self.page.locator("#usernameInput")

    @property
    def password_input(self) -> Locator:
        return self.page.locator("#passwordInput")

    @property
    def sign_in_button(self) -> Locator:
        return self.page.locator("button[type='submit']")

    @property
    def toggle_password_visibility_button(self) -> Locator:
        return self.page.locator("#passwordInput ~ button, .password-wrapper button").first

    @property
    def error_message(self) -> Locator:
        return self.page.locator(".error, .alert, .alert-danger, [class*='error'], .toast-error").first

    def navigate(self):
        """Navigate to the login page."""
        self.page.goto(self.url, wait_until="networkidle")

    def login(self, username: str = Config.ADMIN_USERNAME, password: str = Config.ADMIN_PASSWORD):
        """Perform login with given credentials and wait for navigation."""
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.sign_in_button.click()
        self.page.wait_for_timeout(2000)

    def is_login_page_displayed(self) -> bool:
        """Check if login form elements are visible."""
        return self.username_input.is_visible() and self.sign_in_button.is_visible()
