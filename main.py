from manim import *
        

class BasicStaticOscilloscope(Scene):
    def construct(self):
        # Create oscilloscope with monitor and two inputs (axes)

        ax = [Axes(x_length=4, y_length=4, x_range=[0, 4], y_range=[-2.5, 2.5]) for i in range(2)]

        ax[0].rotate(PI).flip(axis=RIGHT)
        ax[1].rotate(3*PI/2)

        monitor = Rectangle(width=8, height=5).move_to([1, 2.5, 0])
        #monitor_ax = Axes(x_length=4, y_length=4, x_range=[-2.5, 2.5], y_range=[-2.5, 2.5],tips=False).move_to(monitor.get_center())
        #self.add(monitor_ax)

        ax[0].next_to(monitor, LEFT).shift(0.5*LEFT)
        ax[1].next_to(monitor, DOWN).shift(0.5*DOWN)

        axis_labels = [
            MathTex("t").move_to(ax[0].c2p(4,0.5,0)), MathTex("V_y").move_to(ax[0].c2p(-0.5,2.5,0)),
            MathTex("t").move_to(ax[1].c2p(4,0.5,0)), MathTex("V_x").move_to(ax[1].c2p(-0.5,2.5,0))
        ]

        Oscilloscope = VGroup(*ax, *axis_labels, monitor).scale(0.72)
        self.add(Oscilloscope)

        # Plot two sine functions along two axes, display amplitude, frequency, phase difference.

        A = [1, 1.5]
        f = [1.5, 1]
        delta_phi = 30 # in degrees
        # Didn't multiply here cz converting from radian to degree gives inaccurate decimals.
        # Instead, I multiplied later in the plot function.

        curves = VGroup(i.plot(lambda x: h*np.sin(2*PI*j*(x+0)+k), x_range=[0, 2.75]) for h,i,j,k in zip(A,ax, f, [0, delta_phi*DEGREES]))
        self.add(curves)

        condition_labels = [
            MathTex("A_x =", A[1], "\\text{V}"),
            MathTex("f_x =", f[1], "\\text{Hz}"),
            MathTex("A_y =", A[0], "\\text{V}"),
            MathTex("f_y =", f[0], "\\text{Hz}"),
            MathTex("\\Delta \\phi =", delta_phi, "^\\circ")
        ]
        conditions = VGroup([i.shift(n*DOWN*MathTex("A_1 = 1V").get_height()) for i,n in zip(condition_labels, range(len(condition_labels)))])
        self.add(conditions)
        conditions.arrange(DOWN, aligned_edge=LEFT).next_to(monitor, RIGHT)

        # Draw Lissajous figure: Draw point plus trail that lasts one cycle.

        point = Dot(monitor.get_center(), color=BLUE)
        point.move_to([curves[1].get_start()[0], curves[0].get_start()[1],0])
        self.add(point)

        hline = Line(start=point.get_center(), end=curves[0].get_start(), color=BLUE)
        vline = Line(start=point.get_center(), end=curves[1].get_start(), color=BLUE)
        self.add(hline, vline)



class DynamicOscilloscope(Scene):
    def construct(self):

        ##########
        # STATIC PART
        ##########


        # Create oscilloscope with monitor and two inputs (axes)

        ax = [Axes(x_length=4, y_length=4, x_range=[0, 4], y_range=[-2.5, 2.5]) for i in range(2)]

        ax[0].rotate(PI).flip(axis=RIGHT)
        ax[1].rotate(3*PI/2)

        monitor = Rectangle(width=8, height=5).move_to([1, 2.5, 0])
        #monitor_ax = Axes(x_length=4, y_length=4, x_range=[-2.5, 2.5], y_range=[-2.5, 2.5],tips=False).move_to(monitor.get_center())
        #self.add(monitor_ax)

        ax[0].next_to(monitor, LEFT).shift(0.5*LEFT)
        ax[1].next_to(monitor, DOWN).shift(0.5*DOWN)

        axis_labels = [
            MathTex("t").move_to(ax[0].c2p(4,0.5,0)), MathTex("V_y").move_to(ax[0].c2p(-0.5,2.5,0)),
            MathTex("t").move_to(ax[1].c2p(4,0.5,0)), MathTex("V_x").move_to(ax[1].c2p(-0.5,2.5,0))
        ]

        Oscilloscope = VGroup(*ax, *axis_labels, monitor).scale(0.72)
        self.add(Oscilloscope)


        # Display amplitude, frequency, and phase difference

        A = [1, 1]
        f = [2, 2]
        delta_phi = 0 # in degrees
        # Didn't multiply here cz converting from radian to degree gives inaccurate decimals.
        # Instead, I multiplied later in the plot function.

        
        conditions = VGroup(
            MathTex("A_x ="),
            MathTex("f_x ="),
            MathTex("A_y ="),
            MathTex("f_y ="),
            MathTex("\\Delta \\phi =")
        )
        conditions.arrange(DOWN, aligned_edge=LEFT).next_to(monitor, RIGHT)

        self.add(conditions)

        ##########
        # DYNAMIC PART
        ##########


        # Create timer

        time = ValueTracker(0)

        timer = always_redraw(lambda: MathTex("t =", f"{time.get_value():.2f}", "\\text{s}").to_corner(UL))
        self.add(timer)


        # Plot two sine functions along two axes.

        curves = [
            always_redraw(lambda: ax[0].plot(lambda x: A[0]*np.sin(2*PI*f[0]*(x+time.get_value())), x_range=[0, 2.75])),
            always_redraw(lambda: ax[1].plot(lambda x: A[1]*np.sin(2*PI*f[1]*(x+time.get_value())+delta_phi), x_range=[0, 2.75]))
        ]
        self.add(*curves)

        # Draw Lissajous figure: Draw point plus trail that lasts one cycle.

        point = always_redraw(lambda: Dot([curves[1].get_start()[0], curves[0].get_start()[1],0], color=BLUE))
        path = TracedPath(point.get_center, dissipating_time=max(1/f[0],1/f[1]))
        self.add(point, path)

        hline = always_redraw(lambda: Line(start=point.get_center(), end=curves[0].get_start(), color=BLUE))
        vline = always_redraw(lambda: Line(start=point.get_center(), end=curves[1].get_start(), color=BLUE))
        self.add(hline, vline)

        # Run
        def Play(t, A=A, f=f, delta_phi=delta_phi):
            conditions = VGroup(
                MathTex("A_x =", A[1], "\\text{V}"),
                MathTex("f_x =", f[1], "\\text{Hz}"),
                MathTex("A_y =", A[0], "\\text{V}"),
                MathTex("f_y =", f[0], "\\text{Hz}"),
                MathTex("\\Delta \\phi =", delta_phi, "^\\circ")
            )
            conditions.arrange(DOWN, aligned_edge=LEFT).next_to(monitor, RIGHT)
            self.play(time.animate.set_value(t), rate_func=linear, run_time=t)
            time.set_value(0)
        
        Play(10)

        Play(10, f = [1,1.1])
        
        Play(10, A = [1,1.2])

        Play(10, f = [2,2.2], delta_phi = 30)