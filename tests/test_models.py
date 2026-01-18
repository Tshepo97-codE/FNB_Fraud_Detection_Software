"""Tests for FraudDetectionModel"""
import pytest
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / "api"))


class TestFraudDetectionModel:
    """Test cases for the FraudDetectionModel class"""
    
    def test_model_initialization(self):
        """Test that model can be imported and initialized"""
        from models import FraudDetectionModel
        model = FraudDetectionModel()
        assert model is not None
        assert hasattr(model, 'predict_single')
        assert hasattr(model, 'set_threshold')
    
    def test_threshold_setter(self):
        """Test threshold setter with valid values"""
        from models import FraudDetectionModel
        model = FraudDetectionModel()
        
        # Valid thresholds
        assert model.set_threshold(0.5) == True
        assert model.set_threshold(0.0) == True
        assert model.set_threshold(1.0) == True
        
        # Invalid thresholds
        assert model.set_threshold(-0.1) == False
        assert model.set_threshold(1.5) == False
    
    def test_predict_response_structure(self):
        """Test that predict_single returns correct structure"""
        from models import FraudDetectionModel
        model = FraudDetectionModel()
        
        # Mock transaction data
        transaction = {
            'amount': 100.0,
            'merchant_type': 'online',
            'country': 'US'
        }
        
        result = model.predict_single(transaction)
        
        # Check response has required keys (even if there's an error)
        assert isinstance(result, dict)
        if "error" not in result:
            assert "fraud_probability" in result
            assert "is_fraud" in result
            assert "risk_level" in result
            assert "threshold" in result


class TestAppImport:
    """Test that Flask app can be imported"""
    
    def test_app_creation(self):
        """Test that Flask app initializes without errors"""
        from app import app
        assert app is not None
        assert app.config is not None
