import os
import csv


def return_float_body_whl(body_whl):
    res = body_whl.split("x", 2)
    try:
        for i in range(3):
            res[i] = res[i].strip()
            res[i] = float(res[i])
    except ValueError:
        res = [0.0, 0.0, 0.0]

    return res


class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.car_type = ''
        self.photo_file_name = photo_file_name
        self.brand = brand
        self.carrying = float(carrying)

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]


class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = "car"
        self.passenger_seats_count = int(passenger_seats_count)


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'truck'

        res = return_float_body_whl(body_whl)
        self.body_width = float(res[1])
        self.body_height = float(res[2])
        self.body_length = float(res[0])

    def get_body_volume(self):
        return self.body_length * self.body_width * self.body_height


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'spec_machine'
        self.extra = extra


def validation(row):
    # Проверка наличия непустых обязательных полей      +
    # Проверка правильности форматов фотографий         +
    # Проверка верности грузоподьемности                +

    if row[1] == '':
        return False
    elif row[3] == '':
        return False
    elif row[5] == '':
        return False

    if not (os.path.splitext(row[3])[1] == '.jpg' or
            os.path.splitext(row[3])[1] == '.jpeg' or
            os.path.splitext(row[3])[1] == '.png' or
            os.path.splitext(row[3])[1] == '.gif'):
        return False
    elif os.path.splitext(row[3])[0] == '':
        return False

    try:
        float(row[5])
    except ValueError:
        return False

    return True


def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)
        for row in reader:
            if row[0] == 'car':
                if not validation(row):
                    continue
                try:
                    n = int(row[2])
                except ValueError:
                    continue
                car = Car(row[1], row[3], row[5], n)
                car_list.append(car)

            elif row[0] == 'truck':
                if not validation(row):
                    continue
                truck = Truck(row[1], row[3], row[5], row[4])
                car_list.append(truck)

            elif row[0] == 'spec_machine':
                if not validation(row):
                    continue
                if row[6] == '':
                    continue
                spec_machine = SpecMachine(row[1], row[3], row[5], row[6])
                car_list.append(spec_machine)

            else:
                continue

    return car_list
