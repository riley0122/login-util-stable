import os

os.system('pip install --upgrade pip')
os.system('pip install wheel')
os.system('pip install twine')
# in shell:
#   setup/setup.py sdist bdist_wheel
#   twine upload dist/*'
