from manim import *

class PythagoreanTheorem(Scene):
    def construct(self):
        # Create right-angled triangle with labeled sides
        triangle = RightAngleTriangle()
        a_label = MathTex("a").next_to(triangle.c2p(0.5), LEFT)
        b_label = MathTex("b").next_to(triangle.c2p(0.5), DOWN)
        c_label = MathTex("c").next_to(triangle.hyp, RIGHT)
        
        # Create equation
        equation = MathTex("a^2", "+", "b^2", "=", "c^2").scale(1.5)
        equation.next_to(triangle, DOWN, buff=1)

        # Animate triangle and labels
        self.play(Create(triangle))
        self.play(Write(a_label), Write(b_label), Write(c_label))
        self.wait()

        # Animate equation
        self.play(Write(equation))
        self.wait()

        # Example
        example_triangle = RightAngleTriangle(scale=2)
        example_triangle.next_to(triangle, RIGHT, buff=3)
        a_value = MathTex("3").next_to(example_triangle.c2p(0.5), LEFT)
        b_value = MathTex("4").next_to(example_triangle.c2p(0.5), DOWN)
        c_value = MathTex("5").next_to(example_triangle.hyp, RIGHT)

        # Animate example triangle and values
        self.play(Create(example_triangle))
        self.play(Write(a_value), Write(b_value), Write(c_value))
        self.wait()

        # Example equation
        example_equation = MathTex("3^2", "+", "4^2", "=", "5^2").scale(1.5)
        example_equation.next_to(example_triangle, DOWN, buff=1)

        # Animate example equation
        self.play(TransformMatchingTex(equation, example_equation))
        self.wait()

class RightAngleTriangle(VMobject):
    def __init__(self, scale=1, **kwargs):
        super().__init__(**kwargs)
        self.c2p = complex_to_R3(scale)
        self.hyp = Line(self.c2p(0), self.c2p(1 + 1j))
        self.add(Line(self.c2p(0), self.c2p(1j)), Line(self.c2p(0), self.c2p(1)), Line(self.c2p(1), self.c2p(1j)), self.hyp)
