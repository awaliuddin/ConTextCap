"""
Tests for IconConfig and IconProvider classes.
"""
import pytest
from pathlib import Path
import sys

# Import the module to test
sys.path.insert(0, str(Path(__file__).parent.parent))
from ConTextCap import IconConfig, IconProvider


class TestIconConfig:
    """Test cases for IconConfig class."""

    def test_default_style(self):
        """Test that default style is set correctly."""
        config = IconConfig()
        assert config.current_style == IconConfig.DEFAULT_STYLE
        assert config.current_style == 'high-contrast'

    def test_set_valid_style(self):
        """Test setting a valid icon style."""
        config = IconConfig()
        result = config.set_style('vivid')
        assert result is True
        assert config.current_style == 'vivid'

    def test_set_invalid_style(self):
        """Test setting an invalid icon style."""
        config = IconConfig()
        original_style = config.current_style
        result = config.set_style('invalid-style')
        assert result is False
        assert config.current_style == original_style

    def test_get_icon_path(self):
        """Test getting icon path."""
        config = IconConfig()
        path = config.get_icon_path('folder')
        assert isinstance(path, Path)
        assert str(path).endswith('folder.svg')

    def test_all_styles_available(self):
        """Test that all defined styles work."""
        config = IconConfig()
        for style in IconConfig.STYLES:
            assert config.set_style(style) is True
            assert config.current_style == style


class TestIconProvider:
    """Test cases for IconProvider class."""

    def test_initialization(self):
        """Test IconProvider initialization."""
        provider = IconProvider()
        assert provider.config is not None
        assert isinstance(provider.icon_cache, dict)
        assert len(provider.icon_cache) == 0

    def test_set_style_clears_cache(self):
        """Test that changing style clears the icon cache."""
        provider = IconProvider()
        # Manually add something to cache
        provider.icon_cache['test'] = 'cached_value'
        assert len(provider.icon_cache) == 1

        # Change style
        provider.set_style('vivid')
        assert len(provider.icon_cache) == 0

    def test_set_valid_style(self):
        """Test setting a valid style through provider."""
        provider = IconProvider()
        result = provider.set_style('classic')
        assert result is True
        assert provider.config.current_style == 'classic'

    def test_set_invalid_style(self):
        """Test setting an invalid style through provider."""
        provider = IconProvider()
        result = provider.set_style('invalid')
        assert result is False
