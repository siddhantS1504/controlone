import csv
class WarehouseParcelDetail:
    def __init__(self, parcel_number, parcel_weight, parcel_category):
        self.parcel_number = parcel_number
        self.parcel_weight = parcel_weight
        self.parcel_category = parcel_category
    def save_and_display_parcel_details(self, parcels):
        category_parcels = {}
        for parcel in parcels:
            if parcel.parcel_category not in category_parcels:
                category_parcels[parcel.parcel_category] = []
            category_parcels[parcel.parcel_category].append(parcel.parcel_number)
        categories = list(category_parcels.keys())
        values = list(category_parcels.values())
        num_rows = len(values[0])
        num_columns = len(categories)
        print('\t'.join(categories))
        for i in range(num_rows):
            row = [str(values[j][i]) for j in range(num_columns)]
            print('\t'.join(row))
        with open('parcel_details.csv', mode='w', newline='') as file:
            writer = csv.writer(file,delimiter=',')
            writer.writerow(categories)
            for i in range(len(category_parcels['Filters'])):
                row = [category_parcels[key][i] for key in category_parcels]
                writer.writerow(row)
parcels = []
with open('data.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        parcel = WarehouseParcelDetail(
            int(row['Parcel Number']),
            int(row['Parcel Weight (kg)']),
            row['Parcel Category']
        )
        parcels.append(parcel)
warehouse = WarehouseParcelDetail(None, None, None)
warehouse.save_and_display_parcel_details(parcels)
