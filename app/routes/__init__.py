from flask import Flask

# Add configuration, such as registering blueprints or configuring databases
def create_app(test_config=None):
    app = Flask(__name__)

    return app
