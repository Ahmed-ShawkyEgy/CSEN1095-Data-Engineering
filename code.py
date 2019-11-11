# i = 0
# meta = pd.read_excel('data/microbiome/metadata.xls')
# while(i < 9):
#     i= i + 1
#     fileName = 'data/microbiome/MID' + str(i) + '.xls'
#     df = pd.read_excel(fileName, names=['name', 'index'])
#     midString = 'MID' + str(i)
#     df['BARCODE'] = midString
#     resultMerge = pd.merge(df, meta)
#     if(i == 1):
#         result = resultMerge
#     else:
#         result = result.append(resultMerge)
    
# result.to_csv("data/microbiome/result.xls")
i=0
meta = pd.read_excel('data/microbiome/metadata.xls')
# for col in meta.columns: 
#     print(col)
print(meta.columns[1])
for i in range(9):
    midString = 'MID' + str(i+1)
    fileName = 'data/microbiome/MID' + str(i+1) + '.xls'
    index = meta.index[meta['BARCODE'] == midString].tolist()[0]
#     print(meta['SAMPLE'][index])
    columnName = meta['GROUP'][index] + "_" + str(meta['SAMPLE'][index])
    df = pd.read_excel(fileName, names=['name', columnName])
    if i == 0:
        result = df
    else:
        result = pd.merge(result, df, how='outer', on='name')
    
result
