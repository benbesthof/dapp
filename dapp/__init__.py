
import typing
import pandas as pd
from sklearn import preprocessing as pre


def standarddapp(df: pd.DataFrame, target: typing.Union[str, float], to_file: bool = True, filename: str = 'export.csv'):
    numerical_variables = list(df.select_dtypes(exclude = object))
    no_var = []
    for i in numerical_variables:
        if df[i].std() == 0:
            no_var.append(i)
    numerical_variables = list(set(numerical_variables) - set(no_var))

    categorical_variables = list(set(df.select_dtypes(include = object)) - set(df[target]))
    high_card = []
    for i in categorical_variables:
        if len(df[i].value_counts().index) > 200:
            high_card.append(i)
    low_card = []
    for i in categorical_variables:
        if len(df[i].value_counts().index) == 1:
            low_card.append(i)

    categorical_variables = list(set(categorical_variables) - set(high_card) - set(low_card))

    df = df.drop(no_var, axis = 1)
    df = df.drop(low_card, axis = 1)
    df = df.drop(high_card, axis = 1)

    scaled_numerical_variables = [i for i in numerical_variables]
    array = df[numerical_variables].values
    datascaler = pre.MinMaxScaler(feature_range = (0 ,1))
    df[scaled_numerical_variables] = pd.DataFrame(datascaler.fit_transform(array), columns = scaled_numerical_variables)

    dummy_cat_df = pd.get_dummies(df[categorical_variables], drop_first = True)
    df_p = df.drop(categorical_variables, axis = 1)
    df_p[target] = df[target]
    df_p = pd.concat([df_p, dummy_cat_df], axis = 1)

    df_p.loc[(df_p[target] == 'Yes') | (df[target] == True), target] = 1
    df_p.loc[(df_p[target] == 'No') | (df[target] == False), target] = 0

    if to_file:
        df_p.to_csv(filename)
        return df_p
    else:
        return df_p.to_csv()