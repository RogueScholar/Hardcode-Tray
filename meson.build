project('hardcode-tray',
  version: run_command('debian/get-version').stdout().strip(),
  meson_version: '>= 0.46.0',
  license: 'GPL-3.0',
  default_options: ['prefix=/usr']
)

dependency('gobject-introspection-1.0')
dependency('gtk+-3.0')

i18n = import('i18n')
python = import('python')

py_installation = python.find_installation('python3')
if not py_installation.found()
  error('No valid Python 3 interpreter found.')
endif


PYTHON_DIR = join_paths(get_option('prefix'), py_installation.get_path('purelib'))
DATA_DIR = join_paths(get_option('prefix'), get_option('datadir'), meson.project_name())
LOCALE_DIR = join_paths(get_option('prefix'), get_option('localedir'))

# Configuration params
conf = configuration_data()
conf.set('DATA_DIR', DATA_DIR)
conf.set('LOCALE_DIR', LOCALE_DIR)
conf.set('PYTHON_DIR', PYTHON_DIR)
conf.set('PACKAGE', meson.project_name())
conf.set('VERSION', meson.project_version())

subdir('data')
subdir('po')

install_subdir(
  'HardcodeTray',
  install_dir: PYTHON_DIR
)

configure_file(
  input: 'const.py.in',
  output: 'const.py',
  configuration: conf,
  install_dir: join_paths(PYTHON_DIR, 'HardcodeTray')
)

configure_file(
  input: meson.project_name() + '.py.in',
  output: meson.project_name(),
  configuration: conf,
  install_dir: join_paths(get_option('prefix'), get_option('bindir'))
)

summary({'Project Name': meson.project_name(),
         'Build Version': meson.project_version()})
summary({'Build Machine OS': build_machine.system(),
         'Build Machine CPU': build_machine.cpu(),
         'Build Machine Endianness': build_machine.endian()},
         section: 'Compilation Environment')
if meson.is_cross_build()
  summary({'Host Machine OS': host_machine.system(),
           'Host Machine CPU': host_machine.cpu(),
           'Host Machine Endianness': host_machine.endian()},
  section: 'Cross-Compilation Target')
endif
summary({'Source Directory': current_source_dir(),
         'Build Directory': current_build_dir(),
         'bindir': get_option('bindir'),
         'libdir': get_option('libdir'),
         'datadir': get_option('datadir')},
         section: 'Directories')
