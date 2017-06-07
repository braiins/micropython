"""Utility functions for micropython Scons tool.

   Copyright (c) 2016 Braiins Systems s.r.o.
"""
import os

def get_genhdr_pathname(env, header_name):
    """
    @return full pathname for a generated C-header file
    """
    return os.path.join(env.subst('#${VARIANT_DIR}'), 'genhdr',
                        header_name)


def get_script_pathname(env, script_name, script_dir='py'):
    """
    @return full pathname for helper script
    """
    return os.path.join('/usr', 'bin', 'python') + ' ' + \
        os.path.join(env.subst('${CONFIG.MICROPYTHON_DIR}'), script_dir,
                     script_name)


def get_tool_pathname(env, tool_name):
    """
    @return full pathname for tool script (resides in tools/)
    """
    return get_script_pathname(env, tool_name, script_dir='tools')