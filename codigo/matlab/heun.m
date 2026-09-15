function [x, y] = heun(f, x0, y0, xf, n)
% HEUN  Metodo de Heun (predictor-corrector). Chapra cap. 25.
%   Uso:  [x, y] = heun(@(x,y) y, 0, 1, 1, 10);
    h = (xf - x0)/n;
    x = zeros(1,n+1); y = zeros(1,n+1);
    x(1) = x0; y(1) = y0;
    for i = 1:n
        k1 = f(x(i), y(i));
        yp = y(i) + h*k1;                     % predictor (Euler)
        k2 = f(x(i)+h, yp);
        y(i+1) = y(i) + h*(k1 + k2)/2;        % corrector
        x(i+1) = x(i) + h;
    end
end
