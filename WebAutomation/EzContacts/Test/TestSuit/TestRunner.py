from unittest import TestLoader, TestSuite, TextTestRunner
from EzContacts.Test.Scripts.CreateVendorTest import ezContacts_vendors
from EzContacts.Test.Scripts.CreateManufacturerTest import ezContacts_manufacturer
import testtools 


if __name__ == "__main__":

    loader = TestLoader()
    suite = TestSuite((
        loader.loadTestsFromTestCase(ezContacts_vendors),
        loader.loadTestsFromTestCase(ezContacts_manufacturer),
        ))

#run test sequentially using simple TextTestRunner
    runner = TextTestRunner(verbosity=2)
    runner.run(suite)


# #run test parallel using concurrent_suite
    concurrent_suite = testtools.ConcurrentStreamTestSuite(lambda: ((case, None) for case in suite))
    concurrent_suite.run(testtools.StreamResult())