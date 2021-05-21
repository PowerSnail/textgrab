# Copyright (C) 2021 PowerSnail
#
# This file is part of textgrab.
#
# textgrab is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# textgrab is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with textgrab.  If not, see <http://www.gnu.org/licenses/>.

import typing as T

from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt

from . import ui_mainwindow


class MainWindow(QtWidgets.QMainWindow):
    def __init__(
        self,
        parent: T.Optional[QtWidgets.QWidget] = None,
        flags: Qt.WindowFlags = Qt.WindowFlags(),
    ):
        super().__init__(parent=parent, flags=flags)
        ui_mainwindow.Ui_MainWindow().setupUi(self)

    def showEvent(self, event: QtGui.QShowEvent):
        super().showEvent(event )
