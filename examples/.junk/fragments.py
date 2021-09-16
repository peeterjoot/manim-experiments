
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
