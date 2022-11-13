# GloFlow application and media management/publishing platform
# Copyright (C) 2022 Ivan Trajkovic
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

import os, sys
modd_str = os.path.abspath(os.path.dirname(__file__)) # module dir

#--------------------------------------------------
def build():
    
    print("build docs")

    build_dir_str = f"{modd_str}/../build"
    docs_dirs_lst = [
        (f"{modd_str}/../docs",     f"{modd_str}/../build"),
        (f"{modd_str}/../docs/p2p", f"{modd_str}/../build/p2p")
    ]

    for d_str, d_build_str in docs_dirs_lst:
        
        os.system(f"mkdir -p {d_build_str}")

        for f_str in os.listdir(d_str):
            if f_str.endswith(".md"):

                cmd_str = f"mkd2html {d_str}/{f_str} {d_build_str}/{f_str.split('.')[0]}.html"
                print(cmd_str)

                os.system(cmd_str)


#--------------------------------------------------
if __name__ == "__main__":
    build()