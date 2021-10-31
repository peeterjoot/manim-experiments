# uncomment only one of these:
QUALITY_LOW := -ql
#QUALITY_MEDIUM := -qm
#QUALITY_HIGH := -qh
#QUALITY_4K := -qk

include ../manimflags.mk

ALL += TitlePage
ALL += Overview
ALL += ProjRej
#ALL += ProjRejGraphical
ALL += ProjRej2
ALL += ProjRejPerp
ALL += RejIsVector
ALL += Finale

SEQUENCE_TitlePage        := 010
SEQUENCE_Overview         := 020
SEQUENCE_ProjRej          := 040
SEQUENCE_ProjRej2         := 050
SEQUENCE_ProjRejGraphical := 045
SEQUENCE_ProjRejPerp      := 070
SEQUENCE_RejIsVector      := 080
SEQUENCE_Finale           := 150

PROJECT := projrej

ALLPATHS2 := $(foreach p,$(ALL),media/videos/$(SEQUENCE_$(p))_$(p)/$(RESOLUTION)/$(p).mp4)
ALLPATHS := $(foreach p,$(ALL),$(HOME)/$(PROJECT)/$(SEQUENCE_$(p))_$(p).mp4)

all :: $(ALLPATHS2) $(ALLPATHS)
all :: $(PROJECT).mp4

include ../manimrules.mk
