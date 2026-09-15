function [m, b, r2] = minimos_cuadrados(x, y)
% MINIMOS_CUADRADOS  Regresion lineal y = m*x + b. Chapra cap. 17.
%   Uso:  [m, b, r2] = minimos_cuadrados([1 2 3 4 5 6 7], ...
%                                        [0.5 2.5 2 4 3.5 6 5.5]);
    x = x(:); y = y(:); n = numel(x);
    Sx = sum(x); Sy = sum(y); Sxy = sum(x.*y); Sxx = sum(x.^2);
    m = (n*Sxy - Sx*Sy)/(n*Sxx - Sx^2);
    b = (Sy - m*Sx)/n;
    yfit  = m*x + b;
    SSres = sum((y - yfit).^2);
    SStot = sum((y - mean(y)).^2);
    r2 = 1 - SSres/SStot;
end
