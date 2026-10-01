"""
Test Suite: User Management & RBAC
Covers: User Directory, RBAC Roles, User Metrics, Add User Action, Audit Logs
"""
import pytest
from playwright.sync_api import Page, expect
from pages.user_management_page import UserManagementPage


@pytest.mark.users
class TestUserManagement:

    def test_user_management_metrics_and_header(self, authenticated_page: Page):
        """Verify User Management metrics (Total Users, Active Users, Administrators)."""
        users_page = UserManagementPage(authenticated_page)
        users_page.navigate()

        expect(authenticated_page.locator("text=User Management & System RBAC").first).to_be_visible()
        expect(users_page.total_users_card).to_be_visible()
        expect(users_page.active_users_card).to_be_visible()
        expect(users_page.administrators_card).to_be_visible()
        expect(users_page.add_user_button).to_be_visible()

    def test_user_directory_table_contains_admin(self, authenticated_page: Page):
        """Verify user directory table headers and presence of admin user."""
        users_page = UserManagementPage(authenticated_page)
        users_page.navigate()

        expected_headers = ["USERNAME", "FULL NAME", "EMAIL", "ROLE", "STATUS", "ACTIONS"]
        for header in expected_headers:
            expect(users_page.users_table.locator(f"text={header}").first).to_be_visible()

        # Check that 'admin' user row is present
        admin_row = users_page.get_user_row_by_username("admin")
        expect(admin_row).to_be_visible()
        expect(admin_row.locator("text=ADMIN").first).to_be_visible()

    def test_subtabs_navigation(self, authenticated_page: Page):
        """Verify switching between User Directory, Audit Logs, and Login History."""
        users_page = UserManagementPage(authenticated_page)
        users_page.navigate()

        expect(users_page.tab_user_directory).to_be_visible()
        expect(users_page.tab_audit_logs).to_be_visible()
        expect(users_page.tab_login_history).to_be_visible()

        # Click Audit Logs
        users_page.tab_audit_logs.click()
        authenticated_page.wait_for_timeout(500)
        expect(users_page.tab_audit_logs).to_be_visible()

        # Click Login History
        users_page.tab_login_history.click()
        authenticated_page.wait_for_timeout(500)
        expect(users_page.tab_login_history).to_be_visible()
