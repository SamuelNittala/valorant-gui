import PySimpleGUI as sg
from layout import layout
from db import insert_into_table
from helper import formatfordb

window = sg.Window("Valorant", layout=layout)

while True:
    event, values = window.read()

    if event == "Submit":
        agent = values[0] 
        ability = formatfordb(values[1])
        side = formatfordb(values[2])
        map = formatfordb(values[3])
        area = values[4]
        url = formatfordb(values[5])
        insert_into_table(agent,ability,side,map,area,url)
        break
    if event == sg.WIN_CLOSED:
        break

window.close()
