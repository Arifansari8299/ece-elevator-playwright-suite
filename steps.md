0. Setup on a new machine after `git clone`:
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
playwright install chromium
```

1. Activate virtual environment:
```powershell
.\venv\Scripts\Activate.ps1
```

2. Run the test in headless mode 
```
.\venv\Scripts\pytest.exe

```

3. during demonstration 
```
.\venv\Scripts\pytest.exe --headed --slowmo 500

```

4. Run specific suites (Headless or Headed)
```powershell
# Only run Authentication (Headless)
.\venv\Scripts\pytest.exe tests/test_auth.py

# Only run Authentication in Headed mode (Visual demonstration)
.\venv\Scripts\pytest.exe tests/test_auth.py --headed --slowmo 500

# Only run Production Analysis in Headed mode
.\venv\Scripts\pytest.exe tests/test_production.py --headed --slowmo 500

# Only run User Management in Headed mode
.\venv\Scripts\pytest.exe tests/test_user_management.py --headed --slowmo 500

# Only run FastAPI direct Backend tests
.\venv\Scripts\pytest.exe tests/test_backend_api.py
```

5. Running by Marker Tag
```
.\venv\Scripts\pytest.exe -m smoke
.\venv\Scripts\pytest.exe -m api
.\venv\Scripts\pytest.exe -m production

```

