"""
Fixes Hardcoded tray icons in Linux.

Author : Bilal Elmoussaoui (bil.elmoussaoui@gmail.com)
Contributors : Andreas Angerer, Joshua Fogg
Website : https://github.com/bil-elmoussaoui/Hardcode-Tray
Licence : The script is released under GPL, uses a modified script
     form Chromium project released under BSD license
This file is part of Hardcode-Tray.
Hardcode-Tray is free software: you can redistribute it and/or
modify it under the terms of the GNU General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
Hardcode-Tray is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with Hardcode-Tray. If not, see <http://www.gnu.org/licenses/>.
"""
from subprocess import run
from HardcodeTray.modules.svg.svg import SVG, SVGNotInstalled
from HardcodeTray.utils import abs_exec_path, execute


class Inkscape(SVG):
    """Inkscape implemntation of SVG Interface."""

    def __init__(self, colors):
        """Init function."""
        super(Inkscape, self).__init__(colors)

        self.cmd = abs_exec_path(self)
        if not self.is_installed():
            raise SVGNotInstalled

    def convert_to_png(self, input_file, output_file, width=None, height=None):
        """Convert svg to png."""

        is_pre_v1 = run(
            [self.cmd, '--without-gui'], shell=False, timeout=4, check=False
        )

        if is_pre_v1.returncode != 0:
            cmd = [self.cmd, '-o', output_file]
        else:
            cmd = [self.cmd, '-z', '-e', output_file]

        if width and height:
            cmd.extend(['-w', str(width), '-h', str(height)])

        cmd.extend(input_file)
        execute(cmd, False)
