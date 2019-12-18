A magic function starts with % Matplotlib, and to enforce plots to be rendered within the browser, you pass in inline as the backend.Matplotlib has a number of different backends available. One limitation of this backend is that you cannot modify a figure once it's rendered. So after rendering the above figure, there is no way for us to add, for example, a figure title or label its axes.You will need to generate a new plot and add a title and the axes labels** before calling the show function**.

A backend that overcomes this limitation is the notebook backend.

With the notebook backend in place, if a plt function is called, it checks if an

active figure exists, and any functions you call will be applied to this active

figure. If a figure does not exist, it renders a new figure.

