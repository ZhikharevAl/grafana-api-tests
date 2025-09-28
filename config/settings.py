import os
from pathlib import Path

project_root = Path(__file__).parent.parent.resolve()

BASE_DIR = Path(os.environ.get("GITHUB_WORKSPACE", project_root))

DATA_DIR = BASE_DIR / "data"

DB_PATH_STR = os.environ.get("GRAFANA_DB_PATH")

if not DB_PATH_STR:
    DB_PATH = (BASE_DIR / "Mygrafana" / "Mygrafana" / "data" / "grafana.db").resolve()
else:
    DB_PATH = Path(DB_PATH_STR)


USERS_PATH = DATA_DIR / "users.json"
DASHBOARDS_PATH = DATA_DIR / "dashboards.json"
ORGANIZATIONS_PATH = DATA_DIR / "organizations.json"

USERS_TEMPLATE_PATH = DATA_DIR / "users.template.json"
DASHBOARDS_TEMPLATE_PATH = DATA_DIR / "dashboards.template.json"
ORGANIZATIONS_TEMPLATE_PATH = DATA_DIR / "organizations.template.json"


BASE_URL = os.getenv("GRAFANA_BASE_URL", "http://localhost:3000")
BASIC_AUTH = ("admin", "admin")
LOW_ACCESS = ("LowAccess", "test")
