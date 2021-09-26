#WHAT := ManimCELogo
#WHAT := SquareToCircle2
#WHAT := BraceAnnotation
#WHAT := VectorArrow
#WHAT := NumberLineExample
#WHAT := parallelogram
#WHAT := q
#WHAT := ParallelogramComputationClassic
#WHAT := ParallelogramComputationGA
WHAT := 3D

all :: $(WHAT)

QUALITY_LOW := -ql
QUALITY_MEDIUM := -qm
QUALITY_HIGH := -qh
QUALTITY_4K := -qk

MFLAGS += -p
MFLAGS += $(QUALITY_LOW)

% : %.py
	#manim -pql $^ $@
	#manim $(MFLAGS) $^
	../bin/build --preview --main $^

clean:
	rm -rf __pycache__ media
