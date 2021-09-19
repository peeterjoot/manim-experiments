#HIGHRES := 1

ifdef HIGHRES
	RESOLUTION := 1080p60
else
	RESOLUTION := 480p15
   MANIMFLAGS := -pql
endif

ALL += DrawParallelogram
ALL += ProjRej
ALL += ProjRejPerp
ALL += RejIsScalar
ALL += ParallelogramComputationGA

ALLPATHS := $(foreach p,$(ALL),media/videos/parallelogram/$(RESOLUTION)/$(p).mp4)

all :: parallelogram.mp4
all :: $(ALLPATHS)

% : %.py
	manim $(MANIMFLAGS) $^

media/videos/parallelogram/$(RESOLUTION)/%.mp4 : parallelogram.py
	manim $(MANIMFLAGS) $^ $(notdir $(basename $@))

parallelogram.mp4: $(ALLPATHS)
	rm -f concat.in $@
	for i in $(ALL) ; do echo file media/videos/parallelogram/$(RESOLUTION)/$$i.mp4 >> concat.in ; done
	ffmpeg -f concat -safe 0 -i concat.in -c copy $@

clean:
	rm -rf __pycache__ media *.mp4 concat.in
