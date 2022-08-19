import datetime

import PySimpleGUI as sg

import pandas as pd

from car import Car
from car_fleet import Fleet

def main():
    fleet = Fleet()

    # set colour theme of the GUI package
    sg.theme('DarkGrey2')

    EXCEL_FILE = 'Data_Entry.xlsx.xlsx'
    df = pd.read_excel(EXCEL_FILE)

    layout = [
        # enclose car information form in a frame
        [sg.Frame('Car Info', [
            [sg.Text('Reg Number', size=(15, 1)), sg.InputText(key='reg')],
            [sg.Text('Make', size=(15, 1)), sg.InputText(key='make')],
            [sg.Text('Model', size=(15, 1)), sg.InputText(key='model')],

            # dropdown list of years 2000 to the current year
            [sg.Text('Year', size=(15, 1)),
             sg.Combo(list(range(2000, datetime.datetime.now().year + 1)), default_value=2022, key='year',
                      size=(10, 1))],

            # spinner from 0 to 200,000
            [sg.Text('Mileage', size=(15, 1)), sg.Spin(list(range(0, 201000, 10000)), key='mileage', size=(10, 1))],

            # radio buttons of manual or automatic
            [sg.Text('Gearbox', size=(15, 1)), sg.Radio('Manual', 'GEARBOX_RADIO', default=True, key='gear_man'),
             sg.Radio('Automatic', 'GEARBOX_RADIO', key='gear_auto')],

            # dropdown list of petrol, diesel, and electric
            [sg.Text('Fuel Type', size=(15, 1)),
             sg.Combo(['Petrol', 'Diesel', 'Electric'], key='fuel_type', default_value='Petrol', size=(10, 1))],

            # spinner from 1 to 12
            [sg.Text('Seats', size=(15, 1)), sg.Spin(list(range(1, 13)), key='seats', initial_value=5, size=(10, 1))],
            [sg.Submit(), sg.Exit()]
        ])]
    ]

    window = sg.Window('Rental Information Intake Form', layout)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Exit':
            break

        if event == 'Submit':
            df = df.append(values, ignore_index=True)
            df.to_excel(EXCEL_FILE, index=False)
            sg.popup('Data Saved')

            # TODO: check that all fields have been filled

            new_car = Car(
                values['reg'],
                values['make'],
                values['model'],
                values['year'],
                values['mileage'],
                'Manual' if values['gear_man'] else 'Automatic',
                values['fuel_type'],
                values['seats']
            )

            fleet.add_car(new_car)

            print(f'Car successfully added {new_car.reg} to fleet')

    window.close()
    fleet.cars

def upper_case(reg):
    reg.upper()

if __name__ == '__main__':
    main()




