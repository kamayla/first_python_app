import csv
import os

name = ''
name = input("""\
##########################################################################
こんにちわ！私はロボットです。あなたの名前はなんですか？
##########################################################################
""")

if os.path.exists('ranking.csv'):
    with open('ranking.csv', 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        out_data = []
        for row in reader:
            out_row = {'name': row['name'], 'count': row['count']}
            out_data.append(out_row)
        sort_data = sorted(out_data, key=lambda x: int(x['count']), reverse=True)
        for line in sort_data:
            while True:
                answer = input("""\
                            ##########################################################################
                            私のオススメのレストランは{}です。

                            このレストランは好きですか？　[Yes/No]
                            ##########################################################################
                            """.format(line['name']))
                if answer.capitalize() == 'Yes':
                    print('Yes')
                    line['count'] = int(line['count']) + 1
                    break
                elif answer.capitalize() == 'No':
                    print('No')
                    break
        print(sort_data)
        with open('ranking.csv', 'w') as f:
            fieldnames = ['name', 'count']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for update_data in sort_data:
                writer.writerow({'name': update_data['name'], 'count': update_data['count']})


restaurant = input("""\
##########################################################################
{}さん。どこのレストランが好きですか？
##########################################################################
""".format(name))

print("""\
##########################################################################
{}さん。ありがとうございました。

良い一日を！さようなら！
##########################################################################
""".format(name))

cp_restaurant = restaurant.capitalize()

if os.path.exists('ranking.csv'):
    with open('ranking.csv', 'r+') as csv_f:
        reader = csv.DictReader(csv_f)
        exist_flag = False
        data = []
        for row in reader:
            data.append(row)
            if row['name'] == cp_restaurant:
                exist_flag = True
                print('あった')
        if not exist_flag:
            with open('ranking.csv', 'a') as csv_f:
                print('aaa')
                fieldnames = ['name', 'count']
                writer = csv.DictWriter(csv_f, fieldnames=fieldnames)
                writer.writerow({'name': cp_restaurant, 'count': 1})
        else:
            print('sine')
            with open('ranking.csv', 'w') as csv_file:
                fieldnames = ['name', 'count']
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()
                for line in data:
                    if line['name'] == cp_restaurant:
                        line['count'] = int(line['count']) + 1
                    writer.writerow({'name': line['name'], 'count': line['count']})
else:
    with open('ranking.csv', 'w') as csv_f:
        fieldnames = ['name', 'count']
        writer = csv.DictWriter(csv_f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({'name': cp_restaurant, 'count': 1})

