# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package


def test_success():
    assert True

# transactions = [
#     ["eggs", "bacon", "soup"],
#     ["eggs", "bacon", "apple"],
#     ["soup", "bacon", "banana"],
# ]
#
# frequent(transactions, max_length=3, min_support=1, single_tuples=True)
# apriori(transactions, max_length=3, single_tuples=True)
