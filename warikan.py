# Table: 1500円で3人
# Table: 2000円で3人
# Table: 3647円で4人

# amount = 1500
# number_of_people = 3

amount = int(input("合計金額を教えてください：　"))
number_of_people = int(input("テーブルの人数を教えてください：　"))

print(f"1人あたり: {amount // number_of_people}円, 端数: {amount % number_of_people}円")

# amount = [table_1, table_2, table_3]

# table_1 = 1500
# table_2 = 2000
#table_3 = 3647

# このコードみてどうですか？

amount = 1500
number_of_people = 3

print(f"1人あたり: {amount // number_of_people}円, 端数: {amount % number_of_people}円")

amount = 2000
number_of_people = 3

print(f"1人あたり: {amount // number_of_people}円, 端数: {amount % number_of_people}円")

amount = 3000
number_of_people = 4

print(f"1人あたり: {amount // number_of_people}円, 端数: {amount % number_of_people}円")
