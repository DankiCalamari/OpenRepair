import unittest

from utilidades.i18n import browser_language, translate


class LanguageTest(unittest.TestCase):
    def test_browser_language_and_messages(self):
        self.assertEqual(browser_language([('en-US', 1), ('es-MX', 0.8)]), 'es')
        self.assertEqual(browser_language([('es', 0), ('en-US', 1)]), 'en')
        self.assertEqual(translate('Estado cambiado a "Recibido".'), 'Status changed to "Received".')
        self.assertEqual(translate('Usuario "Ana" eliminado.'), 'User "Ana" deleted.')
        self.assertEqual(translate('Taller de Ana'), 'Taller de Ana')


if __name__ == '__main__':
    unittest.main()
