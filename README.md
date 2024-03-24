# vcf-unique-svs
Pull unique structural variants out of a VCF (Variant Call Format) file

[![CircleCI](https://dl.circleci.com/status-badge/img/gh/bess/vcf-unique-svs/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/bess/vcf-unique-svs/tree/main)


## Local Development
1. Install [asdf](https://asdf-vm.com/guide/getting-started.html) for dependencies management
2. Add the python plugin: `asdf plugin-add python`
3. Install python: `asdf install`
4. Install pip: `python setup/get-pip.py`
5. Install pip requirements: `pip install -r requirements.txt`
6. Run the test suite: `pytest -s`