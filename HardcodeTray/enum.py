#!/usr/bin/python3
"""Fixes Hardcoded tray icons in Linux.

Project: Hardcode-Tray <https://github.com/bil-elmoussaoui/Hardcode-Tray>
SPDX-License-Identifier: GPL-3.0-or-later

Copyright (C) 2017 Bilal Elmoussaoui <bil.elmoussaoui@gmail.com>

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
this program. If not, see <https://www.gnu.org/licenses/>.
"""


class Action:
    """Apply (forcefully) or revert icon changes."""
    APPLY = 1
    REVERT = 2
    CLEAR_CACHE = 3

    @staticmethod
    def choices():
        """Return a dict of different choices."""
        choices = {}
        for choice in Action.__dict__:
            if hasattr(Action, choice):
                try:
                    value = int(getattr(Action, choice))
                    choices[value] = choice
                except (TypeError, ValueError):
                    pass
        return choices


class ConversionTools:
    """Provide the various conversion backends."""
    INKSCAPE = "Inkscape"
    CAIROSVG = "CairoSVG"
    RSVGCONVERT = "RSVGConvert"
    SVGEXPORT = "SVGExport"
    IMAGEMAGICK = "ImageMagick"

    @staticmethod
    def choices():
        """Return a dict of different choices."""
        choices = {}
        for choice in ConversionTools.__dict__:
            if hasattr(ConversionTools, choice):
                value = getattr(ConversionTools, choice)
                if (isinstance(value, str) and
                        choice not in ["__module__", "__doc__"]):
                    choices[value] = choice
        return choices


class ApplicationType:
    """Define the types of supported applications."""
    ELECTRON = "ElectronApplication"
    ZIP = "ZipApplication"
    PAK = "PakApplication"
    NWJS = "NWJSApplication"
    QT = "QtApplication"
    APPLICATION = "Application"

    @staticmethod
    def choices():
        """Return a dict of different choices."""
        choices = {}
        for choice in ApplicationType.__dict__:
            if hasattr(ApplicationType, choice):
                value = getattr(ApplicationType, choice)
                if isinstance(value, str) and choice != "__module__":
                    choices[choice.lower()] = value
        return choices
