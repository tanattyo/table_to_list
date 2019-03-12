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
    text = makeDict(df, label)
    print(text)

def makeDict(df, label):

    # 種名によってグルーピング
    grouped = df.groupby(label['label_species']).groups
    all_species_list = {}

    for species in grouped:
        # ある種の標本情報の初期化
        text_info_all_specimens = ''

        for specimen in grouped[species]:
            # ある標本の情報の初期化
            text_info_all_label = ''

            if specimen != 0:
                # ある標本のカテゴリの初期化
                text_info_all_label = ''

                key_label = df.loc[specimen]

                for label_key in label['label_info']:
                    text_info_all_label += str(key_label[label_key])
                text_info_all_label += text_info_all_label
            else:
                print('標本番号ないです')

            text_info_all_specimens += text_info_all_label

        all_specimen_list = {species: text_info_all_specimens}

        all_species_list.update(all_specimen_list)

    return all_species_list

if __name__ == "__main__":
    main()
