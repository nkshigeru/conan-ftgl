from conans import ConanFile, CMake, tools


class FtglConan(ConanFile):
    name = "ftgl"
    version = "2.3.0"
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Ftgl here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"
    requires = "freetype/2.9.1@bincrafters/stable"

    def source(self):
        self.run("git clone https://github.com/ulrichard/ftgl.git")
        self.run("cd ftgl && git checkout 16f7667cbd4b1e988ae24128c5dea54479926f85")
        # This small hack might be useful to guarantee proper /MT /MD linkage
        # in MSVC if the packaged project doesn't have variables to set it
        # properly
        tools.replace_in_file("ftgl/CMakeLists.txt", "PROJECT(FTGL)",
                              '''PROJECT(FTGL)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()''')

    def configure_cmake(self):
        cmake = CMake(self)
        cmake.configure(source_folder="ftgl")
        return cmake

    def build(self):
        cmake = self.configure_cmake()
        cmake.build()

    def package(self):
        cmake = self.configure_cmake()
        cmake.install()

    def package_info(self):
        if self.settings.build_type == "Debug":
            self.cpp_info.libs = ["ftgld"]
        else:
            self.cpp_info.libs = ["ftgl"]
        if not self.options.shared:
            self.cpp_info.defines = ["FTGL_LIBRARY_STATIC"]

