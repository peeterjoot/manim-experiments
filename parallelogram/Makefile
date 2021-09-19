HIGHRES := 1

ifdef HIGHRES
	RESOLUTION := 1080p60
else
	RESOLUTION := 480p15
   MANIMFLAGS := -pql
endif

ALL += DrawParallelogram
ALL += ParallelogramComputationGA

ALLPATHS := $(foreach p,$(ALL),media/videos/main/$(RESOLUTION)/$(p).mp4)

all :: parallelogram.mp4
all :: $(ALLPATHS)

#all :: ParallelogramComputationClassic
#all :: ParallelogramComputationGA

% : %.py
	manim $(MANIMFLAGS) $^

media/videos/main/$(RESOLUTION)/%.mp4 : main.py
	manim $(MANIMFLAGS) $^ $(notdir $(basename $@))

parallelogram.mp4: $(ALLPATHS)
	rm -f concat.in
	for i in $(ALL) ; do echo file media/videos/main/$(RESOLUTION)/$$i.mp4 >> concat.in ; done
	ffmpeg -f concat -safe 0 -i concat.in -c copy parallelogram.mp4

clean:
	rm -rf __pycache__ media *.mp4 concat.in
