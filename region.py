"""import pandas as pd


def clean_address1(address, region_strings1):
    for region in region_strings1:
        if region in address:
            address = address.replace(region, "").strip(',').strip().strip(',').strip()
            print(address)
            return address


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


def bank_region1(region, address):
    region_strings = ["ք․", "ք.", "Ք․", "Ք.", "քաղաք", "Քաղաք", "մ․", "մ.", "Մ․", "Մ.", "մարզ", "Մարզ", "ՀՀ", "հհ",
                      "գ․", "գ.", "Գ․", "Գ.", "գյուղ", "Գյուղ", "հ․", "հ.", "Հ․", "Հ.", "համայնք", "Համայնք"]

    address = clean_address1(address, region_strings)
    print(1)

    city, data = find_region_city(region, address)
    if city:
        return city, data
    else:
        city = check_special_case(region)
        return city


def print_bank_region1(region, address):
    city, data = bank_region1(region, address)
    print(city)
    print(data)


print_bank_region1("Երևան", "ՀՀ Արաբկիր մ․ ք․ ,Քոչար գ․ փողոց, 51/2/հիսունմեկ կոտորակ երկու/շենք, 13/1/տասներեք կոտորակ մեկ/բնակարան")
"""








def clean_address1(address):
    region_strings = ["ք․", "ք.", "Ք․", "Ք.", "քաղաք", "Քաղաք", "մ․", "մ.", "Մ․", "Մ.", "մարզ", "Մարզ", "ՀՀ", "հհ",
                      "գ․", "գ.", "Գ․", "Գ.", "գյուղ", "Գյուղ", "հ․", "հ.", "Հ․", "Հ.", "համայնք", "Համայնք"]

    for r in region_strings:
        print(r)
        print(address)
        address = address.replace(r, "").strip(',').strip().strip(',').strip()
    print(address)
    return address




clean_address1("ՀՀ Արաբկիր մ․ ք․ ,Քոչար գ․ փողոց, 51/2/հիսունմեկ կոտորակ երկու/շենք, 13/1/տասներեք կոտորակ մեկ/բնակարան")
