load("@bazel_tools//tools/build_defs/repo:git.bzl", "git_repository")

git_repository(
    name = "rules_python",
    remote = "https://github.com/bazelbuild/rules_python.git",
    commit = "5c948dcfd4ca79c2ed3a87636c46abba9f5836e9",
)

load("@rules_python//python:pip.bzl", "pip_install")

pip_install(
   name = "pip_deps",
   requirements = "//:pip_deps.txt",
)
