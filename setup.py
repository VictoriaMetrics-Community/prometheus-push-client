from distutils.core import setup


with open("./prometheus_push_client/version.py") as fd:
    exec(fd.read())

github_url = 'https://github.com/gistart/prometheus-push-client'

readme_lines = []
with open('README.md') as fd:
    readme_lines = filter(None, fd.read().splitlines())
readme_lines = list(readme_lines)[:3]
readme_lines.append('Read more at [github page](%s).' % github_url)
readme = '\n\n'.join(readme_lines)


setup(
    name="prometheus_push_client",
    version=__version__,
    author="gistart",
    author_email="gistart@yandex.ru",
    description="Push Prometheus metrics to VictoriaMetrics or other exporters",
    long_description=readme,
    long_description_content_type="text/markdown",
    url=github_url,
    license="Apache License 2.0",
    classifiers=(
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: Apache License 2.0",
        "Operating System :: OS Independent",
    ),
    python_requires=">=3.6",
    packages=[
        "prometheus_push_client"
    ],
    install_requires=[
        "prometheus_client>=0.4.0",
    ],
    extras_require={
        "http": [
            "aiohttp<4",
            "requests<3",
        ],
        "test": [
            "pytest",
            "pytest-asyncio",
            "pytest-cov",
            "aiohttp<4",
            "requests<3",
        ],
    }
)