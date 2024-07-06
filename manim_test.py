import subprocess
import os

from manim import *

class DifferentRotations(Scene):
    def construct(self):
        left_square = Square(color=BLUE, fill_opacity=0.7).shift(2 * LEFT)
        right_square = Square(color=GREEN, fill_opacity=0.7).shift(2 * RIGHT)
        self.play(
            left_square.animate.rotate(PI), Rotate(right_square, angle=PI), run_time=2
        )
        self.wait()


class MovingAround(Scene):
    def construct(self):
        squares = [Square(color=BLACK, fill_opacity=1) for x in range(2)]

        self.play(*[s.animate
                    .shift(1.5*[RIGHT, LEFT][idx])
                    .set_fill(GREEN)
                    for (idx, s) in enumerate(squares)])

        self.play(*[s.animate.scale(1.5) for idx, s in enumerate(squares)])
        self.play(*[s.animate
                    .scale(0.2)
                    .rotate([-.5, .5][idx] * PI)
                    .set_fill(BLACK)
                    for idx, s in enumerate(squares)])
        self.play(*[s.animate
                    .shift(1*[RIGHT, LEFT][idx])
                    .rotate([-.5, .5][idx] * PI)
                    .set_fill(ManimColor('#00AA00'))
                    for (idx, s) in enumerate(squares)])
        self.play(*[s.animate
                    .scale(0.1)
                    .rotate([-.5, .5][idx] * PI)
                    .set_fill(BLACK)
                    for idx, s in enumerate(squares)])


FPS = 144
CLASS_TO_RUN = MovingAround

if __name__ == '__main__':
    # quality medium (720p)
    manim_args = ["manim", "-pqm"]
    manim_args.extend(["--fps", str(FPS)])
    manim_args.extend([os.path.basename(__file__), CLASS_TO_RUN.__name__])
    subprocess.run(manim_args)
