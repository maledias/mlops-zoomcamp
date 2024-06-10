from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LinearRegression

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer

@transformer
def transform(df, *args, **kwargs):
    print("test")
    df.loc[:, "PULocationID"] = df["PULocationID"].astype(str)
    df.loc[:, "DOLocationID"] = df["DOLocationID"].astype(str)
    locations_ids = df[["PULocationID", "DOLocationID"]]
    vectorizer = OneHotEncoder(handle_unknown="ignore")
    X = vectorizer.fit_transform(locations_ids)
    y = df["duration"]
    model = LinearRegression()
    model.fit(X, y)
    print(model.intercept_)
    return model, vectorizer