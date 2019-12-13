from conans import ConanFile, CMake, tools

class RangConan(ConanFile):
    name = "rang"
    version = "3.1"
    license = "Unlicense"
    author = "Abhinav Gauniyal"
    url = "https://github.com/agauniyal/rang"
    description = "A Minimal, Header only Modern c++ library for terminal goodies "
    topics = ("cli", "ansi", "color")
    exports_sources = "include/*"
    no_copy_source = True
    generators = "cmake"

    scm = {"revision": "cabe04d6d6b05356fa8f9741704924788f0dd762",
           "type": "git",
           "url": "https://github.com/agauniyal/rang.git",
           "subfolder": "source"}

    def package(self):
        self.copy("*.hpp", dst="include", keep_path=False)

    def package_id(self):
        self.info.header_only()

