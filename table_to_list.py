import pandas as pd
import sys

def SetCsvFileName():

    args = sys.argv
    return(args[1])

def LoadCsv(csv_file):

    df = pd.read_csv(csv_file)
    return(df)

def SetRequiredLabel():

    # 検索keyとなる列の指定
    label_species = 'name'

    # 抽出したい列の指定
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

def makeDict(df, label):

    # 種名によってグルーピング
    grouped = df.groupby(label['label_species']).groups
    all_species_list = {}

    for species in grouped:
        # ある種の標本情報の初期化
        text_info_all_specimens = ''

        j = 0
        for specimen in grouped[species]:
            # ある標本の情報の初期化
            text_info_all_label = ''

            if specimen != 0:
                # ある標本のカテゴリの初期化
                text_info_all_label = ''

                key_label = df.loc[specimen]

                i = 0
                for label_key in label['label_info']:
                    text_info_all_label += str(key_label[label_key])

                    # label数-1の分だけ","を入れる
                    if i == len(label['label_info'])-1:
                        break
                    text_info_all_label += ', '
                    i += 1
            else:
                text_info_all_label = '[NO SPECIMEN NUMBER!!]'

            text_info_all_specimens += text_info_all_label
            # 標本数-1の分だけ";"を入れる
            if j == len(grouped[species]) - 1:
                break
            text_info_all_specimens += '; '
            j += 1

        text_info_all_specimens_formatted = formatingList(text_info_all_specimens)
        all_specimen_list = {species: text_info_all_specimens_formatted}

        all_species_list.update(all_specimen_list)

    return all_species_list

def formatingList(text):

    # 出力についてテキストで一括でいじれる部分はここで弄る
    formatted_text = text.replace('\u3000', '').replace(' ,', ',').replace(', nan', '').replace('\r\n', ' ')
    return formatted_text

def printSpeciesInfo(all_species_list):

    print('学名を入力（終了はquitを入力）')
    while 1:
        print('>')
        name = input()
        if name == 'quit':
            break
        print(all_species_list[name])
    print('finish')

def main():

    url = SetCsvFileName()
    df = LoadCsv(url)
    label = SetRequiredLabel()
    all_species_list = makeDict(df, label)
    printSpeciesInfo(all_species_list)

if __name__ == "__main__":
    main()
