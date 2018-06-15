from setuptools import setup, find_packages

setup(
    name="anygen-jmespath",
    description="A jmespath plugin for anygen",
    long_description=open("README.md").read(),  # no "with..." will do for setup.py
    long_description_content_type='text/markdown; charset=UTF-8; variant=GFM',
    license="MIT",
    author="Kyrylo Shpytsya",
    author_email="kshpitsa@gmail.com",
    url="https://github.com/kshpytsya/anygen-jmes",
    setup_requires=["setuptools_scm"],
    install_requires=[
        "anygen",
        "jmespath~=0.9"
    ],
    use_scm_version=True,
    python_requires=">=3.6, <=3.7",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    entry_points={"anygen": ["extras = anygen_jmespath:extras"]},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)
