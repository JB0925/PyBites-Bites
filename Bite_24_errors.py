=================================== FAILURES ===================================
__________________ test_super_and_abst_method_implementation ___________________

    def test_super_and_abst_method_implementation():
        merged_prs = [41, 42, 44]
        try:
>           blog = BlogChallenge(1, 'Wordvalues', merged_prs)
E           TypeError: Can't instantiate abstract class BlogChallenge with abstract methods pretty_title

/tmp/test_challenge.py:31: TypeError

During handling of the above exception, another exception occurred:

    def test_super_and_abst_method_implementation():
        merged_prs = [41, 42, 44]
        try:
            blog = BlogChallenge(1, 'Wordvalues', merged_prs)
        except TypeError:
>           pytest.fail("Unexpected TypeError, missing methods/properties?")
E           Failed: Unexpected TypeError, missing methods/properties?

/tmp/test_challenge.py:33: Failed
_________________ test_super_and_abst_property_implementation __________________

    def test_super_and_abst_property_implementation():
        try:
>           bite = BiteChallenge(24, 'ABC and class inheritance', 'my result')
E           TypeError: Can't instantiate abstract class BiteChallenge with abstract methods verify

/tmp/test_challenge.py:42: TypeError

During handling of the above exception, another exception occurred:

    def test_super_and_abst_property_implementation():
        try:
            bite = BiteChallenge(24, 'ABC and class inheritance', 'my result')
        except TypeError:
>           pytest.fail("Unexpected TypeError, missing methods/properties?")
E           Failed: Unexpected TypeError, missing methods/properties?

/tmp/test_challenge.py:44: Failed
=========================== short test summary info ============================
FAILED ../../tmp/test_challenge.py::test_super_and_abst_method_implementation
FAILED ../../tmp/test_challenge.py::test_super_and_abst_property_implementation
========================= 2 failed, 2 passed in 0.09s ==========================
