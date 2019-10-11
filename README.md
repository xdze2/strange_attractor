# Thomas' cyclically symmetric attractor


![animated_attractor](./dynamic_images.gif)


3D intaractive clouds using Potree: https://xdze2.github.io/chaotic-clouds/


## Links and references 

- [http://rreusser.github.io](http://rreusser.github.io/strange-attractors/#thomas) Splendide visualization of different attractors using WebGL
- [wikipedia page of Thomas' attractor](https://en.wikipedia.org/wiki/Thomas%27_cyclically_symmetric_attractor)
- [Labyrinth Chaos, J. C. Sprott et al., 2007](http://sprott.physics.wisc.edu/pubs/paper302.pdf)



- [L’attracteur de Lorenz, paradigme du chaos - E. Ghys](http://www.bourbaphy.fr/ghys.pdf) 


## Thomas' attractor  

A simple equation, with only one parameter `b`:

    dx/dt = sin(y) - bx
    dy/dt = sin(z) - by
    dz/dt = sin(x) - bz


## Notebooks 

- [Test numba and optimization](./test_numba.ipynb)
- [ODE solver test](./which_solver.ipynb)
- [What value for coefficient b](./route_to_chaos.ipynb):

![max of x vs b](./route_to_chaos_fig1.png)

Zoom:

![max of x vs b](./route_to_chaos_fig1_zoom.png)


- [To 3D and beyond](./to_3D_and_beyond.ipynb)

![potree_v3_1000px_interior](./potree_v3_1000px_interior.png)

- [A simple working version in Julia!](./Lorenz_Julia.ipynb)