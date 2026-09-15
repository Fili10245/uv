function [x, y] = euler(f, x0, y0, xf, n)
% EULER  Metodo de Euler para y' = f(x,y). Chapra cap. 25.
%   Uso:  [x, y] = euler(@(x,y) y, 0, 1, 1, 10);   % solucion exacta e^x
    h = (xf - x0)/n;
    x = zeros(1,n+1); y = zeros(1,n+1);
    x(1) = x0; y(1) = y0;
    for i = 1:n
        y(i+1) = y(i) + h*f(x(i), y(i));
        x(i+1) = x(i) + h;
    end
end
