============================= test session starts ==============================
platform linux -- Python 3.8.5, pytest-5.4.2, py-1.8.1, pluggy-0.13.1
rootdir: /tmp
plugins: asyncio-0.12.0
collected 5 items

../../tmp/test_account.py FFFFF

=================================== FAILURES ===================================
_____________________________ test_account_balance _____________________________

    def test_account_balance():
        assert checking.start_balance == 0
>       checking + 10
E       TypeError: unsupported operand type(s) for +: 'Account' and 'int'

/tmp/test_account.py:11: TypeError
___________________________ test_account_comparison ____________________________

    def test_account_comparison():
>       assert checking > saving
E       assert <account.Account object at 0x7f1eff201d00> > <account.Account object at 0x7f1eff201d90>

/tmp/test_account.py:22: AssertionError
_______________________________ test_account_len _______________________________

    def test_account_len():
>       checking + 10
E       TypeError: unsupported operand type(s) for +: 'Account' and 'int'

/tmp/test_account.py:31: TypeError
__________________________ test_account_indexing_iter __________________________

    def test_account_indexing_iter():
>       assert checking[0] == 10
E       TypeError: 'Account' object is not subscriptable

/tmp/test_account.py:38: TypeError
_______________________________ test_account_str _______________________________

    def test_account_str():
>       assert str(checking) == 'Checking account - balance: 15'
E       AssertionError: assert 'Checking acc... - balance: 0' == 'Checking acc...- balance: 15'
E         - Checking account - balance: 15
E         ?                             ^^
E         + Checking account - balance: 0
E         ?                             ^

/tmp/test_account.py:44: AssertionError
=========================== short test summary info ============================
FAILED ../../tmp/test_account.py::test_account_balance - TypeError: unsupport...
FAILED ../../tmp/test_account.py::test_account_comparison - assert <account.A...
FAILED ../../tmp/test_account.py::test_account_len - TypeError: unsupported o...
FAILED ../../tmp/test_account.py::test_account_indexing_iter - TypeError: 'Ac...
FAILED ../../tmp/test_account.py::test_account_str - AssertionError: assert '...
============================== 5 failed in 0.10s ===============================
