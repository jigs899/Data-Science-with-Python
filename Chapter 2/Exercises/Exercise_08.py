# Exercise 8: Preparing data for support vector classifier

# clear environment prior to running this code

# import data
import pandas as pd
df = pd.read_csv('weather.csv')

# dummy code 'Summary'
import pandas as pd
df_dummies = pd.get_dummies(df, drop_first=True)

# shuffle df_dummies
from sklearn.utils import shuffle
df_shuffled = shuffle(df_dummies, random_state=42)

# split df_shuffled into X and y
DV = 'Rain' # Save the DV as DV
X = df_shuffled.drop(DV, axis=1) # get features (X)
y = df_shuffled[DV] # get DV (y)

# scale X
from sklearn.preprocessing import StandardScaler
model = StandardScaler() # instantiate StandardScaler model
X_scaled = model.fit_transform(X) # transform the features to z-scores

# split X and y into testing and training data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.33, random_state=42)



