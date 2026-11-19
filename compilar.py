from py2exe import freeze

freeze(windows=[{"script": "cicfighters.py", "icon_resources": [(1, "cicfighters-large.ico")]}],
       options={"optimize": 1, "bundle_files": 1, "compressed": True},
       zipfile=None)
