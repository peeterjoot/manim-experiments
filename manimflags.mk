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

