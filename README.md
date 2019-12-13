# conan-rang

[Conan](https://bintray.com/zethon/owl/rang%3Aowl) package for the [rang C++ library](https://github.com/agauniyal/rang).

This is the rang recipe used in my open source project [Owl](https://github.com/zethon/owl). 

## Usage

Add `rang/x.y.z@owl/stable` in the list of requirements of your conanfile, where `x.y.z` is the desired version. See [how to use a conanfile.py](http://docs.conan.io/en/latest/mastering/conanfile_py.html) for more information.

If you want to create and upload the rang package then follow these steps:

* `git clone https://github.com/zethon/conan-rang.git` - clone the recipe repo
* `cd conan-rang` 
* `conan create . myrepo/stable` - replace `myrepo` with you own repo information
* `conan upload rang/3.1@myrepo/stable -r myrepo` - upload the package to your own repo

Note: Since this is a header-only library there is no build step required.

## Packaging

See [Conan-Package-Tools](https://github.com/conan-io/conan-package-tools) Github page for more information on packaging.

