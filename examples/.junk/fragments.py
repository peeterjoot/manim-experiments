
        ### 
        #b = a.copy()
        #b.shift(LEFT)
        #self.play(ReplacementTransform(a, b))
        ### 
        #self.play(a.animate.shift(LEFT))

        #Making text
#        first_line = Text("Manim is fun")
#        second_line = Text("and useful")
#        final_line = Text("Hope you like it too!", color=BLUE)
#        color_final_line = Text("Hope you like it too!")
#
#        #Coloring
#        color_final_line.set_color_by_gradient(BLUE,PURPLE)
#
#        #Position text
#        first_line.next_to(a, 4*RIGHT)
#        second_line.next_to(a, 4*RIGHT + DOWN)
#
#        #Showing text
#        self.wait(1)
#        self.play(Write(first_line), Write(second_line))
#        self.wait(1)
#        self.play(FadeOut(second_line), ReplacementTransform(first_line, final_line))
#        self.wait(1)
#        self.play(Transform(final_line, color_final_line))
#        self.wait(2)



        #eq4_text=[ '', '$=$', '$' + mknorm2(r'\vec{u}') + '\left(' + mknorm2( r'\vec{v}') + r' - {\left(\vec{v} \cdot \hat{u}\right)}^2 \right) $' ]
        #eq4_mob=Tex(*eq4_text)
        #for i,item in enumerate(eq4_mob):
        #    dir = RIGHT
        #    if i == 2:
        #        dir = LEFT
        #    item.align_to(eq3_mob[i], dir)

        #eq4=VGroup(*eq4_mob)
        #eq4.shift(DOWN)
        #self.play( Write(eq4) )
        #self.play( FadeOut(eq2_mob[2]) )
