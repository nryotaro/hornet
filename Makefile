pyenv_dir = venv

.PHONY: deploy clean build

deploy: dist/graphviz-hornet-*.tar.gz
	. $(pyenv_dir)/bin/activate && twine upload dist/*

build: 
	rm -rf dist
	. $(pyenv_dir)/bin/activate && python -m build

dist/graphviz-hornet-*.tar.gz: venv/bin/activate
	$(MAKE) pyenv_dir=$(pyenv_dir) build

clean:
	rm -rf $(pyenv_dir) graphviz_hornet.egg-info dist

venv/bin/activate:
	python -m venv $(pyenv_dir)
	. $(pyenv_dir)/bin/activate && \
	pip install --upgrade pip && \
	pip install -e .[dev]
