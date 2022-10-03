
import os
import pandas as pd

base_dir = "G:/Mon Drive/"
df_train = pd.read_csv(base_dir+ 'dataset/train.csv')
df_train.head()

# Create filename.
df_train["img_name"] = df_train["ID"] + "_" + df_train["location"]
df_train.head()


#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# Cleaning Training CSV - It has not useful labels.
train_img_dir = base_dir + "dataset/train/train"
listimg = [e.split('.')[0] for e in os.listdir(train_img_dir)]
df_train = df_train[df_train["img_name"].isin(listimg)]


#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
nperso = df_train['ID'].nunique()
df_train_p_level = df_train.groupby(['ID']).agg({'level': 'max'})
df_train_p_level.groupby(['level']).agg({'level': 'count'})

# Stratified sample of people:
selected_ids_train = df_train_p_level.groupby('level', group_keys=False).apply(lambda x: x.sample(frac=0.8, random_state=1)).index
selected_ids_train_bin = df_train["ID"].isin(selected_ids_train)
selected_ids_train.nunique()

# Save training and validation dataset:
dbfinal_train = df_train[selected_ids_train_bin]
dbfinal_val = df_train[~selected_ids_train_bin]

# Upsample:
dbfinal_train.level.value_counts()
dbfinal_train2 = data_augmentation(dbfinal_train)
dbfinal_train2.level.value_counts()

dbfinal_val.level.value_counts()
dbfinal_val2 = data_augmentation(dbfinal_val)
dbfinal_val2.level.value_counts()

# ::::::::::::::::::::::::::::::::::::::::::::::::
# SAVE
# ::::::::::::::::::::::::::::::::::::::::::::::::
# Organize files in training and testing folder:
mainpath = "G:/Mon Drive/"
df_train.to_csv(mainpath + "dataset/dbfinal_all.csv")

# No upsample datasets:
dbfinal_train.to_csv(mainpath + "dataset/dbfinal_train_NOupsample.csv")
dbfinal_val.to_csv(mainpath + "dataset/dbfinal_test_NOupsample.csv")


print("Done")