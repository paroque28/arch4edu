#!/usr/bin/env python3
from lilaclib import *

maintainers = [{'github': 'petronny'}]
update_on = [{'github': 'arch4edu/devtools-arch4edu'}]
build_prefix = 'extra-x86_64'
pre_build = vcs_update

def post_build():
    git_add_files('PKGBUILD')
    git_commit()

if __name__ == '__main__':
    single_main(build_prefix)
