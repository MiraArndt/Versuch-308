all: build/main.pdf

# hier Python-Skripte:
build/plot1-1.pdf: plot1-1.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python plot1-1.py
build/plot1-2.pdf: plot1-2.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python plot1-2.py
build/plot2-1.pdf: plot2-1.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python plot2-1.py
build/plot2-2.pdf: plot2-2.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python plot2-2.py
build/plot2-3.pdf: plot2-3.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python plot2-3.py
build/plot3.pdf: plot3.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python plot3.py
	

	


# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/main.pdf: build/plot1-1.pdf build/plot1-2.pdf build/plot2-1.pdf build/plot2-2.pdf build/plot2-3.pdf build/plot3.pdf

build/main.pdf: FORCE | build
	  TEXINPUTS=build: \
	  BIBINPUTS=build: \
	  max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	main.tex

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean
