import unittest
import os
from flask import current_app
from manutencao.webapp import create_app, db


class BasicsTestCase(unittest.TestCase):
    def setUp(self):
        env = os.environ.get('WEBAPP_ENV', 'Test')
        self.app = create_app('manutencao.config.%sConfig' % env.capitalize())
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_app_exists(self):
        self.assertFalse(current_app is None)

    def test_app_is_testing(self):
        self.assertTrue(current_app.config['TESTING'])
