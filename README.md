# tempy

Tempy is a simple, single file python script which makes it easy to modularize html files for static web pages. This makes it easier to edit content which is displayed on more than one page in a sight like a header or footer.

## Setup

Tempy is has three different directories that you'll need to understand.

1. Templates
2. Modules
3. Production


### Templates

This directory is for files that import code from the modular files. For example, and index.html which uses a header and footer would go in this directory. To utilize a module from a template, simply insert a module tag `[[[module_tag]]]` in a template file. The module tag must show the same name as the file being called from the modules directory. An example of this is below.

Here, an index file inserts a header from the content in /modules/header.html and a footer from /modules/footer.html

```
index.html

<html>
  <body>
    <!-- insert header -->
    [[[header]]]

    <p> normal webpage content... <p>

    <!-- insert footer -->
    [[[footer]]]
  </body>
</html>
```

### Modules

Modules are files containing code which are then inserted into files in the templates directory. This is where you would want to put header.html and footer.html

### Production

The production directory contains the final html files with the module content inserted into the template pages. The idea is that any files in the production directory are ready to be pushed to your web server. 

