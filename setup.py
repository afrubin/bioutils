from setuptools import setup, find_packages

package_name = "bioutils"
short_description = """miscellaneous simple bioinformatics utilities and lookup tables"""
long_description = open("README.rst").read()

# namespace_package = "".join(package_name.split(".")[:-1])
setup(
    author = package_name + " Committers",
    description = short_description,
    license = "Apache License 2.0 (http://www.apache.org/licenses/LICENSE-2.0)",
    long_description = long_description,
    name = package_name,
    # namespace_packages = [namespace_package],
    package_data = {
	'bioutils': ['_data/assemblies/*.json']
        },
    packages = find_packages(),
    use_scm_version = True,
    zip_safe = True,

    author_email = "biocommons-dev@googlegroups.com",
    url = "https://github.com/biocommons/" + package_name,

    classifiers = [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Healthcare Industry",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Database :: Front-Ends",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
    ],

    keywords = [
        'bioinformatics',
    ],

    # entry_points = {
    #     "console_scripts": [
    #         "seqrepo = seqrepo.cli:main",
    #     ],
    # },

    install_requires = [
        "requests",
        'six',
    ],

    setup_requires = [
        "pytest-runner",
        "setuptools_scm==1.11.1", # bug in 1.13.1 https://github.com/pypa/setuptools_scm/issues/134
        "wheel",
    ],

    tests_require = [
        "pytest",
        "pytest-cov",
        "vcrpy",
    ],
)

# <LICENSE>
# Copyright 2016 Source Code Committers
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# </LICENSE>
