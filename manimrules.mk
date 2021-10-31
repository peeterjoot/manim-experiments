
% : %.py
	manim $(MANIMFLAGS) $^

# copy to a path that is more easily accessible by Mac tools (iMovie, ...), and also include the sequence in the filename.
define CP_template
$(HOME)/$(PROJECT)/$(SEQUENCE_$(1))_$(1).mp4 : media/videos/$(SEQUENCE_$(1))_$(1)/$(RESOLUTION)/$(1).mp4
	mkdir -p $$(dir $$@)
	cp $$^ $$@
endef

define MANIM_template
media/videos/$(SEQUENCE_$(1))_$(1)/$(RESOLUTION)/$(1).mp4 : $(SEQUENCE_$(1))_$(1).py helper.py ../bin/mylatex.py
	manim $(MANIMFLAGS) $(SEQUENCE_$(1))_$(1).py $(1)
endef

$(foreach p,$(ALL),$(eval $(call CP_template,$(p))))

$(foreach p,$(ALL),$(eval $(call MANIM_template,$(p))))

$(PROJECT).mp4: $(ALLPATHS)
	rm -f concat.in $@
	ls $(HOME)/$(PROJECT)/*mp4 | sed 's/^/file /' > concat.in
	ffmpeg -f concat -safe 0 -i concat.in -c copy $@
	open $@

clean:
	rm -rf __pycache__ media *.mp4 concat.in $(HOME)/$(PROJECT)/*.mp4
