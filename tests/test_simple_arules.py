import src.simple_arules.simple_arules as ar


transactions = [["bli", "bla", "blubb"], ["bla"]]

support_dictionaries_expected = [
    {("bla",): 2, ("bli",): 1, ("blubb",): 1},
    {("bla", "bli"): 1, ("bla", "blubb"): 1, ("bli", "blubb"): 1},
    {("bla", "bli", "blubb"): 1},
]

association_rules_expected_7 = [
    (("bla",), ("bli",), 2, 1, 0.5),
    (("bli",), ("bla",), 1, 1, 1.0),
    (("bla",), ("blubb",), 2, 1, 0.5),
    (("blubb",), ("bla",), 1, 1, 1.0),
    (("bli",), ("blubb",), 1, 1, 1.0),
    (("blubb",), ("bli",), 1, 1, 1.0),
    (("bla",), ("bli", "blubb"), 2, 1, 0.5),
]

def test_tuple_reduce():
    assert ar._tuple_reduce((1,)) == 1
    assert ar._tuple_reduce(("bla", "blubb")) == ("bla", "blubb")


def test_get_support_dictionary_for_set_size():
    assert (
        ar._get_support_dictionary_for_set_size(transactions, 3, 1)
        == support_dictionaries_expected[2]
    )


def test_get_support_dictionaries():
    assert (
        ar._get_support_dictionaries(transactions, 3, 1)
        == support_dictionaries_expected
    )


def test_all_sub_combinations():
    assert list(ar._all_sub_combinations([1, 2, 3])) == [
        (1,),
        (2,),
        (3,),
        (1, 2),
        (1, 3),
        (2, 3),
    ]


def test_get_association_rules():
    ar._get_association_rules(support_dictionaries_expected)[:7]
