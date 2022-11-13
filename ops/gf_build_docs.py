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

import jinja2

#--------------------------------------------------
def build():
    
    print("build docs")

    table_of_contents_target_file_str = f"{modd_str}/../static/table_of_contents.html"
    docs_dirs_lst = [
        ("main", f"{modd_str}/../docs",     f"{modd_str}/../static",     "/docs"),
        ("p2p",  f"{modd_str}/../docs/p2p", f"{modd_str}/../static/p2p", "/docs/p2p")
    ]


    sections_docs_html_files_map = {}
    for section_name_str, d_str, d_target_str, url_base_str in docs_dirs_lst:
        
        os.system(f"mkdir -p {d_target_str}")
        section_files_lst = []

        for f_str in os.listdir(d_str):
            if f_str.endswith(".md"):
                
                target_html_file_str = f"{f_str.split('.')[0]}.html"
                target_html_file_path_str = f"{d_target_str}/{f_str.split('.')[0]}.html"

                cmd_str = f"mkd2html {d_str}/{f_str} {target_html_file_path_str}"
                print(cmd_str)

                os.system(cmd_str)

                file_url_str = f"{url_base_str}/{target_html_file_str}"
                section_files_lst.append(file_url_str)

        sections_docs_html_files_map[section_name_str] = section_files_lst


    build_docs_index(sections_docs_html_files_map,
        table_of_contents_target_file_str)

#--------------------------------------------------
def build_docs_index(p_sections_docs_html_files_map,
    p_table_of_contents_target_file_str):

    f = open(f"{modd_str}/template/table_of_contents.html", "r")
    template = jinja2.Template(f.read())
    out_str  = template.render(sections_docs_html_files_map=p_sections_docs_html_files_map)

    f.close()

    f_target = open(p_table_of_contents_target_file_str, "w")
    f_target.write(out_str)
    f_target.close()

    print(out_str)
            
#--------------------------------------------------
if __name__ == "__main__":
    build()