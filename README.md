# IndustrValytics IIoT Platform - QA Test Automation Framework

Enterprise Test Automation Framework for **IndustrValytics (ECE Birla Group IIoT Platform)** built with **Python**, **Playwright**, and **Pytest** following the **Page Object Model (POM)** design pattern.

---

## 1. QA Lead Strategy: Why Playwright for FastAPI + Angular?

Testing a modern IoT web application built with **Angular (Frontend)** and **FastAPI (Backend)** requires handling:
- **Dynamic Asynchronous Rendering**: Angular relies heavily on RxJS streams, client-side routing (`?view=...`), and background HTTP polling. Playwright features built-in **Auto-Waiting** (waiting for network idle, DOM attachment, visibility, and actionability), eliminating artificial sleeps and flaky tests common in Selenium and Cypress.
- **Unified E2E UI + Direct REST API Testing**: Playwright provides `APIRequestContext` right out of the box. You can test UI flows and FastAPI backend endpoints (`/health`, `/api/auth/login`, `/api/machines/gateways/active`, etc.) in the exact same test framework.
- **Fast Execution & Modern Browser Engines**: Runs natively on Chromium, Firefox, and WebKit in headless or headed modes.
- **Trace Viewer & Failure Artifacts**: Automatic full-fidelity traces, videos, and screenshots on failure to easily diagnose shopfloor telemetry and UI issues.

---

## 2. Framework Architecture & Folder Structure

```
ece-elevator-qa/
│
├── config/
│   ├── __init__.py
│   └── config.py               # Centralized configuration (URLs, credentials, timeouts, routes)
│
├── pages/                      # Page Object Model (POM) layer
│   ├── __init__.py
│   ├── base_page.py            # Base actions, global headers (Shopfloor Live, Gateways, Refresh)
│   ├── login_page.py           # Login form, credentials submission, password visibility
│   ├── sidebar_page.py         # Navigation drawer, menu links, profile actions & logout
│   ├── overall_plant_page.py   # Overall Plant KPIs, Phase Voltages & Currents telemetry
│   ├── production_page.py      # Machine Overview cards, status filters (All, Running, Idle, OFF), Trends
│   ├── maintenance_page.py     # Maintenance machine health and electrical telemetry
│   ├── alerts_page.py          # Active alarms, alarm history, threshold rules
│   ├── reports_page.py         # Date filters, machine query, Excel export
│   └── user_management_page.py # User directory, RBAC roles, audit logs, login history
│
├── tests/                      # Automated Pytest test suites
│   ├── __init__.py
│   ├── conftest.py             # Global fixtures (authenticated page, browser context, API client)
│   ├── test_auth.py            # Login, invalid credentials, session persistence, logout
│   ├── test_overall_plant.py   # Plant KPIs, gateway badges, live updates
│   ├── test_production.py      # Machine cards (MCH-01, MCH-02), status filtering, hourly table
│   ├── test_maintenance.py     # Maintenance overview and electrical health telemetry
│   ├── test_alerts.py          # Alarms dashboard, threshold rules, history
│   ├── test_reports.py         # Report generation, date filtering, Excel export action
│   ├── test_user_management.py # User metrics, user directory table, audit log tabs
│   └── test_backend_api.py     # FastAPI direct REST API integration tests
│
├── pytest.ini                  # Pytest configuration, CLI flags, markers
├── requirements.txt            # Python dependencies
└── README.md                   # QA documentation and run guide
```

---

## 3. Test Coverage Matrix

| Module | Scope / Features Covered | Test File |
| :--- | :--- | :--- |
| **Authentication** | Login UI, invalid credentials error, admin authentication, session redirect, logout | `tests/test_auth.py` |
| **Overall Plant Details** | Shopfloor Live badge, active gateways (00WH9OUI, 012ZY5SC), KPIs (Voltage, Current, Temp, Bend Counts), charts | `tests/test_overall_plant.py` |
| **Production Analysis** | Machine Cards (MCH-01 RG-100, MCH-02 HRB-1303), status filter pills (All, Running, Idle, OFF), Shift production, Hourly intervals table | `tests/test_production.py` |
| **Maintenance Analysis** | Machine health overview, electrical telemetry rendering | `tests/test_maintenance.py` |
| **Alerts & Thresholds** | Active alarms status, threshold rules tab, alarms history | `tests/test_alerts.py` |
| **Reports** | Date range picker, machine selector, query execution, Excel export action | `tests/test_reports.py` |
| **User Management & RBAC**| User KPIs (Total, Active, Admins), user table, role badges, audit logs & login history tabs | `tests/test_user_management.py` |
| **FastAPI Backend** | `/health`, `/openapi.json`, `POST /api/auth/login`, `GET /api/machines/gateways/active`, `GET /api/alerts/active`, `GET /api/admin/users` | `tests/test_backend_api.py` |

---

## 4. How to Run the Tests

### Setup Environment
```bash
# Activate your virtual environment
.\venv\Scripts\Activate.ps1

# Install dependencies (if not already installed)
pip install -r requirements.txt
playwright install chromium
```

### Running Tests

1. **Run All Tests Headless (Default CI Mode):**
   ```bash
   pytest
   ```

2. **Run All Tests Headed (Watch browser interactions live):**
   ```bash
   pytest --headed --slowmo 500
   ```

3. **Run a Specific Module:**
   ```bash
   # Authentication
   pytest tests/test_auth.py

   # Production Analysis
   pytest tests/test_production.py

   # FastAPI Backend
   pytest tests/test_backend_api.py
   ```

4. **Run by Marker Tag:**
   ```bash
   pytest -m smoke
   pytest -m api
   pytest -m production
   ```

5. **Generate HTML Report:**
   ```bash
   pytest --html=reports/test_report.html --self-contained-html
   ```
