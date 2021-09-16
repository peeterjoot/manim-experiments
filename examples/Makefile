#all :: ManimCELogo
#all :: SquareToCircle2
#all :: BraceAnnotation
#all :: VectorArrow
#all :: NumberLineExample
#all :: parallelogram
#all :: q
all :: ParallelogramComputationClassic

% : %.py
	#manim -pql $^ $@
	manim -pql $^

clean:
	rm -rf __pycache__ media
