import pandas as pd


def clean_address(address, region_strings):
    for qaxaq in region_strings:
        if qaxaq in address:
            address = address.replace(qaxaq, "").strip(",").strip().strip(",").strip()
    return address


def strip_address(address):
    new_data = str(address).replace(',', " ").strip().split(" ")
    for i in range(len(new_data)):
        if '' in new_data:
            new_data.remove('')
    return new_data


def find_region(address, new_data, regions):
    for reg_ct in new_data[0:2]:
        for reg in regions:
            if reg in reg_ct:
                data = str(address).replace(reg_ct, '').strip(",").strip().strip(",").strip()
                region = reg
                return region, data
    return '', address


def find_region_city(region, data):
    df = pd.read_excel('Book1.xlsx')
    for i in range(len(df.values)):
        if region in df.values[i][1]:
            if str(df.values[i][0]) in data:
                city = df.values[i][0]
                data = data.replace(city, '').strip(",").strip().strip(",").strip()
                return city, data
    return '', data


def check_special_case(region):
    if region == 'Տավուշ':
        city = "Այլ"
    else:
        city = region
    return city


def find_city(address, new_data):
    for reg_ct in new_data[0:2]:
        df = pd.read_excel('Book1.xlsx')
        for i in range(len(df.values)):
            if str(df.values[i][0]) == reg_ct:
                city = df.values[i][0]
                data = str(address).replace(reg_ct, '').strip(",").strip().strip(",").strip()
                region = df.values[i][1]
                data = str(data).replace(region, '').strip(",").strip().strip(",").strip()
                return region, city, data
    return '', '', address


def find_region_in_double(address):
    global region, city, data
    double = ['Նոր Նորք', 'Զեյթուն', 'Մալաթիա', "Մարաշ"]
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
            return region, city, data
    return '', '', address

def check_default_case(address):
    global region, city, data
    region = 'Երևան'
    city = 'Երևան'
    data = address
    return region, city, data


def bank_region(address):
    regions = ['Երևան', 'Արմավիր', 'Արարատ', 'Արագածոտն', 'Կոտայք', 'Շիրակ', 'Լոռի', 'Տավուշ', 'Գեղարքունիք', 'Վայոց',
               'Սյունիք']
    region_strings = ["ք․", "ք.", "Ք․", "Ք.", "քաղաք", "Քաղաք", "մ․", "մ.", "Մ․", "Մ.", "մարզ", "Մարզ", "ՀՀ", "հհ",
                      "գ․", "գ.", "Գ․", "Գ.", "գյուղ", "Գյուղ", "հ․", "հ.", "Հ․", "Հ.", "համայնք", "Համայնք"]

    address = clean_address(address, region_strings)
    new_data = strip_address(address)

    region, data = find_region(address, new_data, regions)
    if region:
        print(region)
        city, data = find_region_city(region, data)
        if city:
            print(city)
            print(data)
        else:
            city = check_special_case(region)
            print(city)
            print(data)
    else:
        region, city, data = find_city(address, new_data)
        if region:
            print(region)
            print(city)
            print(data)
        if not region:
            region, city, data = find_region_in_double(address)
            if region:
                print(region)
                print(city)
                print(data)
            else:
                region, city, data = check_default_case(address)
                print(region)
                print(city)
                print(data)

    if region == 'Վայոց':
        region = 'Վայոց Ձոր'
        data = address.replace(region, "").strip(",").strip().strip(",").strip()
        if city == 'Վայոց':
            city = 'Վայոց Ձոր'
        else:
            data = data.replace(city, "").strip(",").strip().strip(",").strip()
        print(region)
        print(city)
        print(data)


bank_region("Երևան Արաբկիր մ․ ք․ ,Քոչար գ․ փողոց, 51/2/հիսունմեկ կոտորակ երկու/շենք, 13/1/տասներեք կոտորակ մեկ/բնակարան")


