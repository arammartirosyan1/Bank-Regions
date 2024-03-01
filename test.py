import pandas as pd


def clean_address(address, region_strings):
    for region in region_strings:
        address = address.replace(region, "").strip(',').strip().strip(',').strip()
    if 'Վայոց Ձոր' in address.title():
        region = 'Վայոց Ձոր'
        data = address.replace(region, "") .strip(',').strip().strip(',').strip()
        return region, '', data
    else:
        double_cities = {
            "Նոր Նորք": "Նոր Նորք",
            "Զեյթուն": "Քանաքեռ-Զեյթուն",
            "Մալաթիա": "Մալաթիա-Սեբաստիա",
            "Մարաշ": "Նորք-Մարաշ"
        }
        for city, city_alias in double_cities.items():
            if city in str(address).title():
                region = "Երևան"
                city = city_alias
                data = address.replace(city, '').strip(",").strip().strip(",").strip()
                data = data.replace(region, '').strip(",").strip().strip(",").strip()
                return region, city, data
    return '', '', address


def strip_address(address):
    return list(filter(None, str(address).replace(',', " ").strip().split(" ")))


def find_region(address, new_data, regions):
    for reg_ct in new_data[:2]:
        for reg in regions:
            if reg in str(reg_ct).title():
                data = str(address).replace(reg_ct, '').strip(",").strip().strip(",").strip()
                return reg, data
    return '', address


def find_region_city(region, data):
    df = pd.read_excel('Book1.xlsx')
    for index, row in df.iterrows():
        if region in row.iloc[1] and str(row.iloc[0]) in str(data).title():
            city = row.iloc[0]
            data = data.replace(city, '').strip(',').strip().strip(",").strip()
            return city, data
    return '', data


def check_special_case(region):
    if region == 'Տավուշ':
        return "Այլ"
    return region


def find_city(data, new_data):
    df = pd.read_excel('Book1.xlsx')
    for reg_ct in new_data[:2]:
        mask = df.iloc[:, 0] == reg_ct
        matching_rows = df[mask]
        if not matching_rows.empty:
            city = matching_rows.iloc[0, 0]
            region = matching_rows.iloc[0, 1]
            data = str(data).replace(reg_ct, '').strip(",").strip()
            data = data.replace(region, '').strip(",").strip()
            return region, city, data
    return '', '', data


def check_default_case(address):
    return 'Երևան', 'Երևան', address


def bank_region(address):
    regions = ['Երևան', 'Արմավիր', 'Արարատ', 'Արագածոտն', 'Կոտայք', 'Շիրակ', 'Լոռի', 'Տավուշ', 'Գեղարքունիք', 'Վայոց',
               'Սյունիք']
    region_strings = ["ք․", "ք.", "Ք․", "Ք.", "քաղաք", "Քաղաք", "մ․", "մ.", "Մ․", "Մ.", "մարզ", "Մարզ", "ՀՀ", "հհ",
                      "գ․", "գ.", "Գ․", "Գ.", "գյուղ", "Գյուղ", "հ․", "հ.", "Հ․", "Հ.", "համայնք", "Համայնք"]

    region, city, data = clean_address(address, region_strings)
    if region and city:
        return region, city, data
    elif region:
        if not city:
            city, data = find_region_city(region, data)
            if city:
                return region, city, data
            else:
                city = check_special_case(region)
                return region, city, data
    else:
        new_data = strip_address(data)
        region, data = find_region(data, new_data, regions)
        if region:
            city, data = find_region_city(region, data)
            if city:
                return region, city, data
            else:
                city = check_special_case(region)
                return region, city, data
        else:
            region, city, data = find_city(data, new_data)
            if region:
                return region, city, data
            else:
                region, city, data = check_default_case(data)
                return region, city, data


def print_bank_region(address):
    region, city, data = bank_region(address)
    print("Region:", region)
    print("City:", city)
    print("Data:", data)


print_bank_region("ՀՀ Արաբկիր մ․ ք․ ,Քոչար գ․ փողոց, 51/2/հիսունմեկ կոտորակ երկու/շենք, 13/1/տասներեք կոտորակ մեկ/բնակարան")


