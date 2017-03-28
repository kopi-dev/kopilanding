"""
Django settings for project.
"""

from .base import *

try:
    from .local import *
except ImportError:
    print("Can't find modeule settings.local. Make it from local.py.skeleton")

