from manim import *
import manimpango

class GraphAnimation(Scene):
    def construct(self):
        anglevalue = ValueTracker(2)

        axes = Axes(
            x_range=[0,10,1],
            y_range=[0, 10,1],
            x_length=6,
            y_length=6,
            axis_config={"color": WHITE},
            tips=False,
        )

        labels = axes.get_axis_labels(x_label="I",y_label="V")
        def graphPlot(values):
            theGraph = axes.plot_line_graph(x_values=values.xvalue, y_values=values.yvalue)
            return theGraph

        x1 = ValueTracker(0)
        y1 = ValueTracker(0)
        z1 = ValueTracker(0)
        
        x2 = ValueTracker(7)
        y2 = ValueTracker(0)
        z2 = ValueTracker(0)

        dot1 = Dot(axes.coords_to_point(x1.get_value(), y1.get_value(), z1.get_value()), radius=0.05)
        dot2 = Dot(axes.coords_to_point(x2.get_value(), y2.get_value(), z2.get_value()), radius=0.05)
        # dotgroup = VGroup(dot1,dot2).arrange(RIGHT, buff=6)

        theline = Line(dot1.get_center(),dot2.get_center()).set_color(color=YELLOW)
        dottedlines = axes.get_lines_to_point(dot2.get_center(), color=LIGHT_GRAY)

        dot1.add_updater(lambda z: z.become(Dot(axes.coords_to_point(x1.get_value(), 
        y1.get_value(), z1.get_value()), 
        radius=0.05))
        )
        dot2.add_updater(lambda z: z.become(Dot(axes.coords_to_point(x2.get_value(), 
        y2.get_value(), z2.get_value()), 
        radius=0.05))
        )

        theline.add_updater(
            lambda z: z.become(
                Line(dot1.get_center(),dot2.get_center()).set_color(color=YELLOW)
            )
        )
        dottedlines.add_updater(
            lambda z: z.become(
                axes.get_lines_to_point(dot2.get_center(), color=LIGHT_GRAY)
            )
        )
       

        self.add(axes, labels, dot1, dot2, theline, dottedlines)
        self.play(y2.animate(run_time=1).set_value(1))
        self.wait()
        self.play( 
        x2.animate.set_value(5),
        y2.animate.set_value(8),
        x2.animate(run_time=4).set_value(4),
        rate_functions=there_and_back_with_pause)
        
      
        

