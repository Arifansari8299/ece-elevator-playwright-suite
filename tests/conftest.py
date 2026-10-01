"""
Pytest Fixtures and Global Test Configuration for Playwright.
"""
import pytest
from playwright.sync_api import Browser, Page, Playwright, APIRequestContext
from config.config import Config
from pages.login_page import LoginPage
from pages.sidebar_page import SidebarPage


@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args, pytestconfig):
    """Launch browser with maximized window when running in headed mode."""
    launch_args = dict(browser_type_launch_args)
    args = list(launch_args.get("args", []))
    if pytestconfig.getoption("--headed"):
        args.append("--start-maximized")
    launch_args["args"] = args
    return launch_args


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args, pytestconfig):
    """Set dynamic viewport for headed mode and full HD for headless mode."""
    is_headed = pytestconfig.getoption("--headed")
    context_args = dict(browser_context_args)
    context_args["ignore_https_errors"] = True

    if is_headed:
        # In headed mode, adapt 100% to the user's laptop screen resolution (no clipping)
        context_args["no_viewport"] = True
    else:
        # In headless mode, use standard 1080p viewport
        context_args["viewport"] = {
            "width": 1920,
            "height": 1080,
        }
    return context_args


@pytest.fixture
def login_page(page: Page) -> LoginPage:
    """Fixture to provide a fresh LoginPage instance."""
    return LoginPage(page)


@pytest.fixture
def authenticated_page(page: Page) -> Page:
    """Fixture that logs in as Admin and yields the authenticated page."""
    login = LoginPage(page)
    login.navigate()
    login.login(Config.ADMIN_USERNAME, Config.ADMIN_PASSWORD)
    page.wait_for_url("**/oee?**", timeout=Config.DEFAULT_TIMEOUT)
    return page


@pytest.fixture
def sidebar(authenticated_page: Page) -> SidebarPage:
    """Fixture to provide SidebarPage instance on an authenticated session."""
    return SidebarPage(authenticated_page)


@pytest.fixture(scope="session")
def api_client(playwright: Playwright) -> APIRequestContext:
    """Unauthenticated API client fixture."""
    request_context = playwright.request.new_context(
        base_url=Config.API_BASE_URL,
        extra_http_headers={"Accept": "application/json"}
    )
    yield request_context
    request_context.dispose()


@pytest.fixture(scope="session")
def auth_token(api_client: APIRequestContext) -> str:
    """Obtain JWT bearer access token for admin."""
    res = api_client.post(
        "/api/auth/login",
        data={
            "username": Config.ADMIN_USERNAME,
            "password": Config.ADMIN_PASSWORD,
        },
        headers={"Content-Type": "application/json"}
    )
    assert res.status == 200, f"Login failed with status {res.status}"
    return res.json()["access_token"]


@pytest.fixture(scope="session")
def authenticated_api_client(playwright: Playwright, auth_token: str) -> APIRequestContext:
    """Authenticated API client fixture with Bearer token header."""
    request_context = playwright.request.new_context(
        base_url=Config.API_BASE_URL,
        extra_http_headers={
            "Accept": "application/json",
            "Authorization": f"Bearer {auth_token}"
        }
    )
    yield request_context
    request_context.dispose()
