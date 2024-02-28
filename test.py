import pandas as pd


def clean_address(address, region_strings):
    for region in region_strings:
        address = address.replace(region, "").strip(',').strip().strip(',').strip()
    return address


def strip_address(address):
    return list(filter(None, str(address).replace(',', " ").strip().split(" ")))


def find_region(address, new_data, regions):
    for reg_ct in new_data[:2]:
        for reg in regions:
            if reg in reg_ct:
                data = str(address).replace(reg_ct, '').strip(",").strip().strip(",").strip()
                return reg, data
    return '', address


def find_region_city(region, data):
    df = pd.read_excel('Book1.xlsx')
    
    for index, row in df.iterrows():
        if region in row.iloc[1] and str(row.iloc[0]) in data:
            city = row.iloc[0]
            data = data.replace(city, '').strip(',').strip().strip(",").strip()
            return city, data
    
    return '', data


def check_special_case(region):
    if region == 'Տավուշ':
        return "Այլ"
    return region



def find_city(address, new_data):
    df = pd.read_excel('Book1.xlsx')

    for reg_ct in new_data[:2]:
        mask = df.iloc[:, 0] == reg_ct
        matching_rows = df[mask]

        if not matching_rows.empty:
            city = matching_rows.iloc[0, 0]
            region = matching_rows.iloc[0, 1]
            
            data = str(address).replace(reg_ct, '').strip(",").strip()
            data = data.replace(region, '').strip(",").strip()

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


bank_region("ՀՀ, Նորք Մարաշ,  մ․ ք․ ,Քոչար գ․ փողոց, 51/2/հիսունմեկ կոտորակ երկու/շենք, 13/1/տասներեք կոտորակ մեկ/բնակարան")


