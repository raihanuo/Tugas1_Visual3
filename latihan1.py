import PySimpleGUI as sg
window = sg.Window(title="Profile",
                    layout=[
                      [sg.Text("NPM     : 2210010364")],
                      [sg.Text("Nama    : Muhammad Raihan")],
                      [sg.Text("Kelas   : 5B NonReg Banjarmasin")],
                      [sg.Text("Matkul  : Pemrograman Visual 3")],
                    ],
                    size=(400,200),
                  )
window()
window.close()