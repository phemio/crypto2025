import unittest
from tests.steps_def.CommonStep.test_landing import LandingStep

ls = unittest.TestLoader().loadTestsFromTestCase(LandingStep)

cycle1 = unittest.TestSuite([ls])

unittest.TextTestRunner(verbosity=1).run(cycle1)

