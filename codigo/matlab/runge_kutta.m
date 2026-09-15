function [x, y] = runge_kutta(f, x0, y0, xf, n)
% RUNGE_KUTTA  Runge-Kutta de 4.o orden (RK4). Chapra cap. 25.
%   Uso:  [x, y] = runge_kutta(@(x,y) y, 0, 1, 1, 10);
    h = (xf - x0)/n;
    x = zeros(1,n+1); y = zeros(1,n+1);
    x(1) = x0; y(1) = y0;
    for i = 1:n
        k1 = f(x(i),     y(i));
        k2 = f(x(i)+h/2, y(i)+h/2*k1);
        k3 = f(x(i)+h/2, y(i)+h/2*k2);
        k4 = f(x(i)+h,   y(i)+h*k3);
        y(i+1) = y(i) + h/6*(k1 + 2*k2 + 2*k3 + k4);
        x(i+1) = x(i) + h;
    end
end
