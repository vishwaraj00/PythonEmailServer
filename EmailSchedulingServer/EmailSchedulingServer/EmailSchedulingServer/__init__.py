"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__)

import EmailSchedulingServer.views
__all__ = ["views"]
