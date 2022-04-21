# uncomment only one of these:
QUALITY_LOW := -ql
#QUALITY_MEDIUM := -qm
#QUALITY_HIGH := -qh
#QUALITY_4K := -qk

include ../manimflags.mk

ALL += TitlePage
ALL += Overview
ALL += ProjRej
ALL += ProjRej2
ALL += Inverse
ALL += ProjParallelToU
#ALL += ProjRejGraphical
ALL += ProjRejPerp
ALL += RejIsVector
ALL += RejR3
#ALL += RejCross
ALL += Rejvisualization
ALL += RejGAVisualization
ALL += SummaryTable
ALL += Finale

SEQUENCE_TitlePage              := 010
SEQUENCE_Overview               := 020
SEQUENCE_ProjRej                := 040
SEQUENCE_ProjRej2               := 050
SEQUENCE_Inverse                := 051
SEQUENCE_ProjParallelToU        := 052
#SEQUENCE_ProjRejGraphical      := 045
SEQUENCE_ProjRejPerp            := 070
SEQUENCE_RejIsVector            := 080
SEQUENCE_RejR3                  := 090
#SEQUENCE_RejCross               := 091
SEQUENCE_Rejvisualization       := 092
SEQUENCE_RejGAVisualization 	  := 093
SEQUENCE_SummaryTable           := 130
SEQUENCE_Finale                 := 150

PROJECT := projrej

ALLPATHS2 := $(foreach p,$(ALL),media/videos/$(SEQUENCE_$(p))_$(p)/$(RESOLUTION)/$(p).mp4)
ALLPATHS := $(foreach p,$(ALL),$(HOME)/$(PROJECT)/$(SEQUENCE_$(p))_$(p).mp4)

all :: $(ALLPATHS2) $(ALLPATHS)
all :: $(PROJECT).mp4

include ../manimrules.mk
