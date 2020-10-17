load("@rules_python//python:defs.bzl", "py_binary")
load("@pip_deps//:requirements.bzl", "requirement")

py_binary(
    name = "main",
    srcs = ["main.py"],
    deps = [
        requirement("absl-py"),
        requirement("matplotlib"),
        requirement("numpy"),
    ],
)
