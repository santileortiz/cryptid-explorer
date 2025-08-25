#!/usr/bin/python3
from mkpy.utility import *

def default ():
    target = store_get ('last_snip', default='example_procedure')
    call_user_function(target)

def serve ():
    ex ('python3 -m http.server 46080')

if __name__ == "__main__":
    # Everything above this line will be executed for each TAB press.
    # If --get_completions is set, handle_tab_complete() calls exit().
    handle_tab_complete ()

    pymk_default()

