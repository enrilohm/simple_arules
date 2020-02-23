# simple_arules
Blunt implementation that yields the result of the apriori algorithm.

## Installation
```bash
pip install git+https://github.com/enrilohm/simple_arules.git
```

## Usage
```python
from simple_arules import frequent, apriori
transactions = [["eggs", "bacon", "soup"],
                ["eggs", "bacon", "apple"],
                ["soup", "bacon", "banana"]]
frequent(transactions, max_length=3, min_support=1)
apriori(transactions, max_length=3, min_support=1, min_confidence=0.1)
```
