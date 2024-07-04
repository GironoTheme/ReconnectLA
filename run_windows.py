import win32com.client
import win32con
import win32gui
from go_to_world import go_to_world


class RunWindows:
    def __init__(self):
        self.windows_process = []
        self.NAME_OF_WINDOW = 'Lineage2M'

    def switch_windows(self):
        shell = win32com.client.Dispatch("WScript.Shell")

        windows_list = self.__find_windows()

        if windows_list:
            for index, window in enumerate(windows_list):
                if windows_list[index] in self.windows_process:
                    continue

                self.windows_process.append(windows_list[index])

                for i in range(3):
                    shell.SendKeys('%')
                win32gui.ShowWindow(window, win32con.SW_RESTORE)
                win32gui.SetForegroundWindow(window)

                go_to_world.manipulations_in_window(window)

    def __find_windows(self):
        def __is_toplevel(hwnd):
            return win32gui.GetParent(hwnd) == 0 and win32gui.IsWindowVisible(hwnd)

        hwnd_list = []

        win32gui.EnumWindows(lambda hwnd, param: param.append(hwnd) if __is_toplevel(hwnd) else None, hwnd_list)

        lst_processes = [hwnd for hwnd in hwnd_list if self.NAME_OF_WINDOW in win32gui.GetWindowText(hwnd)]

        return lst_processes


run_windows = RunWindows()
