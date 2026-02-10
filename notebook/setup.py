import os
import sys
from pathlib import Path


# --------------------------------------------------
# Path resolution
# --------------------------------------------------

# Directory where setup.py lives (new/notebook)
NOTEBOOK_DIR = Path(__file__).resolve().parent

# Repository root (new/)
REPO_DIR = NOTEBOOK_DIR.parent

# src/ → Python import root (for ai, cfehome, docs)
SRC_ROOT = REPO_DIR / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

# Django project root (contains manage.py)
DJANGO_PROJECT_ROOT = SRC_ROOT / "cfehome"
if not (DJANGO_PROJECT_ROOT / "manage.py").exists():
    raise RuntimeError(
        f"manage.py not found in {DJANGO_PROJECT_ROOT}"
    )

# Run Django as if from manage.py directory
os.chdir(DJANGO_PROJECT_ROOT)

# Correct Django settings module (INNER cfehome)
DJANGO_SETTINGS_MODULE = "cfehome.settings"


# --------------------------------------------------
# Django initialization
# --------------------------------------------------

def init(verbose=False):
    """
    Initialize Django for notebooks / scripts.
    Must be called before using ORM or settings.
    """

    # Allow asyncio inside Jupyter
    try:
        import nest_asyncio
        nest_asyncio.apply()
        if verbose:
            print("Applied nest_asyncio patch")
    except ImportError:
        if verbose:
            print("nest_asyncio not installed")

    # Environment variables
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", DJANGO_SETTINGS_MODULE)
    os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"

    # Initialize Django
    import django
    django.setup()

    if verbose:
        print("Django initialized successfully")
