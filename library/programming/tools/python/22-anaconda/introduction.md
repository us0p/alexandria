# Anaconda
Is a Python distribution, a pre-packaged bundle that includes:
- Python interpreter
- A packager manager called `conda`
- Pre-installed data science and scientific computing libraries, like
	- `numpy`
	- `pandas`
	- `matplotlib`
	- `scikit-learn`
	- etc

It's especially popular in data science, machine learning, and scientific computing because it simplifies managing complex dependencies and environments.
## Why not use `pip`
- **Binary dependencies**: `pip` installs Python packages, but many scientific packages rely on **compiled C/C++ or Fortran code** (e.g., `numpy`, `scipy`, `opencv`). `conda` provides pre-compiled binaries, making it smoother.
- **Environment management**: `conda` makes it very easy to create **isolated environments** with different Python versions or package versions, which is helpful for avoiding conflicts.