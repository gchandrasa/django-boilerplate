# django-boilerplate

Gilang Chandrasa's django project boilerplate.

# Included packages
* Bourbon
* Neat
* jQuery 1.8.2


# Required packages (requirements.txt)
* django
* django-extensions
* django-model-utils
* django-debug-toolbar
* South
* lxml
* django-compressor
* easy-thumbnails


# Setup

Clone the repository

    git clone https://github.com/gchandrasa/django-boilerplate.git <project_name>

Change directory to \<project_name\>

    cd <project_name>

Ignore settings_local.py

    echo $'\nsettings_local.py' >> .gitignore

Reinitialize repository

    rm -rf .git
    git init
    git commit -am "initial setup"

Install required packages

    pip install -r requirements.txt

Done!

Licenses
--------

Bourbon is Copyright © 2011-2012 thoughtbot. It is free software, and may be redistributed under the terms specified in the LICENSE file.
Bourbon Neat is Copyright © 2012 thoughtbot. It is free software, and may be redistributed under the terms specified in the LICENSE file.
