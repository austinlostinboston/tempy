'''
Tempy script

Author: Austin Ankney
Date: 8/7/15
Description: A simple script to help manage html files
    in a modular way to maximize code reuse while avoiding
    javascript alternatives.
'''

import os
import re
import sys

class tempy(object):
    def __init__(self):
        self.base_dir = os.path.dirname(os.path.realpath(__file__))
        self.template_files = self._getFiles(self.base_dir + "/templates")
        self.module_files = self._getFiles(self.base_dir + "/modules")
        self.modules = self._getModules()

    def _getFiles(self,dir_path):
        files = []
        for dirpath, dirnames, filenames in os.walk(dir_path):
            if len(filenames) > 0:
                for f in filenames:
                    file_path = dirpath + "/" + f
                    files.append(file_path)

        return files

    def _getModules(self):
        modules = {}
        for f in self.module_files:
            key_name = f.split("/")[-1].split(".")[0]
            r = open(f, 'r')
            content = r.read()

            modules[key_name] = content

        return modules

    def _sub(self, f, template):
        ## Extract only characters between [[[ and ]]]
        regex = re.compile(r'\[\[\[(\w+)\]\]\]')

        ## Only extract contents when the parse symbol is present
        if regex.search(template) is not None:

            ## Extract parts of response that need replaced
            replacers = regex.findall(template)

            for part in replacers:
                print "Replacing " + part + " in " + f
                try:
                    template = template.replace("[[[" + str(part) + "]]]", self.modules[str(part)])
                except KeyError:
                    print "Could not find module named -> " + str(part)
                    sys.exit(0)
                except:
                    print "Ran into unexpected problem. Stopping tempy."
                    sys.exit(0)

        new_template = template

        return new_template


    def produce(self):
        for f in self.template_files:
            production_file = f.split("/")[-1]
            r = open(f, 'r')
            temp_content = r.read()
            production_content = self._sub(f, temp_content)
            r.close()

            print "Writing " + production_file + " to production"
            w = open(self.base_dir + "/production/" + production_file, 'w')
            w.write(production_content)
            w.close()

        print "Production complete"



if __name__ == "__main__":
    t = tempy()
    t.produce()


