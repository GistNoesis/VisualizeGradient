# VisualizeGradient
It's a tool that help get the correct mental picture of what the gradient of a function is.

This mental picture generalize to higher dimensions.

You can find alternative visualizations for the gradient on the wikipedia gradient page https://en.wikipedia.org/wiki/Gradient

It allows to plot gradient map for 1d and 2d functions, as a vector field.

What is important to realize is that when we plot the function value along the additional dimension, **the gradient lives in the space spanned by the input dimensions**. 

The gradient point in the direction that increase the value of the function. The length of the arrows shows the rate of increase.

This is mental picture help explain what is gradient ascent : we follow the arrows, and we always stay in the original input space.

In 2d we also notice that although the gradient point towards the maximum, when the curve has an oval shape, the true maximum is not on the line following the gradient. This is why https://en.wikipedia.org/wiki/Conjugate_gradient_method exist.

In school, one usually introduce the derivative as the tangent to the curve at a point, but this picture is confusing as following this tangent makes you leave the input space. 

The arrow of the vector field is not a simple projection of a tangent. (For 1d function, the procedure is draw a tangent to the curve, move 1 unit along the x-axis, place a point on the tangent, project this arrow along the y-axis, this gives you an arrow of the right length that you rotate back to the x-axis).

f(x) = x^3+2*x^2-x (The arrows have been clipped to a maximum length)

![f(x) = x^3+2*x^2-x](Figure_1.png?raw=true "Example for 1d Function")

f(x,y) = sin((0.75*x)^2+y^2+0.01)

![f(x,y) = sin((0.75*x)^2+y^2+0.01)](Figure_2.png?raw=true "Example for 2d Function")

You can use 
```python plotgrad.py```
to obtain an interactive version of these two figures.

It requires pytorch numpy and matplotlib 

You can edit the file to plot your own functions
