import pandas as pd

regions = ['Երևան', 'Արմավիր', 'Արարատ', 'Արագածոտն', 'Կոտայք', 'Շիրակ', 'Լոռի', 'Տավուշ', 'Գեղարքունիք', 'Վայոց Ձոր', 'Սյունիք']

region_strings = ["ք․", "ք.", "Ք․", "Ք.", "քաղաք", "Քաղաք", "մ․", "մ.", "Մ․", "Մ.", "մարզ", "Մարզ", "ՀՀ", "հհ", 'համայնք', 'գյուղ', "գ․", "հ․"]

double = ['Նոր Նորք', 'Զեյթուն', 'Մալաթիա', "Մարաշ"]

def bank_region(address):

    num = 10
    for qaxaq in region_strings:
        if qaxaq in address:
            address = address.replace(qaxaq, "").strip(",").strip().strip(",").strip()

    new_data = str(address).replace(',', " ").strip().split(" ")
    for i in range(len(new_data)):
        if '' in new_data:
            new_data.remove('')

    for reg_ct in new_data[0:2]:
        for reg in regions:
            if reg in reg_ct:
                data = str(address).replace(reg_ct, '').strip(",").strip().strip(",").strip()
                region = reg
                regions.pop(0)
                regions.pop(0)
                num -= 2
                df = pd.read_excel('Book1.xlsx')
                for i in range(len(df.values)):
                    if region in df.values[i][1]:
                        if str(df.values[i][0]) in data:
                            city = df.values[i][0]
                            data = data.replace(city, '').strip(",").strip().strip(",").strip()
                            num -= 2
    print(num)

    if num == 10:
        for reg_ct in new_data[0:2]:
            df = pd.read_excel('Book1.xlsx')
            for i in range(len(df.values)):
                if str(df.values[i][0]) == reg_ct:
                    city = df.values[i][0]
                    data = str(address).replace(reg_ct, '').strip(",").strip().strip(",").strip()
                    region = df.values[i][1]
                    regions.pop(0)
                    data = str(data).replace(region, '').strip(",").strip().strip(",").strip()
                    num -= 1
    print(num)

    if num == 10:
        for ct in double:
            if ct in address:
                if ct == "Զեյթուն":
                    city = "Քանաքեռ-Զեյթուն"
                elif ct == "Մալաթիա":
                    city = "Մալաթիա-Սեբաստիա"
                elif ct == "Մարաշ":
                    city = "Նորք-Մարաշ"
                else:
                    city = ct
                region = "Երևան"
                data = str(address).replace(city, '').strip(",").strip().strip(",").strip()
                num -= 1
    print(num)
    if num == 8:
        if region == 'Տավուշ':
            city = "Այլ"
        else:
            city = region
        num -= 1

    print(num)

    if num == 10:
        region ='Երևան'
        city ='Երևան'
        data = address
        num -= 1
    print(num)

    print(region)
    print(city)
    print(data)


bank = bank_region("Գորիս, Պ. Սևակի փողոց 51/2/հիսունմեկ կոտորակ երկու/շենք, 13/1/տասներեք կոտորակ մեկ/բնակարան")


