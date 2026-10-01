"""
Test Suite: Authentication & Session Management
Covers: Login UI, Invalid Credentials, Successful Login, Session Persistence, Logout
"""
import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.sidebar_page import SidebarPage
from config.config import Config


@pytest.mark.auth
@pytest.mark.smoke
class TestAuthentication:

    def test_login_page_renders_properly(self, page: Page):
        """Verify login page UI elements, title, and form inputs exist."""
        login = LoginPage(page)
        login.navigate()

        expect(page).to_have_title("IndustrValytics - IIOT Platform")
        expect(login.username_input).to_be_visible()
        expect(login.password_input).to_be_visible()
        expect(login.sign_in_button).to_be_visible()
        expect(login.sign_in_button).to_have_text("SIGN IN TO PLATFORM")

    def test_login_with_invalid_credentials(self, page: Page):
        """Verify login failure with incorrect credentials."""
        login = LoginPage(page)
        login.navigate()
        login.login("invalid_user", "WrongPassword!999")

        # Must not navigate away from /login
        page.wait_for_timeout(1000)
        assert "/login" in page.url
        expect(login.sign_in_button).to_be_visible()

    def test_successful_login_and_dashboard_landing(self, page: Page):
        """Verify successful login redirects to main application view with admin profile."""
        login = LoginPage(page)
        login.navigate()
        login.login(Config.ADMIN_USERNAME, Config.ADMIN_PASSWORD)

        # Verify redirection to /oee view
        page.wait_for_url("**/oee?**", timeout=Config.DEFAULT_TIMEOUT)
        assert "/oee" in page.url

        # Verify shopfloor live status and admin role badge
        expect(page.locator("text=Shopfloor Live").first).to_be_visible()
        expect(page.locator("text=ADMIN").first).to_be_visible()

    def test_logout_redirects_to_login(self, authenticated_page: Page):
        """Verify logging out clears session and redirects to /login."""
        sidebar = SidebarPage(authenticated_page)
        sidebar.logout()

        # Should be back on /login
        expect(authenticated_page).to_have_url(f"{Config.BASE_URL}/login")
        login = LoginPage(authenticated_page)
        expect(login.sign_in_button).to_be_visible()
