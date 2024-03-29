import PySimpleGUI as sg
import pandas as pd 

sg.theme('DarkGreen 4' )

EXCEL_FILE = 'Data Diri.xlsx'

df = pd.read_excel(EXCEL_FILE)

layout=[
[sg.Text('Masukan Data Kamu: ')],
[sg.Text('Nama', size=(15,1)), sg.InputText(key='Nama')],
[sg.Text('Alamat', size=(15,1)), sg.InputText(key='Alamat')],
[sg.Text('Jenis Kelamin ', size=(15,1)), sg.Combo(['Laki-laki', 'Perempuan'], key = 'Jenis Kelamin')],
[sg.Text('No Telp', size=(15,1)), sg.InputText(key='No Telp')],
[sg.Text('Tanggal Lahir', size=(15,1)), sg.InputText(key='Tanggal Lahir')],
[sg.Text('Hobi', size=(15,1)), sg.InputText(key='Hobi')],

[sg.Submit(), sg.Button ('Clear '), sg.Exit()]
]

window = sg.Window('Form Data Diri',layout)

def clear_input():
    for key in values :
        window[key]('')
        return None

while True : 
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'EXIT':
        break
    if event == 'Clear':
        clear_input()
    if event == 'Submit':
        df = df.append(values, ignore_index= True)
        df.to_excel(EXCEL_FILE, index = False)
        sg.popup('Data Berhasil Di Simpan')
        clear_input()
window.close ()
 
