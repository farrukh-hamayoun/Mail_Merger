PLACEHOLDER = "[Name]"
# with open("data.txt") as f_data:
#     f_data.readline()


with open("name.txt") as rd:
    name_list = rd.readlines()

with open("data.txt") as rd_data:
    Letter_content = rd_data.read()
    for name in name_list:
        n_name = name.strip()
        new_letter = Letter_content.replace(PLACEHOLDER, n_name)
        with open(f"./data/{n_name}.txt", mode="w") as new_name:
            new_name.write(new_letter)