
def drop_columns(df_features_train):
    return df_features_train.drop(columns=['ChannelId_ChannelId_4','ProductCategory_retail','ProductId_ProductId_17',
                                'ProductId_ProductId_18','ProductId_ProductId_25','ProductId_ProductId_26','FraudResult'])
                                 