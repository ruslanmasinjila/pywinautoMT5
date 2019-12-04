from pywinauto.application import Application
import subprocess
import time




mt5_launcher = r"C:\MT5\mt5_demo\terminal64.exe"

configuration_file = r"C:\forex\configuration files\configuration.ini"

mt5_terminal = subprocess.Popen([mt5_launcher,"/config:",configuration_file,"/portable"],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)

app = Application().connect(process=mt5_terminal.pid)

time.sleep(2)

app['3000012389 - Darwinex-Demo: Demo Account - Hedge'].menu_select("File->New Chart->AUDCAD")

app['3000012389 - Darwinex-Demo: Demo Account - Hedge'].menu_select("Insert->Expert->Atratx")

app['Atratx 1.00'].OK.click()

#  app['Atratx 1.00'].print_control_identifiers()