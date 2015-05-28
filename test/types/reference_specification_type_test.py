import unittest
import jstypes.reference_specification as rs

class ReferenceSpecificationTypeTests(unittest.TestCase):
    def test_get_value_is_type_is_not_reference_return_V(self):
        spec = rs.ReferenceSpecification(1, 'foo')
        self.assertEqual(spec.getBase('foo'), 1)
