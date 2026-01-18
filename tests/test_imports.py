"""Basic import tests to ensure modules can be loaded"""
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / "api"))


def test_imports():
    """Test that core modules can be imported"""
    try:
        import app
        assert True
    except ImportError as e:
        pytest.fail(f"Failed to import app: {e}")
    
    try:
        import models
        assert True
    except ImportError as e:
        pytest.fail(f"Failed to import models: {e}")


def test_flask_app_routes():
    """Test that Flask app has expected route structure"""
    from app import app
    
    # Check that app has routes
    routes = [rule.rule for rule in app.url_map.iter_rules()]
    assert len(routes) > 0
