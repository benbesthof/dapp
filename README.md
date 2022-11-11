# dapp

> dappit: Dataset PreProcessor

dapp.standardapp() takes a dataframe and a target and scales numerical data, standardizes categorical values, and normalizes all values.

### Table of Contents
- [Installation](#installation)
- [Usage](#usage)


## Installation

##### Via pip:

    pip install dappit


##### Via Github

    pip install git+https://github.com/sauceboss1526/dapp

## Usage



    from dapp import standarddapp

    standarddapp(
        df:         pandas.DataFrame,
        target:     typing.Union[str, float],
        to_file:    bool = True, 
        filename:   str = 'export.csv')
    )