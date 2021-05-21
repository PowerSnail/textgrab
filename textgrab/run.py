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


"""textgrab.

Usage:
    textgrab 
    textgrab --version
    textgrab (-h | --help)

Options:
    -h --help           Show help
    --version           Print Version
"""

import docopt
import textgrab
from PySide6 import QtWidgets


def main():
    args = docopt.docopt(__doc__, version=textgrab.__version__)
    app = QtWidgets.QApplication()
    w = textgrab.MainWindow()
    w.show()
    app.exec()


if __name__ == "__main__":
    main()
