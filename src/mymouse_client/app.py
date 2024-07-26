"""
My first application
"""

import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]


def postkey(key, ip, mode="lower"):  # mode: upper, lower
    print("{key}, {ip}, {mode}".format(key=key, ip=ip, mode=mode))


class MyMouseClient(toga.App):
    def startup(self):
        self.ip = toga.TextInput(placeholder="IP")
        buttonlist = [
            toga.Button(
                text=i, on_press=lambda i: postkey(key=i.text, ip=self.ip.value)
            )
            for i in alphabet
        ]
        content = toga.Box(children=[self.ip])
        for button in buttonlist:
            content.add(button)
        container = toga.ScrollContainer(content=content)
        # main_box = toga.Box([container])

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = container
        self.main_window.show()


def main():
    return MyMouseClient()
