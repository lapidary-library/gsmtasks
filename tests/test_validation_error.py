from unittest import TestCase

from gsmtasks.components.schemas.ValidationError.schema import ValidationError


class ValidationErrorTest(TestCase):
    def test_validation_error(self):
        messages = ['Missing value', 'Totally broken']
        d = {
            'field_a': messages
        }

        x = ValidationError(d)
        self.assertEqual((dict(field_a=messages),), x.args)
