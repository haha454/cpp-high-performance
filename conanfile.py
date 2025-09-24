from conan import ConanFile


class Recipe(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeToolchain", "CMakeDeps", "VirtualRunEnv"

    def layout(self):
        self.folders.generators = "conan"

    def requirements(self):
        self.requires("boost/1.88.0")

    def test_requirements(self):
        self.test_requires("gtest/1.17.0")
        self.test_requires("benchmark/1.9.4")
