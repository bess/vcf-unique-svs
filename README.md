# vcf-unique-svs
Create individual [Variant Call Format](https://en.wikipedia.org/wiki/Variant_Call_Format) (VCF) files from multisample VCFs with unique variants.

Given a VCF file:
  1. Determine the sample ids referenced in this file (these will vary in name and number)
  2. Create a separate output VCF file for each sample id iff the sample id has unique variants
  3. Into each output file, place only the variants unique to this sample id (i.e., exclude anything that is common, because that won't be a likely culprit for clinical significance.)

[![CircleCI](https://dl.circleci.com/status-badge/img/gh/bess/vcf-unique-svs/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/bess/vcf-unique-svs/tree/main)


## Local Development
1. Install [asdf](https://asdf-vm.com/guide/getting-started.html) for dependencies management
2. Add the python plugin: `asdf plugin-add python`
3. Install python: `asdf install`
4. Install pip: `python setup/get-pip.py`
5. Install pip requirements: `pip install -r requirements.txt`
6. Run the test suite: `pytest -s`