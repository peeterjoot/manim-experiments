#all :: ManimCELogo
#all :: SquareToCircle2
#all :: BraceAnnotation
#all :: VectorArrow
#all :: NumberLineExample
#all :: parallelogram
#all :: q
#all :: ParallelogramComputationClassic
#all :: ParallelogramComputationGA
all :: 3D

QUALITY_LOW := -ql
QUALITY_MEDIUM := -qm
QUALITY_HIGH := -qh
QUALTITY_4K := -qk

MFLAGS += -p
MFLAGS += $(QUALITY_LOW)

% : %.py
	#manim -pql $^ $@
	manim $(MFLAGS) $^

clean:
	rm -rf __pycache__ media
