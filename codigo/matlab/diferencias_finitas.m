function [d1, d2] = diferencias_finitas(f, x, h)
% DIFERENCIAS_FINITAS  Derivadas por diferencias finitas centradas. Chapra cap. 23.
%   d1 : primera derivada,  d2 : segunda derivada
%   Uso:  [d1, d2] = diferencias_finitas(@sin, 1.0);
    if nargin < 3, h = 1e-5; end
    d1 = (f(x+h) - f(x-h))/(2*h);
    d2 = (f(x+h) - 2*f(x) + f(x-h))/h^2;
end
