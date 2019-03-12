import pandas as pd

def LoadCsv(urls_tsv):
    df = pd.read_csv(urls_tsv)
    return(df)

def SetRequiredLabel():
    label_species = 'name'
    label_info = [
        'number',
        'locality',
        'date',
    ]
    label = {
        'label_species': label_species,
        'label_info': label_info,
    }
    return label

def main():
    # urlを設定する
    url = 'test.csv'
    df = LoadCsv(url)
    label = SetRequiredLabel()
    print('データセットの内訳は:' + str(df.shape))
    # 種名によってグルーピング
    grouped = df.groupby(label[0]).groups

    for species in grouped:
        print(species)
        for specimen in grouped[species]:
            if specimen != 0:
                i = df.loc[specimen]
                for label_category in label[1]:
                    print(i[label_category])
            else:
                print('標本番号ないです')

if __name__ == "__main__":
    main()
