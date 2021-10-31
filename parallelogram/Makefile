
# uncomment only one of these:
QUALITY_LOW := -ql
#QUALITY_MEDIUM := -qm
#QUALITY_HIGH := -qh
#QUALITY_4K := -qk

include ../manimflags.mk

ALL += TitlePage
ALL += Overview
ALL += DrawParallelogram
#ALL += RejRotate
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
SEQUENCE_ParallelogramComputationGA  := 100
SEQUENCE_WedgeToDet                  := 110
SEQUENCE_WedgeR3                     := 120
SEQUENCE_WedgeChangeOfBasisPartI     := 123
SEQUENCE_WedgeChangeOfBasisPartII    := 127
SEQUENCE_BivectorAddition            := 130
SEQUENCE_ScalarMultiplicationSign    := 140
SEQUENCE_Finale                      := 150

ALLPATHS2 := $(foreach p,$(ALL),media/videos/$(SEQUENCE_$(p))_$(p)/$(RESOLUTION)/$(p).mp4)
ALLPATHS := $(foreach p,$(ALL),$(HOME)/parallelogram/$(SEQUENCE_$(p))_$(p).mp4)

PROJECT := parallelogram

all :: $(ALLPATHS2) $(ALLPATHS)
all :: $(PROJECT).mp4

include ../manimrules.mk
