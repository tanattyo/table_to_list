import pandas as pd
import sys

def main():

    args = put_csv_file_name()

    csv_file_name = args[1]
    species_name_list = args[2:]

    df = load_csv_file(csv_file_name)
    label = get_necessary_label()
    all_species_list = create_dictionary(df, label)
    print(species_name_list)

    if len(species_name_list) != 0:
        show_species_info(all_species_list, species_name_list)
    else:
        show_all_species_info(all_species_list)

def put_csv_file_name():

    args = sys.argv
    return(args)

def load_csv_file(csv_file):

    df = pd.read_csv(csv_file)
    return(df)

def get_necessary_label():

    # 検索keyとなる列の指定
    label_species = 'name'

    # 抽出したい列の指定
    label_info = [
        'number',
        'condition',
        'num',
        'locality',
        'date',
        'collector',
        'status_ed'
    ]

    label = {
        'label_species': label_species,
        'label_info': label_info,
    }
    return label

def create_dictionary(df, label):

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
            if df.loc[specimen]['number'] != 0:
                # ある標本のカテゴリの初期化
                text_info_all_label = ''

                key_label = df.loc[specimen]

                i = 0
                for label_key in label['label_info']:

                    # stateだったら"state:"を入れるとか，個別の件をここに入力してもいいかも
                    if str(key_label[label_key]) != 'nan':
                        if label_key == 'collector':
                            text_info_all_label += 'Collector. '
                        elif label_key == 'locality':
                            text_info_all_label += 'Locality. '
                        elif label_key == 'date':
                            text_info_all_label += 'Date. '
                        elif label_key == 'status_ed':
                            text_info_all_label += 'Remarks. '

                    # labelをテキストに追加
                    text_info_all_label += str(key_label[label_key])

                    # 個体数の表示
                    if str(key_label[label_key]) != 'nan':
                        if label_key == 'num':
                            try:
                                if int(key_label[label_key]) == 1:
                                    text_info_all_label += ' specimen\n   '
                                elif int(key_label[label_key]) > 1:
                                    text_info_all_label += ' specimens\n   '
                            except:
                                text_info_all_label += ' specimen(s)\n   '

                    # label数-1の分だけ","を入れる
                    if i == len(label['label_info'])-1:
                        break
                    text_info_all_label += ', '
                    i += 1

            else:
                text_info_all_label = '[NO SPECIMEN NUMBER!!]'
                print(specimen)

            text_info_all_specimens += text_info_all_label
            # 標本数-1の分だけ";"を入れる
            if j == len(grouped[species]) - 1:
                break
            text_info_all_specimens += '\n'
            j += 1

        text_info_all_specimens_formatted = format_specimen_info(text_info_all_specimens)
        all_specimen_list = {species: text_info_all_specimens_formatted}

        all_species_list.update(all_specimen_list)

    return all_species_list

def format_specimen_info(text):

    # 出力についてテキストで一括でいじれる部分はここで弄る
    formatted_text = text.replace('\u3000', '').replace(' ,', ',').replace(', nan', '').replace('\r\n', ' ').replace('  , ', '     ')
    return formatted_text

def show_species_info(all_species_list, name_list):

    # argsのリスト数は可変
    for i in name_list:
        try:
            print('>' + i + '\n' + all_species_list[i])
        except:
            print('>' + i + '\n' + 'ラベルが存在しません')

def show_all_species_info(all_species_list):

    for species, text in all_species_list.items():
#        print('>' + species + '\n' + text)
        print('>' + species + '\n')

if __name__ == "__main__":
    main()
