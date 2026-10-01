"""
Global Configuration for ECE Elevators IoT QA Automation Framework
"""
import os

class Config:
    # Base URLs
    BASE_URL = os.getenv("BASE_URL", "http://192.168.10.20:4200")
    API_BASE_URL = os.getenv("API_BASE_URL", "http://192.168.10.20:8000")
    
    # Credentials
    ADMIN_USERNAME = os.getenv("ADMIN_USERNAME", "admin")
    ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "Admin@12345")
    
    # Timeouts (in milliseconds)
    DEFAULT_TIMEOUT = 10000
    NAVIGATION_TIMEOUT = 15000
    
    # Known Gateways
    EXPECTED_GATEWAYS = ["00WH9OUI", "012ZY5SC"]
    
    # Views / Routes
    VIEWS = {
        "overall": f"{BASE_URL}/oee?view=overall",
        "prod_overview": f"{BASE_URL}/oee?view=prod-overview",
        "prod_trend": f"{BASE_URL}/oee?view=prod-trend",
        "maint_overview": f"{BASE_URL}/oee?view=maint-overview",
        "electrical_health": f"{BASE_URL}/oee?view=electrical-health",
        "alerts": f"{BASE_URL}/oee?view=alert-settings",
        "reports": f"{BASE_URL}/oee?view=reports",
        "users": f"{BASE_URL}/oee?view=user-management",
    }
