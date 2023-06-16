#!/bin/bash

# Update version number in setup.py
echo "Update version number in setup.py..."
python renew_setup_version.py

echo "Removing old distributions..."
rm -rf ./dist/*

echo "Building new distribution..."
python setup.py sdist bdist_wheel

echo "Uploading new distribution to PyPI..."
twine upload dist/*

echo "Uninstalling old version of kangforecast..."
pip uninstall -y kangforecast

echo "Installing new version of kangforecast..."
pip install --no-cache-dir --upgrade kangforecast

echo "All done!"

