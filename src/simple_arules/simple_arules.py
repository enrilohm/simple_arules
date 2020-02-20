import pandas as pd
import itertools as it
from collections import Counter
from tqdm import tqdm
from scipy.special import comb

def _tuple_reduce(t):
    return t[0] if len(t) == 1 else t


def _get_support_dictionary_for_set_size(transactions, item_set_size, min_support):
    n_trans=sum(map(lambda x: comb(len(x),item_set_size), transactions))
    print(f"{n_trans} iterations:\n")
    counter = Counter(tqdm(
        it.chain(
            *(
                it.combinations(sorted(set(transaction)), item_set_size)
                for transaction in transactions
            )
        ),total=n_trans)
    )
    print("counter done")
    return dict((x, y) for x, y in counter.items() if y >= min_support)


def _get_support_dictionaries(transactions, max_length, min_support):
    support_dictionaries = []
    for item_set_size in range(1, max_length + 1):
        print(f"generating support_dictionary for item_set_size={item_set_size}\n")
        support_dictionaries.append(
            _get_support_dictionary_for_set_size(
                transactions, item_set_size, min_support
            )
        )
    return support_dictionaries


def _all_sub_combinations(x):
    return it.chain(*(it.combinations(x, n) for n in range(1, len(x))))


def _get_association_rules(support_dictionaries):
    print("creating association_rules")
    association_rules = []
    for item_set_size in range(len(support_dictionaries)):
        suggestions = list(support_dictionaries[item_set_size].items())
        for item_set, support_suggestion in suggestions:
            for subset in _all_sub_combinations(item_set):
                suggestion = set(item_set).difference(subset)
                support_subset = support_dictionaries[len(subset) - 1][subset]
                confidence = support_suggestion / support_subset
                association_rules.append(
                    (
                        subset,
                        tuple(suggestion),
                        support_subset,
                        support_suggestion,
                        confidence,
                    )
                )
    return association_rules


def frequent(transactions, max_length=None, min_support=1, single_tuples=False):
    support_dictionaries = _get_support_dictionaries(
        transactions, max_length, min_support
    )
    print("creating data_frame")
    frequent_df = pd.DataFrame(
        it.chain(*(d.items() for d in support_dictionaries)), columns=["set", "support"]
    )
    if not single_tuples:
        print("converting single_tuples to scalars")
        frequent_df["set"] = frequent_df["set"].map(lambda x: _tuple_reduce(x))
    return frequent_df


def apriori(
    transactions, max_length=2, min_support=1, min_confidence=0, single_tuples=False
):
    support_dictionaries = _get_support_dictionaries(
        transactions, max_length=max_length, min_support=min_support
    )
    rules = _get_association_rules(support_dictionaries)
    rules_df = pd.DataFrame(
        rules,
        columns=[
            "reason",
            "suggestion",
            "support_reason",
            "support_suggestion",
            "confidence",
        ],
    )
    if not single_tuples:
        rules_df["suggestion"] = rules_df["suggestion"].map(lambda x: _tuple_reduce(x))
        rules_df["reason"] = rules_df["reason"].map(lambda x: _tuple_reduce(x))
    return rules_df
