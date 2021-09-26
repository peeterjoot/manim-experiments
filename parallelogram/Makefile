
# uncomment only one of these:
QUALITY_LOW := -ql
#QUALITY_MEDIUM := -qm
#QUALITY_HIGH := -qh
#QUALITY_4K := -qk

ifdef QUALITY_LOW
	RESOLUTION := 480p15
   MANIMFLAGS := $(QUALITY_LOW)
endif
ifdef QUALITY_MEDIUM
	RESOLUTION := 720p30
   MANIMFLAGS := $(QUALITY_MEDIUM)
endif
ifdef QUALITY_HIGH
	RESOLUTION := 1080p60
   MANIMFLAGS := $(QUALITY_HIGH)
endif
ifdef QUALITY_4K
	RESOLUTION := 2160p60
   MANIMFLAGS := $(QUALITY_4K)
endif

#MANIMFLAGS += -p

ALL += TitlePage
ALL += Overview
ALL += DrawParallelogram
ALL += ProjRej
ALL += ProjRej2
ALL += RejRotate
ALL += ProjRejPerp
ALL += RejIsVector
ALL += RejIsVector2
ALL += ParallelogramComputationGA
ALL += WedgeToDet
ALL += WedgeR3
ALL += BivectorAddition

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
	#../bin/build --killonly
	#open $@

clean:
	rm -rf __pycache__ media *.mp4 concat.in
