#!/usr/local/bin/python3.4 -tt

import sys
import os
import stat
import settings_init
import settings_check
import curses_gui
from curses_win_manager import windowManager
from string import Template
from optparse import OptionParser

def get_cli_opts():
  """
  Retrieve command lines arguments.
  ./freebsd-rpi-builder.py -h for usage informations.
  """

  optparser = OptionParser()
  optparser.add_option("-q", "--quiet",
                       action="store_false", dest="verbose", default=True,
                       help="don't print status messages to stdout")

  optparser.add_option("-n", "--no-gui",
                       action="store_false", dest="gui", default=True,
                       help="start program without the ncurses gui. "\
                       "If --no-gui is provided, a configuration file "\
                       "must be provided via the --config option, and the"\
                       "bash script will be generated instantly")

  optparser.add_option("-c", "--config",
                       dest="config_file",
                       help="provide a custom configuration file FILE",
                       metavar="FILE")

  dict_opts = optparser.parse_args()
  return dict_opts


def read_templ_files():
  try:
    f = open("./template/script.sh", "r")
    templ_script = Template(f.read())
    f.close()
    f = open("./template/settings.sh", "r")
    templ_settings = Template(f.read())
    f.close()
  except FileNotFoundError:
    print("Missing template file(s) in ./template/. Try to restore the git repo"\
          " Exiting program...")
    sys.exit(1)
  return (templ_script, templ_settings)

def main():
  # Set defaults
  (cli_opts, cli_args) = get_cli_opts() # Todo: error handling + -n depends -c
  build_opts = settings_init.set_defaults_opts()
  (templ_script, templ_settings) = read_templ_files()

  # Read provided setting file
  if cli_opts.config_file != None:
    settings_init.read_conf(cli_opts.config_file, build_opts) # Todo: error handling

  if cli_opts.gui == True:
    curses_gui.start_curses_gui(build_opts)
    # Start GUI

  # Error checking
  nerrors = settings_check.check_settings(build_opts)
  if nerrors != 0:
    print("/!\\ {} warning(s) were generated concerning your configuration "\
          "setup".format(nerrors))

  # Create final script and settings
  f_conf = open(build_opts['output_conf_file'], "w+")
  f_script = open(build_opts['output_script_file'], "w+")
  output_settings = templ_settings.safe_substitute(build_opts)
  output_script = templ_script.safe_substitute(build_opts)
  f_conf.write(output_settings)
  f_script.write(output_script)
  print("{} file created".format(build_opts['output_conf_file']))
  print("{} file created".format(build_opts['output_script_file']))
  os.chmod(build_opts['output_script_file'], stat.S_IRWXU | stat.S_IRGRP | stat.S_IXGRP | stat.S_IXOTH)
  f_conf.close()
  f_script.close()
  sys.exit(0)

if __name__ == '__main__':
  main()
