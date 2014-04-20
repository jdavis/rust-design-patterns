RUSTC=printf "\033[32;1mRustc:\033[33m %s\033[m\n" $@; rustc
SRC=$(wildcard patterns/*.rs)
PROG:=$(patsubst patterns/%.rs,build/%,$(SRC))
RUSTFLAGS=

.SILENT:
.PRECIOUS: $(LIBSTAMP)

all: exe
	# Build executables

help:
	# Show this help
	grep -A1 ^[a-z].*\: Makefile | sed -r 's/: (.*)$$/:/g' | sed ':a;N;$$!ba;s/:\n//g' | sed s,\\#,\\t,g | grep -v \\--

clean:
	# Remove executables
	rm -fr $(PROG) build/ patterns/*~ *~

exe: $(PROG)
	# Build executables

run: $(PROG)
	# Run executables
	@for EXE in $(PROG); do\
		printf "\033[33;1m%s\033[m\n" $$EXE;\
		./$$EXE;\
	done

version:
	# Display version of source code
	git describe

%: build/%
	printf "\033[33;1m%s\033[m\n" $<
	$<

build/% : patterns/%.rs
	mkdir -p build
	$(RUSTC) $(RUSTFLAGS) $< -o $@
