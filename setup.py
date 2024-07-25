from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in frappe_direct_printing/__init__.py
from frappe_direct_printing import __version__ as version

setup(
	name="frappe_direct_printing",
	version=version,
	description="Print directly to you printers from you favorite Frappe-Framework apps",
	author="itsdave GmbH",
	author_email="dev@itsdave.de",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
