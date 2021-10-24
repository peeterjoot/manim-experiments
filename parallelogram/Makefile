
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
#ALL += RejRotate
ALL += ProjRejPerp
ALL += RejIsVector
#ALL += RejIsVector2
ALL += ParallelogramComputationGA
ALL += WedgeToDet
ALL += WedgeR3
ALL += WedgeChangeOfBasisPartI
ALL += WedgeChangeOfBasisPartII
ALL += BivectorAddition
ALL += ScalarMultiplicationSign
ALL += Finale

SEQUENCE_TitlePage                   := 010
SEQUENCE_Overview                    := 020
SEQUENCE_DrawParallelogram           := 030
SEQUENCE_ProjRej                     := 040
SEQUENCE_ProjRej2                    := 050
SEQUENCE_ProjRejPerp                 := 070
SEQUENCE_RejIsVector                 := 080
SEQUENCE_ParallelogramComputationGA  := 100
SEQUENCE_WedgeToDet                  := 110
SEQUENCE_WedgeR3                     := 120
SEQUENCE_WedgeChangeOfBasisPartI     := 123
SEQUENCE_WedgeChangeOfBasisPartII    := 127
SEQUENCE_BivectorAddition            := 130
SEQUENCE_ScalarMultiplicationSign    := 140
SEQUENCE_Finale                      := 150

ALLPATHS2 := $(foreach p,$(ALL),media/videos/$(SEQUENCE_$(p))_$(p)/$(RESOLUTION)/$(SEQUENCE_$(p))_$(p).mp4)
ALLPATHS := $(foreach p,$(ALL),$(HOME)/parallelogram/$(SEQUENCE_$(p))_$(p).mp4)

all :: $(ALLPATHS2) $(ALLPATHS)
all :: parallelogram.mp4

% : %.py
	manim $(MANIMFLAGS) $^

# copy to a path that is more easily accessible by Mac tools (iMovie, ...), and also include the sequence in the filename.
define CP_template
$(HOME)/parallelogram/$(SEQUENCE_$(1))_$(1).mp4 : media/videos/$(SEQUENCE_$(1))_$(1)/$(RESOLUTION)/$(1).mp4
	mkdir -p $$(dir $$@)
	cp $$^ $$@
endef

define MANIM_template
media/videos/$(SEQUENCE_$(1))_$(1)/$(RESOLUTION)/%.mp4 : $(SEQUENCE_$(1))_$(1).py helper.py ../bin/mylatex.py
	manim $(MANIMFLAGS) $(SEQUENCE_$(1))_$(1).py $(1)
endef

$(foreach p,$(ALL),$(eval $(call CP_template,$(p))))

$(foreach p,$(ALL),$(eval $(call MANIM_template,$(p))))

parallelogram.mp4: $(ALLPATHS)
	rm -f concat.in $@
	ls $(HOME)/parallelogram/*mp4 | sed 's/^/file /' > concat.in
	ffmpeg -f concat -safe 0 -i concat.in -c copy $@
	open $@

clean:
	rm -rf __pycache__ media *.mp4 concat.in $(HOME)/parallelogram/*.mp4
